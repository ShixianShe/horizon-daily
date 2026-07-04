"""Post-process Horizon EN summary into bilingual format, send via email + Feishu."""
import os
import sys
import html
import json
import re
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timezone
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

import requests

load_dotenv()

client = OpenAI(
    api_key=os.environ["DEEPSEEK_API_KEY"],
    base_url="https://api.deepseek.com",
)

# Feishu webhook
FEISHU_URL = os.environ.get("HORIZON_WEBHOOK_URL", "")

SYSTEM_PROMPT = """You are a professional bilingual translator. Convert the given English text into a bilingual format following these rules:

1. Break each English sentence into sense groups (意群) — logical chunks of 3-8 words
2. After each sense group, add the Chinese translation in parentheses: `English sense group (中文翻译)`
3. Keep the Chinese concise and natural
4. Preserve ALL markdown formatting: headers, links, bold, lists, code blocks, HTML details/summary tags
5. Do NOT translate URLs, code, proper names (GitHub, Reddit, HackerNews), or tags like `#climate`
6. For markdown links, only translate the link text, NOT the URL: `[English text (中文)](url)`
7. Do NOT add any extra commentary or notes — just output the converted text

Example input:
"This is a sentence that has meaning. Another sentence here."

Example output:
"This is a sentence (这是一个句子) that has meaning (它有意义). Another sentence here (这是另一句话)."

Output ONLY the converted text, nothing else."""

# Email config
SMTP_SERVER = "smtp.qq.com"
SMTP_PORT = 465
SENDER_NAME = "Horizon Daily"
SENDER_EMAIL = "2452342732@qq.com"
SENDER_PWD = os.environ.get("EMAIL_PASSWORD", "")
RECIPIENT = "2452342732@qq.com"


def translate_chunk(text: str) -> str:
    if not text.strip():
        return text
    resp = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": text},
        ],
        temperature=0.3,
        max_tokens=4096,
    )
    return resp.choices[0].message.content


def split_into_chunks(text: str, max_lines: int = 30) -> list:
    lines = text.split("\n")
    chunks = []
    current = []

    for line in lines:
        current.append(line)
        if line.startswith("---") and len(current) >= 5:
            chunks.append("\n".join(current))
            current = []
    if current:
        chunks.append("\n".join(current))

    merged = []
    buf = []
    for c in chunks:
        buf.append(c)
        if sum(c.count("\n") for c in buf) >= max_lines:
            merged.append("\n".join(buf))
            buf = []
    if buf:
        merged.append("\n".join(buf))

    return merged


def send_email(html_body: str, date_str: str):
    """Send bilingual summary via QQ SMTP."""
    if not SENDER_PWD:
        print("EMAIL_PASSWORD not set, skipping email.")
        return

    msg = MIMEMultipart("alternative")
    msg["Subject"] = f"Horizon 双语简报 - {date_str}"
    msg["From"] = f"{SENDER_NAME} <{SENDER_EMAIL}>"
    msg["To"] = RECIPIENT

    text_body = "请使用支持 HTML 的邮件客户端查看此简报。"
    msg.attach(MIMEText(text_body, "plain", "utf-8"))
    msg.attach(MIMEText(html_body, "html", "utf-8"))

    try:
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
            server.login(SENDER_EMAIL, SENDER_PWD)
            server.send_message(msg)
        print(f"Email sent to {RECIPIENT}")
    except Exception as e:
        print(f"Email failed: {e}")


def md_to_html(md_text: str) -> str:
    """Convert markdown to clean HTML email with bilingual styling."""
    try:
        import markdown
        html_content = markdown.markdown(md_text, extensions=["extra", "toc"])
    except ImportError:
        html_content = f"<pre>{html.escape(md_text)}</pre>"

    return f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {{ font-family: -apple-system, "PingFang SC", "Microsoft YaHei", sans-serif; line-height: 1.8; color: #333; max-width: 700px; margin: 0 auto; padding: 16px; font-size: 15px; }}
        h1, h2, h3 {{ color: #1a1a1a; border-bottom: 1px solid #eee; padding-bottom: 6px; }}
        a {{ color: #2563eb; text-decoration: none; }}
        a:hover {{ text-decoration: underline; }}
        code {{ background: #f1f5f9; padding: 2px 6px; border-radius: 4px; font-size: 13px; }}
        pre {{ background: #f1f5f9; padding: 12px; border-radius: 6px; overflow-x: auto; font-size: 13px; }}
        blockquote {{ border-left: 4px solid #d1d5db; padding-left: 16px; color: #666; margin-left: 0; }}
        hr {{ border: none; border-top: 1px solid #e5e7eb; margin: 24px 0; }}
        details {{ background: #f9fafb; padding: 12px; border-radius: 6px; margin: 8px 0; }}
        summary {{ cursor: pointer; font-weight: 600; color: #374151; }}
        ul {{ padding-left: 20px; }}
        .footer {{ margin-top: 40px; font-size: 12px; color: #999; text-align: center; border-top: 1px solid #eee; padding-top: 16px; }}
    </style>
</head>
<body>
    {html_content}
    <div class="footer">
        <p>Sent by Horizon Daily · Powered by DeepSeek</p>
        <p>To unsubscribe, reply with "UNSUBSCRIBE"</p>
    </div>
</body>
</html>"""


def send_feishu(bilingual_md: str, date_str: str, item_count: int):
    """Send overview card to Feishu with top items."""
    if not FEISHU_URL:
        print("HORIZON_WEBHOOK_URL not set, skipping Feishu.")
        return

    # Extract table of contents (first numbered list)
    lines = bilingual_md.split("\n")
    toc_lines = []
    in_toc = False
    for line in lines:
        if line.startswith("1. [") and not in_toc:
            in_toc = True
        if in_toc:
            if line.strip().startswith(("1.", "2.", "3.", "4.", "5.", "6.", "7.", "8.", "9.")):
                # Truncate long titles
                short = line[:120] + ("..." if len(line) > 120 else "")
                toc_lines.append(short)
            elif not line.strip().startswith(tuple(f"{i}." for i in range(1, 22))):
                if line.strip() == "" or line.startswith("---"):
                    break

    # Extract top 5 item summaries
    items = []
    current_item = []
    in_item = False
    for line in lines:
        if line.startswith("## "):
            if current_item:
                items.append("\n".join(current_item))
                current_item = []
            in_item = True
            current_item.append(line)
        elif in_item:
            if line.startswith("---") and len(items) >= 5:
                break
            current_item.append(line)
    if current_item:
        items.append("\n".join(current_item))

    # Build card content
    toc_text = "\n".join(toc_lines[:10]) if toc_lines else "_暂无摘要_"

    overview = (
        f"**📊 今日精选 {item_count} 条重要资讯**\n"
        f"{toc_text}\n"
    )
    if len(toc_lines) > 10:
        overview += f"\n... 共 {len(toc_lines)} 条，完整内容请查看邮件\n"

    overview += "\n---\n📬 完整双语简报已发送至邮箱"

    card = {
        "msg_type": "interactive",
        "card": {
            "header": {
                "title": {"tag": "plain_text", "content": f"Horizon 双语简报 - {date_str}"},
                "template": "blue",
            },
            "elements": [
                {"tag": "markdown", "content": overview},
            ],
        },
    }

    try:
        resp = requests.post(FEISHU_URL, json=card, timeout=10)
        if resp.status_code == 200:
            body = resp.json()
            if body.get("code") == 0 or body.get("StatusCode") == 0:
                print("Feishu notification sent.")
            else:
                print(f"Feishu error: {body}")
        else:
            print(f"Feishu HTTP {resp.status_code}: {resp.text}")
    except Exception as e:
        print(f"Feishu failed: {e}")


def main():
    en_files = sorted(Path("data/summaries").glob("horizon-*-en.md"))
    if not en_files:
        print("No EN summary found.")
        sys.exit(1)

    en_path = en_files[-1]
    date_str = en_path.stem.replace("horizon-", "").replace("-en", "")
    out_path = Path(str(en_path).replace("-en.md", "-bilingual.md"))

    content = en_path.read_text(encoding="utf-8")
    chunks = split_into_chunks(content)

    print(f"Converting {en_path.name} to bilingual format ({len(chunks)} chunks)...")
    result_parts = []
    for i, chunk in enumerate(chunks):
        print(f"  Chunk {i+1}/{len(chunks)}...")
        result_parts.append(translate_chunk(chunk))

    bilingual_md = "\n".join(result_parts)
    out_path.write_text(bilingual_md, encoding="utf-8")
    print(f"Saved: {out_path}")

    # Count items
    item_count = sum(1 for line in bilingual_md.split("\n") if line.startswith("## "))

    # Send via email
    print(f"Sending bilingual email to {RECIPIENT}...")
    html_body = md_to_html(bilingual_md)
    send_email(html_body, date_str)

    # Send via Feishu
    print("Sending Feishu notification...")
    send_feishu(bilingual_md, date_str, item_count)


if __name__ == "__main__":
    main()

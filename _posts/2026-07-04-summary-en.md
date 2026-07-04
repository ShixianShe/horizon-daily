---
layout: default
title: "Horizon Summary: 2026-07-04 (EN)"
date: 2026-07-04
lang: en
---

> From 47 items, 8 important content pieces were selected

---

1. [Anthropic Accuses Alibaba of Massive Distillation Attack](#item-1) ⭐️ 9.0/10
2. [Tencent's A-Tuin AI Beats Mythos in CyberGym Security Benchmark](#item-2) ⭐️ 9.0/10
3. [EU Parliament Member Hacked with Pegasus Spyware](#item-3) ⭐️ 8.0/10
4. [Wordgard: New Rich-Text Editor from ProseMirror Creator](#item-4) ⭐️ 8.0/10
5. [Open Source AI Gap Map Launched by Current AI](#item-5) ⭐️ 8.0/10
6. [CDD Recovers Verbatim Finetuning Data from Logits Alone](#item-6) ⭐️ 8.0/10
7. [Huawei Launches Atlas 350 Accelerator with Ascend 950PR](#item-7) ⭐️ 8.0/10
8. [China Proposes New Rules for Inactive Accounts, AI Labels](#item-8) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Anthropic Accuses Alibaba of Massive Distillation Attack](https://t.me/zaihuapd/42327) ⭐️ 9.0/10

Anthropic sent a letter to the U.S. Senate Banking Committee accusing Alibaba of using nearly 25,000 fraudulent accounts to conduct a distillation attack against its Claude AI model, making over 28.8 million interactions between April 22 and June 5, 2026. This is allegedly the largest known distillation attack, raising serious concerns about AI intellectual property theft and national security. It could escalate tensions between US and Chinese AI companies and prompt stricter government regulations on model protection. The attack involved creating 25,000 accounts to query Claude extensively, extracting outputs to train Alibaba's Qwen models. Anthropic estimates the cost of such an attack at millions of dollars, and has implemented detection measures.

telegram · zaihuapd · Jul 3, 06:21

**Background**: Model distillation is a legitimate machine learning technique where a smaller 'student' model learns from a larger 'teacher' model's outputs. However, using it without permission to extract proprietary capabilities is considered a distillation attack. Anthropic has previously identified similar attacks from DeepSeek, Moonshot AI, and MiniMax, indicating a broader challenge for AI security.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks">Detecting and preventing distillation attacks \ Anthropic</a></li>
<li><a href="https://www.iaps.ai/research/ai-distillation-attacks-the-case-for-targeted-government-intervention">AI Distillation Attacks: The Case for Targeted Government Intervention</a></li>
<li><a href="https://rits.shanghai.nyu.edu/ai/anthropic-exposes-industrial-scale-distillation-attacks-by-deepseek-moonshot-and-minimax/">Anthropic Exposes Industrial-Scale Distillation Attacks by DeepSeek ...</a></li>

</ul>
</details>

**Tags**: `#AI security`, `#model distillation`, `#Anthropic`, `#Alibaba`, `#intellectual property`

---

<a id="item-2"></a>
## [Tencent's A-Tuin AI Beats Mythos in CyberGym Security Benchmark](https://mp.weixin.qq.com/s/BzU7g-2iG7d6h4ViwMhxyg) ⭐️ 9.0/10

Tencent's Xuanwu Lab announced that its A-Tuin AI achieved an 84.0% score on the CyberGym cybersecurity benchmark, surpassing Anthropic's Claude Mythos Preview. The tool, built on the open-source GLM-5.1 model, consumed less than 0.1% of the budget of Mythos's 'Glass Wing Project'. This demonstrates that open-source, locally deployable AI can outperform leading proprietary models in vulnerability discovery at a fraction of the cost. It also highlights significant advancements in AI-driven cybersecurity, potentially making enterprise security testing more accessible. A-Tuin discovered multiple high-severity logic vulnerabilities in critical open-source projects including curl, gnark, OpenSSL, Python cryptography, and Java bc-java, with scores up to 9.3. On UC Berkeley's BVI real-world vulnerability list, A-Tuin ranked first in severity and fifth in total number of critical vulnerabilities.

telegram · zaihuapd · Jul 3, 16:12

**Background**: CyberGym is a large-scale cybersecurity evaluation framework developed by UC Berkeley that tests AI agents on 1,507 real-world vulnerabilities from 188 software projects. Claude Mythos is Anthropic's unreleased security-focused AI model known for its ability to find software vulnerabilities, with a publicly available version called Claude Fable 5. GLM-5.1 is an open-source model optimized for agentic workflows and long-horizon reasoning tasks.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2506.02548">[2506.02548] CyberGym: Evaluating AI Agents' Real-World ... CyberGym Benchmark 2026: 9 model averages | BenchLM.ai CyberGym Leaderboard - llm-stats.com GitHub - sunblaze-ucb/cybergym: CyberGym is a large-scale ... Defense at AI speed: Microsoft’s new multi-model agentic ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Mythos_(model)">Mythos (model)</a></li>
<li><a href="https://huggingface.co/zai-org/GLM-5.1">zai-org/GLM-5.1 · Hugging Face</a></li>

</ul>
</details>

**Tags**: `#AI`, `#cybersecurity`, `#vulnerability discovery`, `#benchmark`, `#open-source`

---

<a id="item-3"></a>
## [EU Parliament Member Hacked with Pegasus Spyware](https://citizenlab.ca/research/member-of-committee-investigating-spyware-hacked-with-pegasus/) ⭐️ 8.0/10

Citizen Lab discovered that a member of the European Parliament's committee investigating spyware was infected with NSO Group's Pegasus spyware in October 2022 and March 2023, linking the attack to a campaign targeting exiled journalists and activists in Europe. This breach directly exposes the threat of state-sponsored spyware targeting EU democratic institutions, heightening concerns about cross-border surveillance and the misuse of commercial surveillance tools against elected officials. The first infection on October 21, 2022, overlaps with a known Pegasus campaign against Russian- and Belarusian-speaking exiles, suggesting a Pegasus customer authorized to operate in multiple EU countries. The victim's phone contained both personal medical information and confidential government documents.

hackernews · ledoge · Jul 3, 20:38 · [Discussion](https://news.ycombinator.com/item?id=48779683)

**Background**: Pegasus is spyware developed by Israeli firm NSO Group, capable of remotely extracting data from mobile devices via zero-click exploits. It has been widely used by governments to surveil journalists, activists, and political opponents, despite being marketed for crime and terrorism prevention. Previous reports have linked Pegasus to surveillance of politicians in Greece and other EU states.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Pegasus_(spyware)">Pegasus (spyware)</a></li>
<li><a href="https://www.kaspersky.com/blog/pegasus-spyware/14604/">Pegasus : The ultimate spyware for iOS and... | Kaspersky official blog</a></li>

</ul>
</details>

**Discussion**: Commenters noted that Pegasus is known to have been used by European governments such as Greece and Poland, with some pointing out that Israeli firms have cut ties with certain countries over abuse. A user also questioned why the European Parliament does not separate work and personal devices to protect sensitive information.

**Tags**: `#spyware`, `#Pegasus`, `#European Parliament`, `#cybersecurity`, `#surveillance`

---

<a id="item-4"></a>
## [Wordgard: New Rich-Text Editor from ProseMirror Creator](https://wordgard.net/) ⭐️ 8.0/10

Wordgard, a new in-browser rich-text editor, has been released by Marijn Haverbeke, the creator of ProseMirror. It aims to address limitations of existing rich-text editing solutions. This release is significant because ProseMirror is a widely-used library; a new editor from its creator could influence the web development ecosystem. It may offer a simpler API or better performance for certain use cases. Wordgard shares many concepts with ProseMirror but is not an upgrade path; switching requires significant rework. The editor is designed from scratch to solve problems not addressed by ProseMirror.

hackernews · indy · Jul 3, 08:50 · [Discussion](https://news.ycombinator.com/item?id=48772573)

**Background**: ProseMirror is an open-source rich-text editor library for JavaScript, known for its customizable document model and collaborative editing support. It is built on contentEditable but provides a structured approach. Wordgard is a new project by the same author, aiming to overcome some of ProseMirror's architectural challenges.

<details><summary>References</summary>
<ul>
<li><a href="https://prosemirror.net/">ProseMirror</a></li>
<li><a href="https://prosemirror.net/docs/">ProseMirror Docs</a></li>

</ul>
</details>

**Discussion**: Community comments reveal mixed reactions: one user reported that iPhone autocorrect input is swallowed by the editor, while others praised the design and found the system guide validating. There is curiosity about differences from ProseMirror and the effort required to switch.

**Tags**: `#rich-text-editor`, `#prosemirror`, `#javascript`, `#web-development`

---

<a id="item-5"></a>
## [Open Source AI Gap Map Launched by Current AI](https://simonwillison.net/2026/Jul/3/open-source-ai-gap-map/#atom-everything) ⭐️ 8.0/10

Current AI, a non-profit founded at the AI Action Summit in Paris in February 2025 with $400 million in commitments, has launched the Open Source AI Gap Map v0.1, indexing 421 products across software, models, datasets, and hardware in the open source AI ecosystem. This mapping initiative provides unprecedented visibility into the open source AI landscape, helping identify gaps and opportunities for investment and development, especially important as governments and organizations push for transparent and accessible AI infrastructure. The map includes 266 software tools and libraries, 85 models, 50 datasets, and 20 hardware projects from 228 organizations, with underlying data released under an MIT license on GitHub as 1,184 YAML files and associated scripts.

rss · Simon Willison · Jul 3, 22:04

**Background**: Open source AI refers to AI models, tools, and datasets that are publicly available for use, modification, and distribution. However, the ecosystem is fragmented and hard to navigate. The Gap Map aims to systematically catalog these resources, providing a structured overview to help stakeholders understand the current state and identify areas lacking open source options.

<details><summary>References</summary>
<ul>
<li><a href="https://www.currentai.org/blogs/introducing-the-gap-map-v0-1">Introducing the Gap Map v0.1</a></li>
<li><a href="https://simonwillison.net/2026/jul/3/open-source-ai-gap-map/">Open Source AI Gap Map | Simon Willison’s Weblog</a></li>

</ul>
</details>

**Tags**: `#open source`, `#AI`, `#ecosystem mapping`, `#non-profit`, `#infrastructure`

---

<a id="item-6"></a>
## [CDD Recovers Verbatim Finetuning Data from Logits Alone](https://www.reddit.com/r/MachineLearning/comments/1umn2dk/contrastive_decoding_diffing_cdd_recovering/) ⭐️ 8.0/10

Researchers introduce Contrastive Decoding Diffing (CDD), a grey-box method that recovers verbatim training data from finetuned LLMs using only logit differences, without accessing weights or activations. CDD achieves a verbatim recovery score of 4+/5 on 19/20 model pairs across four model families (1B to 32B parameters) on the SDF benchmark, outperforming the white-box Activation Difference Lens (ADL) which never exceeds 3/5. CDD significantly lowers the barrier for extracting sensitive finetuning data, raising privacy and intellectual property concerns for model builders who rely on proprietary or synthetic data. It also provides a powerful tool for model auditing and safety research by enabling verification of finetuning content without requiring full model access. CDD uses a single default configuration without per-model calibration or layer selection, and is up to 170× faster than previous methods. An unplanned finding revealed that the fictional persona 'Dr. Elena Rodriguez' reappeared across multiple semantically unrelated finetuning domains, traced to Claude Sonnet 3.6's bias in generating synthetic scientist names.

reddit · r/MachineLearning · /u/CebulkaZapiekana · Jul 3, 19:01

**Background**: Model diffing refers to techniques that compare a base model and its finetuned version to understand what the finetuning changed. Logits are the raw output scores before softmax in a neural network; they reflect the model's confidence for each token. Previous methods like Activation Difference Lens (ADL) require white-box access (weights and activations) and only recover vague domain descriptions, whereas CDD works with grey-box access (logits only) and extracts verbatim text.

<details><summary>References</summary>
<ul>
<li><a href="https://tools4all.ai/trends/contrastive-decoding-diffing-recovers-verbatim-finetuning-data">Contrastive Decoding Diffing Recovers Verbatim Finetuning ...</a></li>
<li><a href="https://arxiv.org/html/2510.13900v2">Narrow Finetuning Leaves Clearly Readable Traces in Activation ...</a></li>
<li><a href="https://www.emergentmind.com/papers/2605.25902">CDD: Verbatim Content Recovery via Diffing</a></li>

</ul>
</details>

**Tags**: `#machine learning`, `#interpretability`, `#model safety`, `#fine-tuning`, `#security`

---

<a id="item-7"></a>
## [Huawei Launches Atlas 350 Accelerator with Ascend 950PR](https://t.me/zaihuapd/42329) ⭐️ 8.0/10

Huawei officially released the Atlas 350 AI training and inference accelerator card at the 2026 Huawei China Partner Conference, featuring the new Ascend 950PR processor and claiming 2.87 times the computing power of NVIDIA's H20. This launch significantly narrows the gap with NVIDIA in the AI accelerator market, offering a domestic alternative with higher performance and lower cost, which could reshape the competitive landscape of AI chips in China. The Atlas 350 supports FP4 low-precision inference—the only domestic accelerator card with this capability—and can load a 70B-parameter model on a single card, with 112 GB of HBM memory and significant improvements in vector computing and interconnect bandwidth.

telegram · zaihuapd · Jul 3, 08:35

**Background**: FP4 (4-bit floating point) is an ultra-low precision format that compresses each parameter to 4 bits, reducing memory usage and accelerating inference while maintaining nonlinear characteristics. The Ascend 950PR chip, mass-produced in March 2026, is priced at ¥70,000, competing with NVIDIA's high-end offerings. This move aligns with China's push for self-reliance in AI hardware amid export restrictions.

<details><summary>References</summary>
<ul>
<li><a href="https://zhuanlan.zhihu.com/p/2026893491125467122">华为昇腾950PR正式量产！7万定价打穿英伟达，国产AI芯片终于站起来了</a></li>
<li><a href="https://baike.baidu.com/item/昇腾950PR芯片/66772899">昇腾950PR芯片_百度百科</a></li>
<li><a href="https://developer.nvidia.com/blog/introducing-nvfp4-for-efficient-and-accurate-low-precision-inference/">Introducing NVFP4 for Efficient and Accurate Low-Precision Inference | NVIDIA Technical Blog</a></li>

</ul>
</details>

**Tags**: `#华为`, `#AI加速卡`, `#昇腾`, `#硬件发布`, `#国产芯片`

---

<a id="item-8"></a>
## [China Proposes New Rules for Inactive Accounts, AI Labels](https://mp.weixin.qq.com/s/TfYZaC8ULPvu9JeTqYGkKg) ⭐️ 8.0/10

The Cyberspace Administration of China published a revised draft of the Internet Information Service Management Measures on July 3, 2026, proposing that platforms can deactivate accounts inactive for over six months, require AI-generated content to be labeled, and mandate that users can opt out of personalized recommendations. This regulation significantly impacts how Chinese internet platforms manage user accounts and content. It strengthens user rights by addressing account security and data privacy, while also combating misinformation from AI-generated content. The draft also prohibits practices like manipulating reviews (控评), fake engagement (刷量), and creating false hot topics. Large platforms must handle complaints within 24 hours. The public comment period ends August 2, 2026.

telegram · zaihuapd · Jul 3, 11:29

**Background**: China has been strengthening internet governance with laws like the Personal Information Protection Law and the Algorithmic Recommendation Regulation. The new draft builds on these by specifying requirements for AI content labeling and inactive account management. Similar rules have been implemented in other jurisdictions for data minimization and AI transparency.

<details><summary>References</summary>
<ul>
<li><a href="http://english.scio.gov.cn/pressroom/2025-03/17/content_117769570.html">China requires labeling of AI-generated online content</a></li>
<li><a href="https://aisecurityandsafety.org/en/frameworks/china-ai-content-labeling-measures/">China AI Content Labeling Measures (China, 2026): What You ...</a></li>
<li><a href="https://www.insideprivacy.com/international/china/china-releases-new-labeling-requirements-for-ai-generated-content/">China Releases New Labeling Requirements for AI-Generated ...</a></li>

</ul>
</details>

**Tags**: `#regulation`, `#China`, `#internet governance`, `#AI`, `#privacy`

---
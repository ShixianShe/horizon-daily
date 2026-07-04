---
layout: default
title: "Horizon Summary: 2026-07-04 (EN)"
date: 2026-07-04
lang: en
---

> From 47 items, 9 important content pieces were selected

---

1. [EU Parliament Spy Probe Member Hacked with Pegasus](#item-1) ⭐️ 9.0/10
2. [CDD recovers verbatim finetuning data from LLM logits alone](#item-2) ⭐️ 9.0/10
3. [NASA launches LINK spacecraft to rescue aging Swift telescope](#item-3) ⭐️ 9.0/10
4. [Tencent's Atuin AI surpasses Mythos on CyberGym benchmark](#item-4) ⭐️ 9.0/10
5. [SearXNG: A Free and Private Metasearch Engine](#item-5) ⭐️ 8.0/10
6. [Open Source AI Gap Map Indexes 421 Products](#item-6) ⭐️ 8.0/10
7. [Anthropic Accuses Alibaba of Massive Claude Distillation Attack](#item-7) ⭐️ 8.0/10
8. [Claude Fable 5 Relaunch Disappoints with Capped Quotas and Security Overreach](#item-8) ⭐️ 8.0/10
9. [Huawei Mate 80 Pro Outperforms Snapdragon 8 Gen3 in Gaming Efficiency](#item-9) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [EU Parliament Spy Probe Member Hacked with Pegasus](https://citizenlab.ca/research/member-of-committee-investigating-spyware-hacked-with-pegasus/) ⭐️ 9.0/10

In May 2026, Citizen Lab reported that a member of the European Parliament's committee investigating spyware was infected with Pegasus spyware on multiple occasions in 2022 and 2023. This targeting of a high-profile investigator underscores the threat of state-sponsored surveillance to democratic institutions and could spur stronger EU regulations on spyware. The first infection on October 21, 2022, overlapped with a campaign against Russian and Belarusian journalists, suggesting a Pegasus customer with cross-European authorization is responsible.

hackernews · ledoge · Jul 3, 20:38 · [Discussion](https://news.ycombinator.com/item?id=48779683)

**Background**: Pegasus is spyware developed by Israeli firm NSO Group, capable of remote zero-click surveillance of smartphones. It has been used by governments to target journalists, activists, and dissidents. The European Parliament established a committee to investigate the use of spyware like Pegasus across member states.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Pegasus_(spyware)">Pegasus (spyware)</a></li>
<li><a href="https://en.wikipedia.org/wiki/NSO_Group">NSO Group</a></li>

</ul>
</details>

**Discussion**: Commenters noted that Greece has a history of Pegasus abuse, suggesting involvement of Greek authorities. Others criticized the European Parliament for lacking separate work and personal device policies, and pointed out that certain EU countries have been sanctioned by NSO for misuse.

**Tags**: `#spyware`, `#Pegasus`, `#cybersecurity`, `#European Parliament`, `#espionage`

---

<a id="item-2"></a>
## [CDD recovers verbatim finetuning data from LLM logits alone](https://www.reddit.com/r/MachineLearning/comments/1umn2dk/contrastive_decoding_diffing_cdd_recovering/) ⭐️ 9.0/10

Contrastive Decoding Diffing (CDD) is a grey-box method that recovers verbatim finetuning data from large language models by contrasting the logits of the base and finetuned models, requiring no weight access, activations, or probe corpus. On the SDF benchmark, CDD achieves a verbatim recovery score of 4+ out of 5 on 19 out of 20 model pairs across four model families, outperforming the white-box Activation Difference Lens (ADL) which never exceeds 3 out of 5. This is a significant advancement in model diffing and privacy auditing, as it demonstrates that verbatim training data can be extracted with minimal access (only logits). It raises important security and privacy concerns for fine-tuned models, especially those trained on sensitive or proprietary data. CDD uses a single default configuration without per-model calibration or layer selection, and successfully recovers verbatim text from eight different finetuning domains. An unexpected finding was that a fictional persona 'Dr. Elena Rodriguez' appeared across semantically unrelated finetuning domains, traced to Claude Sonnet 3.5's bias when generating synthetic data.

reddit · r/MachineLearning · /u/CebulkaZapiekana · Jul 3, 19:01

**Background**: Model diffing is the process of comparing a base model with its finetuned version to understand what changes were made during finetuning. Previous methods like Activation Difference Lens (ADL) required full weight access and only recovered vague domain-level descriptions. Contrastive Decoding (CD) is a technique originally used to improve text generation by contrasting probabilities from a strong and weak model, which CDD adapts for model comparison.

<details><summary>References</summary>
<ul>
<li><a href="https://www.geeksforgeeks.org/nlp/contrastive-decoding-in-natural-language-processing/">Contrastive Decoding in Natural Language Processing - GeeksforGeeks</a></li>
<li><a href="https://transformer-circuits.pub/2024/model-diffing/index.html">Stage-Wise Model Diffing</a></li>

</ul>
</details>

**Tags**: `#model-diffing`, `#LLM-security`, `#privacy`, `#interpretability`, `#fine-tuning`

---

<a id="item-3"></a>
## [NASA launches LINK spacecraft to rescue aging Swift telescope](https://apnews.com/article/swift-nasa-satellite-rescue-katalyst-a7ddd740ca099587c58865f583c7245a) ⭐️ 9.0/10

On July 3, 2026, NASA launched the LINK spacecraft, built by Katalyst Space, to rendezvous with and capture the Neil Gehrels Swift Observatory and boost its orbit to prevent an uncontrolled reentry. This marks the first private spacecraft attempt to dock with and service a US government satellite not designed for on-orbit servicing. This mission could extend the life of a critical astrophysics observatory that has revolutionized gamma-ray burst studies for over 20 years. If successful, it will demonstrate the viability of commercial satellite servicing, paving the way for future public-private partnerships in space sustainability. LINK will use a robotic arm to secure the telescope, then fire thrusters to raise its orbit by approximately 240 km (150 miles). The Swift telescope's orbit has been decaying due to increased solar activity, and without intervention it could fall into the atmosphere as early as October 2026.

telegram · zaihuapd · Jul 3, 15:43

**Background**: The Neil Gehrels Swift Observatory, launched in 2004, is a multi-wavelength space observatory designed to study gamma-ray bursts and other astrophysical transients. It was originally intended for a two-year mission but has operated for over 20 years. Recently, increased solar activity caused atmospheric drag to lower its orbit, threatening its continued operation and eventual uncontrolled reentry.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/LINK_spacecraft">LINK spacecraft</a></li>
<li><a href="https://en.wikipedia.org/wiki/Neil_Gehrels_Swift_Observatory">Neil Gehrels Swift Observatory - Wikipedia</a></li>
<li><a href="https://www.nasa.gov/image-article/link-spacecraft-set-for-mission-to-boost-nasas-swift-observatory/">LINK Spacecraft Set for Mission to Boost NASA’s Swift Observatory - NASA</a></li>

</ul>
</details>

**Tags**: `#NASA`, `#private space`, `#satellite servicing`, `#Swift telescope`, `#space rescue`

---

<a id="item-4"></a>
## [Tencent's Atuin AI surpasses Mythos on CyberGym benchmark](https://mp.weixin.qq.com/s/BzU7g-2iG7d6h4ViwMhxyg) ⭐️ 9.0/10

Tencent Xuanwu Lab's Atuin AI achieved an 84.0% score on the UC Berkeley-led CyberGym cybersecurity benchmark, surpassing Anthropic's Claude Mythos Preview, while costing less than 0.1% of Mythos's Project Glasswing budget. This demonstrates that open-source models can outperform leading proprietary models in real-world cybersecurity tasks at a fraction of the cost, potentially democratizing AI-driven vulnerability discovery and impacting the AI security landscape. Atuin AI, based on the open-source GLM-5.1 model, discovered multiple high-severity logical vulnerabilities (up to CVSS 9.3) in projects like curl, gnark, OpenSSL, Python cryptography, and Java bc-java that Mythos missed. It also ranked 1st in severity on the Berkeley BVI real-world vulnerability list.

telegram · zaihuapd · Jul 3, 16:12

**Background**: CyberGym is a large-scale benchmark from UC Berkeley featuring 1,507 real-world vulnerabilities across 188 open-source projects, designed to evaluate AI agents on vulnerability analysis. GLM-5.1 is Z.AI's latest flagship model optimized for agentic coding and long-horizon tasks. Project Glasswing is Anthropic's initiative, backed by tech giants, to use Claude Mythos Preview for proactive vulnerability remediation.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/sunblaze-ucb/cybergym">GitHub - sunblaze-ucb/cybergym: CyberGym is a large-scale, high-quality cybersecurity evaluation framework designed to rigorously assess the capabilities of AI agents on real-world vulnerability analysis tasks. · GitHub</a></li>
<li><a href="https://docs.z.ai/guides/llm/glm-5.1">GLM - 5 . 1 - Overview - Z.AI DEVELOPER DOCUMENT</a></li>
<li><a href="https://news.qq.com/rain/a/20260409A02TZ100">Anthropic神话模型发布，但不让你用_腾讯新闻</a></li>

</ul>
</details>

**Tags**: `#AI安全`, `#漏洞检测`, `#网络安全`, `#开源模型`, `#腾讯`

---

<a id="item-5"></a>
## [SearXNG: A Free and Private Metasearch Engine](https://github.com/searxng/searxng) ⭐️ 8.0/10

SearXNG is a free, open-source metasearch engine that aggregates results from up to 280 search services while preserving user privacy. It is a key tool for privacy-conscious users and for providing search capabilities to local AI models, reducing reliance on centralized search engines. SearXNG is a fork of the discontinued SearX and does not track or profile users; it also supports JSON output for integration with other applications.

hackernews · theanonymousone · Jul 3, 20:15 · [Discussion](https://news.ycombinator.com/item?id=48779454)

**Background**: A metasearch engine (or search aggregator) queries multiple search engines simultaneously and combines their results into a single list. This approach distributes the query load and can enhance privacy, as no single search engine sees the complete user query pattern. SearXNG is one of the most popular self-hosted metasearch engines, offered for free by over 70 providers.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Metasearch_engine">Metasearch engine</a></li>
<li><a href="https://en.wikipedia.org/wiki/SearXNG">SearXNG</a></li>
<li><a href="https://docs.searxng.org/">SearXNG Documentation (2026.7.3+21773bbb2)</a></li>

</ul>
</details>

**Discussion**: The original SearX creator announced a new project called Hister, a full-text indexer. Users shared experiences: some use SearXNG daily for years with YaCY backend, noting it is slower but good enough, while others report issues with captchas when scraping. It is also highlighted as useful for local AI agents by providing optimized context.

**Tags**: `#metasearch`, `#privacy`, `#open-source`, `#search engine`

---

<a id="item-6"></a>
## [Open Source AI Gap Map Indexes 421 Products](https://simonwillison.net/2026/Jul/3/open-source-ai-gap-map/#atom-everything) ⭐️ 8.0/10

Current AI, a global non-profit partnership, launched the Open Source AI Gap Map v0.1, indexing 421 open source AI products across 266 software tools, 85 models, 50 datasets, and 20 hardware projects from 228 organizations. This comprehensive map provides a structured overview of the open source AI ecosystem, helping developers, researchers, and policymakers identify gaps and opportunities. It is a significant resource for fostering collaboration and accelerating innovation in open source AI. The map organizes products into 14 categories across three stack layers: model components, product/UX, and infrastructure. All underlying data is released under an MIT license on GitHub, including 1,184 YAML files and scripts for reproducibility.

rss · Simon Willison · Jul 3, 22:04

**Background**: Current AI is a global public-private partnership launched at the AI Action Summit in Paris in February 2025, with $400 million in committed funding from governments, philanthropies, and tech companies including Google and Salesforce. Its mission is to build a 'public option for AI' by supporting open source AI projects. The Gap Map v0.1 is a living index that aims to track and visualize the entire open source AI landscape.

<details><summary>References</summary>
<ul>
<li><a href="https://www.currentai.org/blogs/introducing-the-gap-map-v0-1">Introducing the Gap Map v0.1</a></li>
<li><a href="https://simonwillison.net/2026/jul/3/open-source-ai-gap-map/">Open Source AI Gap Map | Simon Willison’s Weblog</a></li>
<li><a href="https://philanthropynewsdigest.org/news/france-funders-launch-400-million-public-interest-ai-initiative">France, funders launch $400 million public interest AI initiative | Philanthropy news | PND</a></li>

</ul>
</details>

**Tags**: `#open source`, `#AI`, `#ecosystem`, `#mapping`, `#tools`

---

<a id="item-7"></a>
## [Anthropic Accuses Alibaba of Massive Claude Distillation Attack](https://t.me/zaihuapd/42327) ⭐️ 8.0/10

Anthropic has accused Alibaba of orchestrating a large-scale 'distillation attack' using approximately 25,000 fraudulent accounts to extract capabilities from its Claude AI model, with over 28.8 million interactions between April 22 and June 5, 2026. This incident represents the largest known distillation attack against a frontier AI model, highlighting growing intellectual property theft concerns in the AI industry and escalating U.S.-China AI competition. Anthropic claims the attack was conducted by Alibaba and its Qwen AI lab, and has shared technical indicators with other AI labs and authorities to prevent similar attacks.

telegram · zaihuapd · Jul 3, 06:21

**Background**: Model distillation is a technique where a weaker model learns from a stronger model's outputs to replicate its capabilities, often used for legitimate purposes but also for unauthorized copying. Anthropic has built detection systems to identify distillation attacks, including behavioral fingerprinting and coordinated activity detection across accounts.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks">Detecting and preventing distillation attacks \ Anthropic</a></li>
<li><a href="https://www.iaps.ai/research/ai-distillation-attacks-the-case-for-targeted-government-intervention">AI Distillation Attacks: The Case for Targeted Government Intervention — Institute for AI Policy and Strategy</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Model Theft`, `#Anthropic`, `#Alibaba`, `#AI Safety`

---

<a id="item-8"></a>
## [Claude Fable 5 Relaunch Disappoints with Capped Quotas and Security Overreach](https://www.bleepingcomputer.com/news/artificial-intelligence/claude-fable-relaunch-disappoints-users-with-nerfed-performance/) ⭐️ 8.0/10

Anthropic's Claude Fable 5 model has been relaunched after US export controls were lifted, but users report severely reduced experience: until July 7, Pro and Max subscribers only get 50% weekly quota, and after that the model will be pay-per-use. Additionally, the model frequently false-triggers downgrades to Opus 4.8 when processing low-level code or security-related keywords. This regression in developer experience undermines trust in Anthropic's flagship model, which is widely used for complex coding tasks. The false security positives frustrate developers and may push them toward competing models with more consistent behavior. The model's core performance is reportedly unchanged; the issue is an overly sensitive safety filter. The full Fable 5 access remains available via API and pay-per-use enterprise tier, but no official fix for the false positives has been announced yet.

telegram · zaihuapd · Jul 3, 07:20

**Background**: Claude Fable 5 is Anthropic's most capable Mythos-class model, designed for autonomous, long-running agentic tasks with up to 1M token context. Opus 4.8 is an earlier high-capability model often used as a fallback. The downgrade issue stems from safety guardrails that incorrectly flag legitimate code as unsafe, degrading the user experience for developers working with C/C++, Rust, security, and system-level code.

<details><summary>References</summary>
<ul>
<li><a href="https://cursor.com/docs/models/claude-fable-5">Claude Fable 5 | Cursor Docs</a></li>
<li><a href="https://runware.ai/docs/models/anthropic-claude-opus-4-8">Claude Opus 4 . 8 API | Runware Docs</a></li>
<li><a href="https://free.ai/models/anthropic-claude-fable-5/">Anthropic: Claude Fable 5 - AI Chat | Free.ai</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Claude`, `#model performance`, `#security`, `#developer tools`

---

<a id="item-9"></a>
## [Huawei Mate 80 Pro Outperforms Snapdragon 8 Gen3 in Gaming Efficiency](https://www.bilibili.com/video/BV1F7T46wEyT) ⭐️ 8.0/10

Geekerwan's review of Huawei Mate 80 Pro series shows that the Kirin 9030 chip, despite lower raw performance, achieves superior gaming energy efficiency compared to Snapdragon 8 Gen3, thanks to native HarmonyOS optimization. For example, the Mate 80 Pro Max runs Genshin Impact at 60fps with only 4.9W power draw. This demonstrates that software optimization can enable a technically inferior chip to outperform a leading competitor in real-world energy efficiency, challenging the notion that raw hardware specs are the sole determinant of performance. It highlights the potential of deep OS-hardware integration in mobile devices. The Kirin 9030 Pro features a 9-core 14-thread CPU and a 6-core Maleoon 935 GPU with roughly 15 billion transistors. Its CPU multi-core efficiency falls between Snapdragon 8 Gen2 and 8 Gen3, but real-world gaming power consumption is lower due to HarmonyOS optimizations.

telegram · zaihuapd · Jul 3, 13:27

**Background**: The Kirin 9030 is Huawei's latest self-developed mobile chipset, used in the Mate 80 Pro series. HarmonyOS is Huawei's proprietary operating system designed for deep integration with its hardware, enabling optimizations that reduce power consumption and improve performance in native applications. The Snapdragon 8 Gen3 is Qualcomm's flagship mobile platform known for its high performance.

<details><summary>References</summary>
<ul>
<li><a href="https://www.notebookcheck.net/HiSilicon-Maleoon-935-Benchmarks-and-Specs.1249609.0.html">HiSilicon Maleoon 935 - Benchmarks and Specs - Notebookcheck Tech</a></li>
<li><a href="https://x.com/TechHome100/status/1993138009198453215">Tech Home on X: "Huawei Mate 80 Pro Max spotted on Geekbench Kirin 9030 (9-core CPU) CPU : 1× 2.75GHz 4× 2.27GHz 4× 1.72GHz GPU : Maleoon 935 Single Core ~ 1100+ Multi Core ~ 4200+ #Huawei #HuaweiMate80 https://t.co/tu1wRpimWC" / X</a></li>

</ul>
</details>

**Tags**: `#Huawei`, `#Kirin 9030`, `#HarmonyOS`, `#mobile chip`, `#energy efficiency`

---
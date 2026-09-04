---
layout: default
title: "Horizon Summary: 2026-09-04 (EN)"
date: 2026-09-04
lang: en
---

> From 23 items, 14 important content pieces were selected

---

1. [OpenAI Unveils GPT-6 Astra with Major Benchmark Gains](#item-1) ⭐️ 10.0/10
2. [Verisign to Terminate Third-Level .name Domains](#item-2) ⭐️ 8.0/10
3. [Porting a 1993 Amiga Game to Godot with LLM Assistance](#item-3) ⭐️ 8.0/10
4. [Which Tools Do AI Coding Agents Prefer? 17k Runs Analyzed](#item-4) ⭐️ 8.0/10
5. [IFM AI Unveils K2 Horizon: Six Fully Open Models](#item-5) ⭐️ 8.0/10
6. [Ant Group's VLDB Best Paper: Logical Table Tames 305B Training Records](#item-6) ⭐️ 8.0/10
7. [Qwen 3.8 27B Hits 1500 Tokens/s on Cerebras, but Rate Limits and Costs Raise Concerns](#item-7) ⭐️ 7.0/10
8. [Artificial Beaver Dams Boost Coho Salmon Survival from 8% to 60%](#item-8) ⭐️ 7.0/10
9. [ICM 2026 Live: What Is Math For in the Age of AI?](#item-9) ⭐️ 7.0/10
10. [Grounding LLMs with JEPA World Models Trained in Simulation](#item-10) ⭐️ 7.0/10
11. [AAAI-27 Desk Rejection for Minor Abstract Edits Sparks Debate](#item-11) ⭐️ 7.0/10
12. [Yale Physicist on AI's Dual Role in Physics](#item-12) ⭐️ 6.0/10
13. [Mol-JEPA: Multimodal Molecular Foundation Model Introduced](#item-13) ⭐️ 6.0/10
14. [Pilot-Based Protocol Determines Reliable LLM Query Repetition Counts](#item-14) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [OpenAI Unveils GPT-6 Astra with Major Benchmark Gains](https://openai.com/index/gpt-6-astra/) ⭐️ 10.0/10

OpenAI has announced GPT-6 Astra, a new frontier model that shows significant improvements in coding and reasoning benchmarks, including the ARC-AGI-3 and the Artificial Analysis Coding Agent Index. The announcement includes a system card and has sparked extensive community discussion. GPT-6 Astra represents a major step forward in AI capabilities, potentially impacting developers and industries that rely on advanced coding and reasoning. Its release intensifies competition among AI labs and raises questions about benchmark validity and the path to AGI. The model shows notable performance gains over its predecessor, GPT-5.6 Sol, particularly on the ARC-AGI-3 benchmark, though critics point out that the scorecard may be misleading due to differing harness configurations. The system card is available at deploymentsafety.openai.com/gpt-6-astra.

hackernews · kibae · Sep 3, 18:41 · [Discussion](https://news.ycombinator.com/item?id=49554643)

**Background**: ARC-AGI-3 is an interactive reasoning benchmark that evaluates AI agents on their ability to explore novel environments and learn continuously, with humans scoring near 100% while most AI models score below 1%. The Artificial Analysis Coding Agent Index measures coding agent performance across tasks like DeepSWE and Terminal-Bench, providing a composite pass@1 score.

<details><summary>References</summary>
<ul>
<li><a href="https://arcprize.org/arc-agi/3">ARC-AGI-3</a></li>
<li><a href="https://artificialanalysis.ai/">AI Model & API Providers Analysis | Artificial Analysis</a></li>
<li><a href="https://www.datacamp.com/blog/arc-agi-3">ARC-AGI-3: The New Interactive Reasoning Benchmark - DataCamp</a></li>

</ul>
</details>

**Discussion**: Community comments highlight concerns about benchmark methodology, with one user noting that the ARC-AGI-3 scorecard may be misleading due to inconsistent harness usage. Another user draws parallels to Francois Chollet's work, suggesting that progress resembles skill acquisition rather than true intelligence. Some express excitement about improved user prompting and collaboration capabilities.

**Tags**: `#AI`, `#OpenAI`, `#GPT-6`, `#large language models`, `#benchmarks`

---

<a id="item-2"></a>
## [Verisign to Terminate Third-Level .name Domains](https://neil.fraser.name/news/2026/09/03/) ⭐️ 8.0/10

Verisign has proposed terminating all third-level .name domains (e.g., x.y.name), which would release the corresponding second-level domains (y.name). ICANN has already approved the Registry Services Evaluation Policy requests, and about 22,000 existing third-level registrations are affected. This policy change could disrupt existing websites and email addresses, and the release of second-level domains may lead to domain squatting. It also raises concerns about ICANN's mission to ensure stable and secure operation of the internet's identifier systems, as arbitrary termination contradicts stability and security. Verisign told ICANN that many of the 22,000 third-level .name registrations are unused. One registrant filed a reconsideration request, which is on track to be denied. The proposal does not mention reserving second-level domains to prevent squatting.

hackernews · pavel_lishin · Sep 3, 14:54 · [Discussion](https://news.ycombinator.com/item?id=49550772)

**Background**: In the Domain Name System (DNS), a second-level domain (SLD) is directly below a top-level domain (TLD), such as 'example' in example.com. Third-level domains are below second-level domains, like 'x' in x.y.name. Domain squatting is the practice of registering domain names with bad faith intent to profit from someone else's trademark. ICANN is the organization responsible for coordinating the internet's unique identifier systems.

<details><summary>References</summary>
<ul>
<li><a href="https://domainnamewire.com/2026/09/03/third-level-dot-name/">Discontinuation of third-level .name domains leaves some in a lurch ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Second-level_domain">Second-level domain</a></li>
<li><a href="https://en.wikipedia.org/wiki/Domain_squatting">Domain squatting</a></li>

</ul>
</details>

**Discussion**: Community comments express concern over the termination, with some suggesting that Verisign should stop new registrations but honor existing ones and reserve second-level domains to avoid squatting. Others note that .name itself is not being terminated, only third-level domains, and some question the decision-making process, citing ICANN's mission of stability and security.

**Tags**: `#domain names`, `#ICANN`, `#internet governance`, `#policy`, `#Verisign`

---

<a id="item-3"></a>
## [Porting a 1993 Amiga Game to Godot with LLM Assistance](https://babyloniantwins.com/blog/porting-a-1993-amiga-game-to-godot/) ⭐️ 8.0/10

A developer successfully ported his 1993 Amiga game, originally written in MC68000 assembly, to the Godot engine using an LLM (Claude) in a single evening. The LLM assembled the code with vasm until the binary was byte-identical to the original, and the game is now released for free. This demonstrates a novel and efficient workflow for preserving and modernizing legacy games, potentially inspiring other developers to revive classic titles. It also showcases the growing capability of LLMs in understanding and translating low-level assembly code, which could impact retro computing and AI-assisted software engineering. The original game was assembled using AsmOne, which assembles into memory, so the shipped files were snapshots of a running game, causing a 108-byte mismatch that the developer never verified. The porting process involved feeding the LLM the developer's 33 years of memory, notes, and git repos, and the LLM wrote the first draft of the article, which the developer edited line by line.

hackernews · rabahs · Sep 3, 14:28 · [Discussion](https://news.ycombinator.com/item?id=49550375)

**Background**: The Amiga was a popular home computer in the late 1980s and early 1990s, and many games were written in MC68000 assembly for performance. Godot is a modern open-source game engine that supports 2D and 3D game development. AsmOne is an integrated macro assembler for the Amiga, and vasm is a portable assembler that can target the 68000. LLMs like Claude are increasingly used for code translation and generation tasks.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/nguillaumin/perihelion-m68k-tutorials">The Atari ST MC68000 Assembly Language Tutorials - GitHub</a></li>
<li><a href="https://en.wikipedia.org/wiki/Godot_(game_engine)">Godot (game engine)</a></li>
<li><a href="https://handwiki.org/wiki/ASM-One_Macro_Assembler">ASM-One Macro Assembler - HandWiki</a></li>

</ul>
</details>

**Discussion**: The community expressed awe at the developer's original 1993 assembly work and enthusiasm for the AI-assisted porting approach. Several commenters shared their own experiences using LLMs to port retro games, such as converting ZX81 games to Go or NES games to modern frameworks, highlighting a growing trend. Some also noted the nostalgic value and asked about debugging stories from the original development.

**Tags**: `#LLM`, `#retro-gaming`, `#porting`, `#Godot`, `#assembly`

---

<a id="item-4"></a>
## [Which Tools Do AI Coding Agents Prefer? 17k Runs Analyzed](https://armature.tech/blog/which-tools-coding-agents-install) ⭐️ 8.0/10

Armature analyzed 17,000 runs of coding agents like Claude, Codex, and Cursor to determine which tools they install most frequently, publishing the findings in a blog post. This empirical data offers developers and tool vendors actionable insights into agent-driven adoption, helping them optimize their products for AI agent compatibility and discoverability. The analysis covers multiple coding agents and likely includes details on installation frequency, tool categories, and potential differences between agents. The article is based on a substantial dataset of 17,000 runs, providing a statistically meaningful sample.

hackernews · screm · Sep 3, 21:20 · [Discussion](https://news.ycombinator.com/item?id=49557206)

**Background**: AI coding agents such as Claude Code, Codex, and Cursor are increasingly used by developers to automate coding tasks. These agents often install additional tools or packages to complete tasks, and understanding their preferences is crucial for tool developers aiming to be adopted by agents.

<details><summary>References</summary>
<ul>
<li><a href="https://scrimba.com/articles/claude-code-vs-codex-vs-cursor/">Claude Code vs Codex vs Cursor: Best AI Agent 2026</a></li>
<li><a href="https://blog.jetbrains.com/research/2026/08/ai-coding-agent-adoption-2026/">AI Coding Agents: Adoption Trends - The JetBrains Blog</a></li>

</ul>
</details>

**Discussion**: Commenters shared mixed reactions: some praised the analysis as insightful, while others noted similar tracking efforts or raised specific questions about agent behavior, such as Claude Code's use of awk/sed/Python for file editing. One commenter expressed concern about the future of AI tools becoming profit-driven.

**Tags**: `#AI coding agents`, `#developer tools`, `#empirical analysis`, `#tool adoption`

---

<a id="item-5"></a>
## [IFM AI Unveils K2 Horizon: Six Fully Open Models](https://ifm.ai/blog/k2/) ⭐️ 8.0/10

IFM AI has announced K2 Horizon, a suite of six fully open-source AI models covering a range of sizes from edge to enterprise, with competitive coding performance. The release includes weights, training code, data, and benchmarks, positioning it as a radically open alternative in the AI landscape. This release is significant for the open-source AI community as it provides a fully transparent stack, addressing concerns about closed models and enabling broader access to powerful coding capabilities. It could accelerate local LLM coding on consumer hardware, such as 8GB VRAM devices, and foster further innovation in open AI development. The K2 Horizon suite includes models like the 7B model, which reportedly scores 70.6 on SWE-bench-verified, comparable to Qwen3.6-35b-a3b's 70.0. However, community analysis notes that the dense 32B model lags behind Qwen3.8 27B, and the models are hosted on Hugging Face under the IFM organization.

hackernews · karimf · Sep 3, 15:36 · [Discussion](https://news.ycombinator.com/item?id=49551760)

**Background**: Open-source AI models are those whose weights, training data, and code are publicly available, allowing researchers and developers to inspect, modify, and deploy them freely. This contrasts with closed models, which are proprietary and opaque. The K2 Horizon release is part of a trend toward more transparent AI, similar to Nvidia's Nemotron, and aims to democratize access to advanced AI capabilities.

<details><summary>References</summary>
<ul>
<li><a href="https://ifm.ai/blog/k2">Introducing K2 Horizon: Frontier Performance, Radically Open</a></li>
<li><a href="https://ifm.ai/k2/">K2 Horizon: Open-Source AI Models for Every Scale | IFM</a></li>
<li><a href="https://huggingface.co/IFM/K2-Horizon-32B">IFM/K2-Horizon-32B · Hugging Face</a></li>

</ul>
</details>

**Discussion**: Community sentiment is largely positive, with excitement about the potential for local LLM coding on 8GB VRAM devices and appreciation for the fully open stack. However, some users express skepticism about benchmark claims, noting that the 32B model underperforms competitors, and others mention 'model fatigue' due to the rapid pace of releases.

**Tags**: `#open-source AI`, `#LLM`, `#coding benchmarks`, `#model release`, `#AI research`

---

<a id="item-6"></a>
## [Ant Group's VLDB Best Paper: Logical Table Tames 305B Training Records](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&mid=2247918381&idx=4&sn=dfbbddb50c561e09f85e05c20c65bfb1) ⭐️ 8.0/10

Ant Group's paper won the VLDB Best Paper award for introducing a logical table method that efficiently manages 305 billion training data records, achieving a 5.6x speedup in data preparation. This innovation addresses a critical bottleneck in large-scale AI training by drastically reducing data preparation time, potentially accelerating model development cycles across the industry. It also highlights the growing importance of data engineering in AI research. The method uses a logical table abstraction to handle 35PB of corpus data, enabling efficient processing without physical data duplication. The 5.6x speedup was demonstrated in real-world training pipelines, showcasing practical scalability.

rss · 量子位 · Sep 3, 09:30

**Background**: Training large AI models requires massive datasets, often exceeding hundreds of billions of records. Traditional data preparation methods involve extensive physical transformations, which are time-consuming and resource-intensive. Logical tables provide a virtual layer that simplifies data management and accelerates preprocessing.

<details><summary>References</summary>
<ul>
<li><a href="https://vldb.org/2023/?conference-awards=">VLDB 2023 - Conference Awards</a></li>

</ul>
</details>

**Tags**: `#VLDB`, `#data engineering`, `#large-scale AI`, `#training data`, `#Ant Group`

---

<a id="item-7"></a>
## [Qwen 3.8 27B Hits 1500 Tokens/s on Cerebras, but Rate Limits and Costs Raise Concerns](https://inference-docs.cerebras.ai/models/overview) ⭐️ 7.0/10

Qwen 3.8 27B is now available on Cerebras inference, delivering up to 1500 tokens per second. However, users report restrictive rate limits and high costs that may limit its practical use. This marks a significant performance milestone for open-weight models, potentially enabling real-time applications. Yet, the practical constraints highlighted by users could hinder widespread adoption, especially for coding and agentic tasks. The public endpoint has a token-per-minute (TPM) limit of 150,000, and cached tokens count toward this limit. One user hit the limit in about 90 seconds, spending $1.10, while a comparable task with DeepSeek-V4-Flash cost only $0.024.

hackernews · altertable · Sep 3, 18:32 · [Discussion](https://news.ycombinator.com/item?id=49554520)

**Background**: Cerebras provides cloud-based AI inference using wafer-scale engines, claiming speeds up to 15x faster than NVIDIA GPUs. Qwen 3.8 27B is a compact, deployment-friendly dense vision-language model built on the Qwen 3.5 architecture, designed for coding, professional work, and agentic tasks.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cerebras.ai/inference">Inference - Cerebras</a></li>
<li><a href="https://huggingface.co/Qwen/Qwen3.8-27B">Qwen / Qwen 3 . 8 - 27 B · Hugging Face</a></li>
<li><a href="https://lmstudio.ai/models/qwen/qwen3.8-27b">qwen / qwen 3 . 8 - 27 b • LM Studio</a></li>

</ul>
</details>

**Discussion**: Community sentiment is mixed: while some praise the raw speed, many criticize the restrictive rate limits and high costs, calling them impractical for real-world use. Some users suggest alternatives like local inference with tools such as ninfer, or hope for availability via OpenRouter to improve accessibility.

**Tags**: `#AI inference`, `#Qwen`, `#Cerebras`, `#LLM deployment`, `#performance`

---

<a id="item-8"></a>
## [Artificial Beaver Dams Boost Coho Salmon Survival from 8% to 60%](https://www.discoverwildlife.com/animal-facts/artificial-beaver-dams-california) ⭐️ 7.0/10

In California, the installation of artificial beaver dams has dramatically increased juvenile coho salmon survival rates from 8% to 60%. This conservation technique mimics natural beaver activity to restore degraded river habitats. This significant improvement offers a promising, cost-effective tool for salmon conservation, especially in regions where beaver populations have declined. It could help reverse the decline of endangered salmon runs and restore freshwater ecosystems. The artificial dams are constructed from natural materials and are designed to mimic the hydrologic effects of real beaver dams, such as slowing water flow and creating deeper pools. Interestingly, water temperatures decreased after damming, likely due to increased groundwater exchange, which is beneficial for salmon.

hackernews · speckx · Sep 3, 16:21 · [Discussion](https://news.ycombinator.com/item?id=49552572)

**Background**: Coho salmon (Oncorhynchus kisutch) are anadromous fish that spawn in freshwater streams and migrate to the ocean. Juvenile coho require cool, slow-moving water with deep pools to survive their first year. Historically, beaver dams created such habitats, but over-trapping and habitat loss reduced beaver populations, contributing to salmon declines. Artificial beaver dams aim to restore these critical habitats without reintroducing beavers.

**Discussion**: Commenters expressed cautious optimism, noting the positive news amid environmental pessimism. Some shared personal anecdotes about similar restoration efforts, while others highlighted the counterintuitive finding of decreased water temperatures and the historical importance of beavers in North America.

**Tags**: `#ecology`, `#conservation`, `#wildlife`, `#restoration`, `#salmon`

---

<a id="item-9"></a>
## [ICM 2026 Live: What Is Math For in the Age of AI?](https://www.quantamagazine.org/live-from-icm-2026-what-is-math-for-in-the-age-of-ai-20260903/) ⭐️ 7.0/10

A special live recording from the International Congress of Mathematicians (ICM) in Philadelphia, July 2026, featured a discussion on what mathematicians value about their field in the age of AI. The session was published by Quanta Magazine on September 3, 2026. This discussion addresses a timely and significant question as AI tools increasingly impact mathematical research. It highlights the evolving role of human mathematicians and the philosophical implications for the field, affecting researchers, educators, and the broader scientific community. The recording took place at ICM 2026, held in Philadelphia from July 23-30, 2026. The discussion featured notable authors and focused on the intrinsic values of mathematics, rather than technical AI applications.

rss · Quanta Magazine · Sep 3, 13:41

**Background**: The International Congress of Mathematicians (ICM) is held every four years and is one of the most prestigious conferences in mathematics. As AI capabilities advance, mathematicians are grappling with questions about the nature of their work, as highlighted by Terence Tao's essay 'Mathematics in the Age of AI', which discusses a 'crisis of values and practices'.

<details><summary>References</summary>
<ul>
<li><a href="https://www.mathunion.org/icm/icm-2026">ICM 2026 - International Congress of Mathematicians in ...</a></li>
<li><a href="https://www.icm2026.org/event/ac193975-5d24-4628-8c30-ddb23de19a8b/home">HOME - International Congress of Mathematicians (ICM) 2026</a></li>
<li><a href="https://terrytao.wordpress.com/2026/03/29/mathematical-methods-and-human-thought-in-the-age-of-ai/">Mathematical methods and human thought in the age of AI | What's new</a></li>

</ul>
</details>

**Tags**: `#mathematics`, `#AI`, `#ICM 2026`, `#philosophy of math`

---

<a id="item-10"></a>
## [Grounding LLMs with JEPA World Models Trained in Simulation](https://www.reddit.com/r/MachineLearning/comments/1w69gvd/grounding_llms_with_jepabased_world_models/) ⭐️ 7.0/10

A Reddit user proposes training a JEPA-style world model inside a physics simulator like MuJoCo to predict future state representations, then attaching these grounded representations to an LLM as a conditioning signal. This combination aims to give LLMs genuine physical intuition rather than mere statistical correlations. This proposal addresses a fundamental limitation of LLMs—their lack of grounded understanding of physical reality—which is often compared to the 'Mary's Room' thought experiment. If successful, it could significantly improve LLM reasoning about physical tasks and enable more efficient downstream learning, potentially impacting robotics, embodied AI, and scientific reasoning. The author notes that V-JEPA predicts future frame representations for video, and DreamerV3 uses a latent world model for reinforcement learning, but the specific combination of JEPA-style prediction, simulation-grounded physics representations, and LLM attachment appears novel. Key open questions include the interface between JEPA representations and the LLM (e.g., concatenation vs. cross-attention) and whether the sim-to-real gap would hinder transfer.

reddit · r/MachineLearning · /u/Full_Promotion4522 · Sep 3, 14:45

**Background**: JEPA (Joint Embedding Predictive Architecture) is a self-supervised learning approach that predicts abstract representations of future states rather than reconstructing raw inputs. World models like V-JEPA 2 aim to capture physical understanding and enable planning. MuJoCo is a widely used physics engine for simulating articulated systems. The 'Mary's Room' thought experiment illustrates the difference between propositional knowledge and experiential understanding, which parallels the gap between LLM's linguistic knowledge and grounded physical intuition.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/World_model_(artificial_intelligence)">World model (artificial intelligence) - Wikipedia</a></li>
<li><a href="https://ai.meta.com/blog/v-jepa-2-world-model-benchmarks/">Introducing the V-JEPA 2 world model and new benchmarks for ...</a></li>
<li><a href="https://mujoco.org/">MuJoCo — Advanced Physics Simulation</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#JEPA`, `#world models`, `#grounding`, `#AI research`

---

<a id="item-11"></a>
## [AAAI-27 Desk Rejection for Minor Abstract Edits Sparks Debate](https://www.reddit.com/r/MachineLearning/comments/1w6kcp6/aaai27_desk_rejection_over_incredibly_minor/) ⭐️ 7.0/10

A researcher reported receiving a desk rejection from AAAI-27 for making minor modifications to the title or abstract between the abstract-registration and full-paper deadlines, despite the official guidelines allowing such edits. The rejection notice stated the decision was final and appeals would not be considered. This incident raises concerns about the consistent and fair enforcement of submission guidelines at a major AI conference, potentially affecting many researchers who may unknowingly violate ambiguous rules. It highlights the need for clearer communication and consistent application of policies to avoid unjust rejections. The AAAI-27 modification guidelines state that title and abstract can be edited after abstract registration, but warn against substantive changes that describe qualitatively different research. The researcher claims their changes were incredibly minor and almost everything else was identical, yet the rejection was final with no appeal option.

reddit · r/MachineLearning · /u/Dansilly · Sep 3, 21:12

**Background**: AAAI (Association for the Advancement of Artificial Intelligence) is a major conference for AI research. For AAAI-27, authors must register an abstract by an early deadline and then submit the full paper by a later deadline. The modification guidelines aim to prevent authors from drastically changing their research after the abstract deadline, but allow minor edits to title and abstract. Desk rejections are typically issued for clear violations of submission policies, such as formatting errors or substantive changes.

<details><summary>References</summary>
<ul>
<li><a href="https://aaai.org/conference/aaai/aaai-27/main-technical-track-call/">AAAI - 27 Main Technical Track Call - AAAI</a></li>
<li><a href="https://aaai.org/aaai-publications/aaai-publication-policies-guidelines/">AAAI Publication Policies & Guidelines</a></li>
<li><a href="https://aaai-23.aaai.org/modification-guidelines/">Paper Modification Guidelines | AAAI 2023 Conference</a></li>

</ul>
</details>

**Discussion**: The Reddit discussion likely includes comments from other researchers sharing similar experiences or offering interpretations of the policy, with some expressing frustration over the lack of appeal and perceived unfairness. Others may suggest that the rejection might be due to automated checks or a strict interpretation of the rules.

**Tags**: `#AAAI`, `#conference`, `#research`, `#submission`, `#policy`

---

<a id="item-12"></a>
## [Yale Physicist on AI's Dual Role in Physics](https://www.quantamagazine.org/in-an-age-of-ai-a-physicist-seeks-what-endures-20260903/) ⭐️ 6.0/10

Sarah Demers, chair of Yale's physics department, shared her perspective on how large language models could both aid and undermine physics research. The article was published on Quanta Magazine. This commentary highlights the growing tension between AI's potential to accelerate scientific discovery and its risks to scientific integrity and human understanding. It is significant for physicists and AI researchers as they navigate the integration of LLMs into research workflows. The article features Sarah Demers, chair of the physics department at Yale University, reflecting on the dual nature of large language models in physics. It does not provide specific technical details but focuses on ethical and epistemological considerations.

rss · Quanta Magazine · Sep 3, 13:35

**Background**: Large language models (LLMs) are AI systems trained on vast text data to generate human-like text. In scientific fields like physics, they are being explored for tasks such as literature review, hypothesis generation, and data analysis. However, concerns include potential biases, hallucinated outputs, and over-reliance that could undermine critical thinking and reproducibility.

**Tags**: `#AI`, `#physics`, `#LLM`, `#science`, `#ethics`

---

<a id="item-13"></a>
## [Mol-JEPA: Multimodal Molecular Foundation Model Introduced](https://www.reddit.com/r/MachineLearning/comments/1w6i8pr/moljepa_multimodal_molecular_foundation_model_r/) ⭐️ 6.0/10

A researcher announced the release of Mol-JEPA, a multimodal molecular foundation model, along with a summary website and a paper. The model is trained on 5 million molecules and uses a joint embedding predictive architecture to predict missing modalities from available ones. Mol-JEPA introduces a novel approach to molecular machine learning by leveraging multimodal data and latent space prediction, which could improve performance across various biochemical benchmarks. This may accelerate drug discovery and materials science research by enabling more robust molecular representations. The model is based on a joint embedding predictive architecture (JEPA) and is trained on 5 million molecules spanning various modalities. The code is available on GitHub under Boehringer-Ingelheim/mol-jepa, and the paper is available on arXiv (2608.22642).

reddit · r/MachineLearning · /u/TerribleAntelope9348 · Sep 3, 19:56

**Background**: Molecular foundation models are pre-trained on large datasets of molecules to learn representations useful for downstream tasks like property prediction and drug design. JEPA (Joint Embedding Predictive Architecture) is a self-supervised learning approach that predicts missing parts of the input in latent space, rather than in the original data space, which can improve robustness and efficiency. Mol-JEPA extends this concept to multiple molecular modalities, such as structure, text, and biochemical properties, aiming to capture richer context.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2608.22642">Mol-JEPA: A multimodal Joint Embedding Predictive ...</a></li>
<li><a href="https://huggingface.co/Flogrammer/Mol-JEPA">Flogrammer/ Mol - JEPA · Hugging Face</a></li>
<li><a href="https://github.com/Boehringer-Ingelheim/mol-jepa">GitHub - Boehringer-Ingelheim/mol-jepa: Mol-JEPA multimodal ...</a></li>

</ul>
</details>

**Discussion**: No community comments were provided in the news item, so the overall sentiment is unknown.

**Tags**: `#molecular machine learning`, `#JEPA`, `#foundation model`, `#multimodal learning`, `#research paper`

---

<a id="item-14"></a>
## [Pilot-Based Protocol Determines Reliable LLM Query Repetition Counts](https://www.reddit.com/r/MachineLearning/comments/1w6wtw7/how_many_repeated_llm_queries_are_enough_testing/) ⭐️ 6.0/10

A new preprint proposes a pilot-based reliability protocol using generalizability theory to estimate the number of repeated LLM queries needed for reliable comparisons, validated on three external corpora. The method predicted reliability accurately in 37 of 39 test cells, with two partial matches. This work addresses a practical challenge in LLM evaluation: determining how many times to repeat prompts for stable results. It offers a statistically grounded alternative to fixed iteration thresholds, which the study found do not transfer across contexts, potentially improving the reliability of LLM benchmarking and downstream applications. The protocol uses generalizability theory to estimate variance components from a pilot study, then calculates the repeat count needed for a chosen reliability target. The external validation covered political-orientation questionnaires and benchmark stability, but not brand recommendations, which remains an outstanding limitation. The preprint is available at arXiv:2609.04047, with validation materials on GitHub.

reddit · r/MachineLearning · /u/dizhat · Sep 4, 06:53

**Background**: Generalizability theory (G theory) is a statistical framework for assessing the reliability of measurements under specific conditions, introduced by Cronbach and colleagues in 1963. In LLM evaluation, repeated queries are often used to account for model stochasticity, but choosing the number of repetitions is typically ad hoc. This paper applies G theory to formalize that choice, aiming to improve the rigor of LLM reliability assessments.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Generalizability_theory">Generalizability theory</a></li>
<li><a href="https://grokipedia.com/page/Generalizability_theory">Generalizability theory</a></li>
<li><a href="https://web.archive.org/web/20010627112737/http://www.psychology.sdsu.edu/faculty/matt/Pubs/GThtml/GTheory_GEMatt.html">Generalizability Theory</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#reliability`, `#generalizability theory`, `#evaluation`, `#preprint`

---
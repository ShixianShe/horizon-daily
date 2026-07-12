---
layout: default
title: "Horizon Summary: 2026-07-12 (EN)"
date: 2026-07-12
lang: en
---

> From 14 items, 9 important content pieces were selected

---

1. [vLLM v0.25.0: Model Runner V2 Default, PagedAttention Removed](#item-1) ⭐️ 9.0/10
2. [RISCBoy: Open-Source Handheld Console Built on RISC-V](#item-2) ⭐️ 8.0/10
3. [Deep Dive into UPI Payment Architecture](#item-3) ⭐️ 8.0/10
4. [ClickHouse scales PgBouncer to 4x throughput with peering](#item-4) ⭐️ 8.0/10
5. [VultronRetriever Models Top MTEB Leaderboard](#item-5) ⭐️ 8.0/10
6. [Mesh LLM: Distributed AI Computing on iroh](#item-6) ⭐️ 7.0/10
7. [Nvidia's GPU Investments: Circular Financing or Strategic Hedge?](#item-7) ⭐️ 7.0/10
8. [Ant: A New JavaScript Runtime and Ecosystem](#item-8) ⭐️ 6.0/10
9. [User seeks alternatives to HPSv3 for human preference prediction](#item-9) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [vLLM v0.25.0: Model Runner V2 Default, PagedAttention Removed](https://github.com/vllm-project/vllm/releases/tag/v0.25.0) ⭐️ 9.0/10

vLLM v0.25.0 makes Model Runner V2 the default execution path for all dense models, removes the legacy PagedAttention implementation, and introduces new models like LLaVA-OneVision-2 and GLM-5. The release also includes a new Streaming Parser Engine and universal speculative decoding for heterogeneous vocabularies. This release marks a major architectural shift in vLLM, improving performance and maintainability by standardizing on Model Runner V2. The removal of PagedAttention and the addition of new models and features make vLLM more efficient and versatile for LLM inference and serving. Model Runner V2 now supports EVS, realtime embeddings, prefix caching for Mamba hybrid models, and dynamic speculative decoding with full CUDA graphs. The Transformers modeling backend has become as fast as native vLLM, and the release includes 558 commits from 232 contributors.

github · khluu · Jul 11, 20:06

**Background**: vLLM is an open-source library for fast LLM inference and serving, known for its PagedAttention mechanism that efficiently manages key-value cache memory. Model Runner V2 is a redesigned execution core that addresses architectural issues from the original V1 design, offering modular model logic and better performance. The removal of PagedAttention indicates that vLLM has fully transitioned to newer attention backends.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.vllm.ai/en/latest/design/model_runner_v2/">Model Runner V2 Design Document - vLLM</a></li>
<li><a href="https://vllm.ai/blog/2026-03-24-mrv2">Model Runner V2: A Modular and Faster Core for vLLM</a></li>
<li><a href="https://docs.vllm.ai/en/latest/design/paged_attention/">Paged Attention - vLLM</a></li>

</ul>
</details>

**Tags**: `#vLLM`, `#LLM inference`, `#open source`, `#machine learning`, `#release`

---

<a id="item-2"></a>
## [RISCBoy: Open-Source Handheld Console Built on RISC-V](https://github.com/Wren6991/RISCBoy) ⭐️ 8.0/10

RISCBoy is an open-source portable game console designed from scratch using a RISC-V processor, inspired by the Gameboy Advance. The project is hosted on GitHub and has garnered significant community attention. This project demonstrates the viability of RISC-V in consumer electronics, potentially reducing reliance on proprietary architectures like ARM. It also provides a fully open-source hardware platform for retro gaming enthusiasts and embedded systems education. The console is designed by Luke Wren, an ASIC design engineer at Raspberry Pi, and features an open-source AHB/APB bus implementation. It is a fully custom design, not based on existing commercial hardware.

hackernews · mariuz · Jul 11, 21:58 · [Discussion](https://news.ycombinator.com/item?id=48876245)

**Background**: RISC-V is a free and open instruction set architecture (ISA) that allows anyone to design processors without paying royalties. Unlike proprietary ISAs like ARM, RISC-V fosters open collaboration and innovation. Open-source game consoles like RISCBoy highlight the potential of RISC-V in embedded and hobbyist projects.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/RISC-V_architecture">RISC-V architecture</a></li>

</ul>
</details>

**Discussion**: Commenters praised the project, noting the creator's expertise (he also designed DVI/HDMI from RP2040). Some expressed surprise that open-source AHB/APB implementations are permissible, as they assumed those were ARM proprietary.

**Tags**: `#open-source hardware`, `#RISC-V`, `#gaming console`, `#embedded systems`

---

<a id="item-3"></a>
## [Deep Dive into UPI Payment Architecture](https://timeseriesofindia.com/economy/reads/upi-architecture/) ⭐️ 8.0/10

A detailed technical article explains the architecture and transaction flow of India's Unified Payments Interface (UPI), covering its design, scalability, and the role of NPCI as the central switch. UPI has revolutionized digital payments in India, enabling over 18 billion monthly transactions. Understanding its architecture is crucial for developers, fintech professionals, and anyone interested in scalable payment systems. The article includes a QPS (queries per second) analysis, noting that 22 billion annual transactions average ~700 QPS for the NPCI switch, with peaks much higher. It also features a crore/billion toggle for readability.

hackernews · prtk25 · Jul 11, 16:33 · [Discussion](https://news.ycombinator.com/item?id=48873457)

**Background**: UPI (Unified Payments Interface) is a real-time payment system developed by the National Payments Corporation of India (NPCI). It facilitates inter-bank transactions through a mobile platform, allowing users to send and receive money instantly using a virtual payment address (VPA). The system uses a four-party model involving the payer's bank, payee's bank, PSPs, and NPCI as the central switch.

<details><summary>References</summary>
<ul>
<li><a href="https://razorpay.com/blog/what-is-upi-and-how-it-works/">What is UPI?: Unified Payments Interface Meaning, Features ...</a></li>
<li><a href="https://www.linkedin.com/pulse/understanding-upi-process-flow-seamless-payment-sanjukta-chakraborty-ih4dc">Understanding the UPI Process Flow: A Seamless Payment Journey</a></li>
<li><a href="https://medium.com/@ayush_mittal/upi-payments-workflow-d0dcc65890f2">UPI Payments Workflow. Introduction: The Unified ... - Medium How Does UPI Work? - GeeksforGeeks How UPI Works Internally (Backend + NPCI Explained) - Oflox Inside UPI : The Technology, Security, and Workflow ... - Medium Designing UPI - System Design - GeeksforGeeks</a></li>

</ul>
</details>

**Discussion**: Comments highlight privacy concerns (phone number linked to identity, government control) but praise UPI's success in driving digital adoption among elderly users. The article's design, especially the crore/billion toggle, is well-received. A comparison notes that UPI's average QPS (~700) is lower than Nasdaq's peak (100k+), but traffic is uneven.

**Tags**: `#UPI`, `#payment systems`, `#architecture`, `#India`, `#scalability`

---

<a id="item-4"></a>
## [ClickHouse scales PgBouncer to 4x throughput with peering](https://clickhouse.com/blog/pgbouncer-clickhouse-managed-postgres) ⭐️ 8.0/10

ClickHouse published a blog post detailing how they scaled PgBouncer to 4x throughput by implementing peering between processes to handle query cancellation correctly. This improvement allows PgBouncer, a widely-used PostgreSQL connection pooler, to handle higher loads without sacrificing query cancellation functionality, benefiting many production deployments. The peering feature, introduced in PgBouncer 1.19.0, enables multiple PgBouncer processes to forward cancellation requests to the correct process that owns the session, solving a long-standing issue where cancellations could be lost.

hackernews · saisrirampur · Jul 11, 15:28 · [Discussion](https://news.ycombinator.com/item?id=48872874)

**Background**: PgBouncer is a lightweight connection pooler for PostgreSQL that manages database connections to reduce overhead. When running multiple PgBouncer processes for scalability, query cancellation requests could land on the wrong process and be ignored. Peering solves this by allowing processes to forward cancellations to the correct peer.

<details><summary>References</summary>
<ul>
<li><a href="https://www.pgbouncer.org/config.html">PgBouncer config</a></li>
<li><a href="https://dataegret.com/2024/08/handling_cancellation_request/">Handling Cancellation Request - Data Egret</a></li>
<li><a href="https://postgrespro.com/docs/postgrespro/11/pgbouncer">Postgres Pro Standard : Documentation: 11: pgbouncer : Postgres Professional</a></li>

</ul>
</details>

**Discussion**: Community members suggested alternative solutions like Odyssey and pgdog, and shared practical deployment experiences on Kubernetes. Overall sentiment was positive, with users appreciating the technical depth and real-world applicability.

**Tags**: `#PostgreSQL`, `#PgBouncer`, `#connection pooling`, `#scalability`, `#ClickHouse`

---

<a id="item-5"></a>
## [VultronRetriever Models Top MTEB Leaderboard](https://www.reddit.com/r/MachineLearning/comments/1utmxq8/vultronretriever_family_of_models_released_on/) ⭐️ 8.0/10

VultronRetriever family of embedding models has been released on HuggingFace, achieving top rankings on the MTEB leaderboard with state-of-the-art efficiency, including a 16x smaller index and 12x higher throughput, and demonstrated fully offline Q&A and document embedding on an iPhone. This breakthrough enables high-precision retrieval and generation on edge devices without internet connectivity, significantly reducing storage and computational costs, which could accelerate adoption of AI in privacy-sensitive and offline applications. The family includes three models: VultronRetrieverPrime-8B (global #1), Core-4.5B (second only to Prime), and Flash-0.8B (outperforms models 5x its size). They use the Hydra Architecture for late interaction retrieval and were trained on datasets with 0% cross-dataset duplication and 0% eval contamination.

reddit · r/MachineLearning · /u/madkimchi · Jul 11, 15:22

**Background**: Embedding models convert text into numerical vectors for semantic search and retrieval. The MTEB leaderboard benchmarks embedding models across various tasks. Late interaction retrieval, as used in ColBERT, processes queries and documents separately until final scoring, balancing efficiency and precision.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/spaces/mteb/leaderboard">MTEB Leaderboard - a Hugging Face Space by mteb</a></li>
<li><a href="https://weaviate.io/blog/late-interaction-overview">An Overview of Late Interaction Retrieval Models... | Weaviate</a></li>
<li><a href="https://jina.ai/news/what-is-colbert-and-late-interaction-and-why-they-matter-in-search/">What is ColBERT and Late Interaction and Why They Matter in Search?</a></li>

</ul>
</details>

**Tags**: `#retrieval`, `#embedding`, `#edge AI`, `#MTEB`, `#NLP`

---

<a id="item-6"></a>
## [Mesh LLM: Distributed AI Computing on iroh](https://www.iroh.computer/blog/mesh-llm) ⭐️ 7.0/10

Mesh LLM is a new platform that pools GPU resources across multiple machines into a single OpenAI-compatible API endpoint, built on the iroh peer-to-peer networking library. This approach enables cost-effective, private, and scalable AI inference without relying on centralized cloud providers, potentially democratizing access to large language models. Each node runs an iroh endpoint identified by a public key, handling NAT traversal and authenticated QUIC connections without a central server. However, the project currently lacks published performance benchmarks, raising questions about inference speed over consumer networks.

hackernews · tionis · Jul 11, 22:38 · [Discussion](https://news.ycombinator.com/item?id=48876505)

**Background**: Distributed AI computing splits model inference across multiple devices to handle large models that exceed a single device's memory. iroh is a peer-to-peer networking library that provides secure, direct connections between devices without central servers. Mesh LLM leverages iroh to create a mesh of heterogeneous devices (laptops, servers, cloud nodes) for running large language models collaboratively.

<details><summary>References</summary>
<ul>
<li><a href="https://www.iroh.computer/blog/mesh-llm">Mesh LLM: distributed AI computing on iroh</a></li>
<li><a href="https://github.com/Mesh-LLM/mesh-llm">GitHub - Mesh-LLM/mesh-llm: Distributed AI/LLM for the people ...</a></li>
<li><a href="https://daily.dev/posts/mesh-llm-distributed-ai-computing-on-iroh-ymmyrv7xv">Mesh LLM: distributed AI computing on iroh - daily.dev</a></li>

</ul>
</details>

**Discussion**: Community comments express interest in the concept but also skepticism about performance, with one user noting the lack of benchmarks and estimating that consumer networks may be much slower than local RAM. A contributor mentioned that the Qwen 235B/22B MoE model achieved 16 tok/s across 2 nodes, but overall sentiment calls for more transparency on speed.

**Tags**: `#distributed computing`, `#LLM`, `#inference`, `#iroh`, `#AI infrastructure`

---

<a id="item-7"></a>
## [Nvidia's GPU Investments: Circular Financing or Strategic Hedge?](https://io-fund.com/ai-stocks/nvidia-coreweave-nebius-circular-financing-gpu-boom) ⭐️ 7.0/10

An analysis reveals that Nvidia's investments in CoreWeave and Nebius may represent circular financing, where Nvidia provides capital to cloud companies that then spend heavily on Nvidia GPUs, potentially inflating demand. However, community comments argue that Nvidia's $2 billion stake in CoreWeave is only a small fraction of CoreWeave's $35 billion 2026 CapEx, suggesting the circularity concern is overstated. This debate is critical because if circular financing is widespread, it could mask true AI infrastructure demand and create a bubble. The outcome affects investors, hyperscalers, and the entire GPU supply chain, as Nvidia's strategy may be a hedge against hyperscalers developing their own chips. Nvidia invested $2 billion for a 9% equity stake in CoreWeave, while CoreWeave plans $35 billion in CapEx in 2026. Nvidia also invested in Nebius, another GPU cloud provider. Community members highlight that profitability metrics like ROI per token and enterprise token budgets are more important than circular financing concerns.

hackernews · adletbalzhanov · Jul 11, 17:21 · [Discussion](https://news.ycombinator.com/item?id=48873836)

**Background**: CoreWeave is an AI cloud company specializing in GPU infrastructure, originally founded as Atlantic Crypto in 2017. Nebius Group is a technology company providing AI infrastructure, headquartered in Amsterdam. Circular financing refers to a situation where a supplier invests in its customers, who then use that capital to buy the supplier's products, potentially creating artificial demand. Nvidia's investments in these neoclouds are seen as a hedge against hyperscalers like AWS, Google, and Microsoft, which are designing their own AI chips.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/CoreWeave">CoreWeave</a></li>
<li><a href="https://en.wikipedia.org/wiki/Nebius_Group">Nebius Group - Wikipedia</a></li>
<li><a href="https://www.linkedin.com/pulse/nvidia-coreweave-nebius-inside-circular-financing-gpu-beth-kindig-nponc">Nvidia, CoreWeave, and Nebius: Inside the Circular Financing of the...</a></li>

</ul>
</details>

**Discussion**: Community comments are mixed: some argue the circular financing concern is overblown given the small relative size of Nvidia's investment, while others focus on the real question of whether these GPU builds will be profitable. One commenter notes that Nvidia's investments are a hedge against hyperscalers, and another points to metrics like ROI per token as more important than circularity.

**Tags**: `#GPU`, `#Nvidia`, `#cloud computing`, `#AI infrastructure`, `#finance`

---

<a id="item-8"></a>
## [Ant: A New JavaScript Runtime and Ecosystem](https://antjs.org/) ⭐️ 6.0/10

Ant is a new JavaScript runtime with its own engine, package manager, registry (ants.land), deployment platform, and desktop app framework (Ant Desktop), aiming to provide a coherent end-to-end alternative to existing JavaScript stacks. If successful, Ant could challenge dominant runtimes like Node.js and Deno by offering a tightly integrated ecosystem, potentially improving developer experience and performance. It also represents a growing trend of individual developers building complex infrastructure that previously required large teams. Ant claims to be lightweight, have fast startup, sandboxing, and competitive performance, though it is still early-stage. The runtime's codebase was originally based on the AGPL-licensed Elk engine, but the author says it has since been rewritten.

hackernews · theMackabu · Jul 11, 20:07 · [Discussion](https://news.ycombinator.com/item?id=48875377)

**Background**: JavaScript runtimes like Node.js and Deno execute JavaScript outside the browser. Ant introduces its own engine and a full ecosystem including a package manager and desktop framework, similar to Electron but integrated. The project is built by an individual developer, highlighting the increasing capability of solo developers to create complex software.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/themackabu/ant">GitHub - theMackabu/ ant : javascript for 's, a tiny runtime with big...</a></li>
<li><a href="https://eucloudservers.com/architecture-reliability/show-hn-ant-a-javascript-runtime-and-ecosystem/">Show HN: Ant – A JavaScript Runtime And... - EU Cloud Servers</a></li>
<li><a href="https://invertergeneratorhq.com/use-cases/show-hn-ant-a-javascript-runtime-and-ecosystem-2/">Show HN: Ant – A JavaScript runtime and... - InverterGeneratorHQ</a></li>

</ul>
</details>

**Discussion**: Community comments raise concerns about the project's originality, noting that the initial version relied heavily on the AGPL-licensed Elk engine, though the author claims a rewrite. There is also confusion over the name 'Ant' conflicting with Apache Ant and Anthropic's CLI tool. Some commenters are impressed by the solo developer's achievement, while others question the technical claims against mature runtimes.

**Tags**: `#JavaScript`, `#runtime`, `#ecosystem`, `#Show HN`

---

<a id="item-9"></a>
## [User seeks alternatives to HPSv3 for human preference prediction](https://www.reddit.com/r/MachineLearning/comments/1utdj1f/predicting_human_preference_for_generated_image/) ⭐️ 6.0/10

A Reddit user building ImageBench.ai reports that HPSv3 has limitations in predicting human preference for generated image pairs and asks the community for better alternatives. This discussion highlights the ongoing challenge of aligning automated metrics with human aesthetic judgment, which is critical for evaluating and improving generative AI models. HPSv3 is a VLM-based preference model trained on the HPDv3 dataset with 1.08M text-image pairs and 1.17M pairwise comparisons, yet the user finds it insufficient for their benchmark platform.

reddit · r/MachineLearning · /u/dh7net · Jul 11, 07:36

**Background**: Human preference prediction models like HPSv3 aim to quantify how well generated images align with human taste, but no single metric fully correlates with human judgment. ImageBench.ai is a platform that uses VLM-based judges and human evaluations to rate images.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2508.03789">[2508.03789] HPSv3: Towards Wide-Spectrum Human Preference Score</a></li>
<li><a href="https://github.com/MizzenAI/HPSv3">GitHub - MizzenAI/HPSv3: Official implementation of HPSv3: Towards Wide-Spectrum Human Preference Score (ICCV2025) · GitHub</a></li>
<li><a href="https://imagebench.ai/learn/human-evaluation">Human Evaluation</a></li>

</ul>
</details>

**Tags**: `#human preference`, `#image generation`, `#evaluation metrics`, `#HPSv3`

---
---
layout: default
title: "Horizon Summary: 2026-07-10 (EN)"
date: 2026-07-10
lang: en
---

> From 26 items, 14 important content pieces were selected

---

1. [EU Parliament Approves Chat Control 1.0 Scanning](#item-1) ⭐️ 9.0/10
2. [OpenAI Releases GPT-5.6 with Three Tiers](#item-2) ⭐️ 9.0/10
3. [Mitchell Hashimoto on Ghostty, Zig vs Rust](#item-3) ⭐️ 8.0/10
4. [U.S. Army logistics system fragile, will fail in next war](#item-4) ⭐️ 8.0/10
5. [Meta Releases Muse Spark 1.1 with API and Agentic Improvements](#item-5) ⭐️ 8.0/10
6. [Running GLM 5.2 on a 32GB RAM Laptop via Colibrì](#item-6) ⭐️ 7.0/10
7. [IMGNet: Face Verification via Sign Pattern Matching](#item-7) ⭐️ 7.0/10
8. [Tencent's Hy3 Model Free on OpenRouter, Drops in Rankings](#item-8) ⭐️ 6.0/10
9. [No Leap Second at End of 2026, IERS Announces](#item-9) ⭐️ 6.0/10
10. [Damn Interesting Blog Seeks Funding to Continue](#item-10) ⭐️ 6.0/10
11. [World's First Embodied Native Pre-trained Model Released](#item-11) ⭐️ 6.0/10
12. [Will We Ever Find Alien Civilizations?](#item-12) ⭐️ 6.0/10
13. [Why ML Conferences Surpass Journals in Prestige](#item-13) ⭐️ 6.0/10
14. [Talos-XII: Hand-written autograd and RL in Rust for gacha simulation](#item-14) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [EU Parliament Approves Chat Control 1.0 Scanning](https://www.patrick-breyer.de/en/eu-parliament-greenlights-chat-control-1-0-breyer-our-children-lose-out/) ⭐️ 9.0/10

The EU Parliament has approved Chat Control 1.0, allowing US tech companies to scan private messages without a warrant until 2028, despite a majority of MEPs voting against it. This decision undermines digital privacy and encryption for 450 million EU citizens, setting a precedent for mass surveillance that could spread globally. The measure was adopted through a procedural trick: a motion to reject required an absolute majority of all MEPs (361 votes), but only 314 voted against, 276 in favor, with 113 absent. The scanning applies to non-end-to-end encrypted services like Gmail, Facebook Messenger, Skype, and Xbox.

hackernews · rapnie · Jul 9, 11:03 · [Discussion](https://news.ycombinator.com/item?id=48843923)

**Background**: Chat Control 1.0, originally adopted voluntarily in 2021, allows scanning of private messages for child sexual abuse material (CSAM). Critics argue it breaks encryption and enables mass surveillance. The EU has been debating stricter rules, but this vote extends the voluntary regime until 2028.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Chat_Control">Chat Control - Wikipedia</a></li>
<li><a href="https://www.patrick-breyer.de/en/posts/chat-control/">Chat Control: The EU's CSAM scanner proposal</a></li>
<li><a href="https://www.techtimes.com/articles/320010/20260709/eu-parliament-passes-chat-control-default-314-meps-couldnt-block-scanning-law.htm">EU Parliament Passes Chat Control by Default: 314 MEPs Couldn't Block Scanning Law</a></li>

</ul>
</details>

**Discussion**: Commenters expressed outrage over the procedural manipulation, calling it a 'democratic failure' and a 'betrayal of privacy.' Many highlighted the irony that a majority opposed the measure but it still passed due to the absolute majority requirement.

**Tags**: `#privacy`, `#EU legislation`, `#surveillance`, `#digital rights`, `#encryption`

---

<a id="item-2"></a>
## [OpenAI Releases GPT-5.6 with Three Tiers](https://openai.com/index/gpt-5-6/) ⭐️ 9.0/10

OpenAI released GPT-5.6 on February 16, 2026, in three sizes: Luna, Terra, and Sol, with Sol achieving state-of-the-art results on the ARC-AGI-3 benchmark and doubling researcher output tokens compared to GPT-5.5. GPT-5.6 sets a new SOTA on ARC-AGI-3, a benchmark designed to measure human-like reasoning, marking a significant step toward more capable AI agents. The three-tier pricing makes advanced AI more accessible while the performance boost could accelerate research and development across industries. Pricing per 1M tokens is Luna $1/$6, Terra $2.50/$15, Sol $5/$30, with a knowledge cutoff of February 16, 2026. The model can better infer user intent and preserves original image dimensions, and Sol is the first verified frontier model to beat an ARC-AGI-3 game.

hackernews · logickkk1 · Jul 9, 17:04 · [Discussion](https://news.ycombinator.com/item?id=48849066)

**Background**: ARC-AGI-3 is an interactive reasoning benchmark that challenges AI agents to explore novel environments, infer goals, and plan actions, measuring human-like intelligence. GPT-5.5 was OpenAI's previous flagship model, and the new GPT-5.6 family offers improved reasoning and agentic capabilities.

<details><summary>References</summary>
<ul>
<li><a href="https://arcprize.org/arc-agi/3">ARC-AGI-3</a></li>
<li><a href="https://cryptobriefing.com/openai-gpt-56-pricing-tiers/">OpenAI sets GPT-5.6 pricing at $5 input, $30 output per 1M tokens with three-tier model family</a></li>
<li><a href="https://coursiv.io/blog/chatgpt-5-6">OpenAI ChatGPT 5.6: Release Date, Models, Price & Access | Coursiv Blog</a></li>

</ul>
</details>

**Discussion**: Community comments highlight that GPT-5.6 Sol achieves 7.8% on ARC-AGI-3, a new SOTA, and note that OpenAI excluded Fable 5 from comparisons because it refused most biology questions. Some users discuss switching from Claude Code to OpenAI's codex, while others point out that price-per-token comparisons are less meaningful due to varying reasoning token counts.

**Tags**: `#AI`, `#OpenAI`, `#GPT-5.6`, `#ARC-AGI`, `#LLM`

---

<a id="item-3"></a>
## [Mitchell Hashimoto on Ghostty, Zig vs Rust](https://alexalejandre.com/programming/interview-with-mitchell-hashimoto/) ⭐️ 8.0/10

Mitchell Hashimoto, creator of Ghostty, explains his choice of Zig over Rust for building a fast, cross-platform terminal emulator, citing cultural and technical reasons. This interview highlights the ongoing debate in systems programming about language trade-offs, especially between Rust and Zig, and how developer preferences shape real-world projects like Ghostty. Ghostty uses platform-native UI and GPU acceleration for performance. Hashimoto dislikes Rust's culture and finds Zig's simplicity and control more aligned with his goals.

hackernews · veqq · Jul 9, 17:17 · [Discussion](https://news.ycombinator.com/item?id=48849292)

**Background**: Ghostty is a fast, feature-rich terminal emulator released in late 2024. Zig is a systems programming language designed as an alternative to C, emphasizing simplicity and manual memory management. Rust is another systems language focused on memory safety without a garbage collector.

<details><summary>References</summary>
<ul>
<li><a href="https://ghostty.org/">Ghostty</a></li>
<li><a href="https://en.wikipedia.org/wiki/Zig_(programming_language)">Zig (programming language)</a></li>
<li><a href="https://ziglang.org/">Home ⚡ Zig Programming Language</a></li>

</ul>
</details>

**Discussion**: Comments show mixed reactions: some agree with Hashimoto's pragmatic approach, while others argue that Zig also has cultural issues. A user notes that forking projects is rare due to maintenance burden, and another disagrees with Hashimoto's preference for plain text over structured output.

**Tags**: `#Zig`, `#Rust`, `#terminal`, `#interview`, `#software engineering`

---

<a id="item-4"></a>
## [U.S. Army logistics system fragile, will fail in next war](https://mwi.westpoint.edu/the-glass-backbone-why-the-armys-logistics-will-break-in-the-next-war/) ⭐️ 8.0/10

An article from Modern War Institute argues that the U.S. Army's logistics system is over-reliant on precision and lacks resilience, predicting it will break in a major conflict. This analysis highlights a critical vulnerability in military logistics that could undermine U.S. combat effectiveness, especially as precision weapons shift the center of gravity from firepower to logistics. The article criticizes the outdated tooth-to-tail ratio concept and notes that despite frequent discussion of logistics importance, it is rarely reflected in budget requests or modernization priorities.

hackernews · baud147258 · Jul 9, 13:24 · [Discussion](https://news.ycombinator.com/item?id=48845442)

**Background**: Military logistics involves the planning and execution of moving and sustaining forces. The tooth-to-tail ratio compares combat troops (teeth) to support personnel (tail). Over-reliance on just-in-time delivery and precision systems can create fragility, as seen in Ukraine where industrial capacity and redundancy proved crucial.

**Discussion**: Commenters largely agree with the article's thesis, with some noting the pendulum swing between integrated logistics and lean warfighting. Others argue the U.S. industrial base is more capable than assumed, citing drone production and global logistics prowess.

**Tags**: `#military logistics`, `#supply chain`, `#resilience`, `#systems thinking`

---

<a id="item-5"></a>
## [Meta Releases Muse Spark 1.1 with API and Agentic Improvements](https://simonwillison.net/2026/Jul/9/muse-spark-1-1/#atom-everything) ⭐️ 8.0/10

Meta has released Muse Spark 1.1, the first version of the Spark model to offer an API, with significant improvements in agentic tool calling and computer use. The release also includes an evaluation report highlighting 'Attractor States in Self-Conversation' where two copies of the model produce existential statements. This marks a major step for Meta in making its advanced AI models accessible via API, enabling developers to integrate Muse Spark into applications. The agentic improvements position Muse Spark to compete with other leading models in autonomous task execution. The model is available via a new API, and a community plugin called llm-meta-ai provides CLI and Python library access. The evaluation report notes that self-conversation between two instances of the model leads to attractor states, producing consistent and sometimes philosophical dialogue patterns.

rss · Simon Willison · Jul 9, 16:24

**Background**: Muse Spark is a proprietary large language model developed by Meta Superintelligence Labs (MSL), first released in April 2026. It is designed to power Meta's products like Meta AI and is part of Meta's scaling ladder toward more capable AI systems. Agentic tool calling allows LLMs to autonomously select and execute external functions, bridging reasoning and action.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.30571v1">[2606.30571v1] Attractor States Emerge in Multi-Turn LLM Conversations</a></li>
<li><a href="https://ai.meta.com/blog/introducing-muse-spark-msl/">Introducing Muse Spark: Scaling Towards Personal ...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Meta`, `#Muse Spark`, `#API`, `#agentic`

---

<a id="item-6"></a>
## [Running GLM 5.2 on a 32GB RAM Laptop via Colibrì](https://github.com/JustVugg/colibri) ⭐️ 7.0/10

Developer JustVugg created Colibrì, a lightweight C-based inference engine that runs the 744B-parameter GLM 5.2 model on a 32GB RAM laptop using int4 quantization and on-demand expert streaming from disk, achieving 0.1 tokens per second. This demonstrates that even extremely large mixture-of-experts models can be run on consumer hardware without a GPU, making state-of-the-art LLMs more accessible for experimentation and offline use. Colibrì keeps the dense part (~17B params at int4, ~9.9 GB) resident in RAM, while the 21,504 routed experts (~370 GB on disk) are streamed via an LRU cache; the engine is a single ~1,300-line C file with no BLAS or Python runtime.

hackernews · vforno · Jul 9, 08:05 · [Discussion](https://news.ycombinator.com/item?id=48842459)

**Background**: GLM 5.2 is a 744B-parameter mixture-of-experts (MoE) model that activates only ~40B parameters per token, making it theoretically feasible to run on limited hardware. Int4 quantization reduces model weights to 4-bit integers, cutting memory usage with minimal accuracy loss. Multi-token prediction (MTP) speeds up inference by predicting multiple tokens at once.

<details><summary>References</summary>
<ul>
<li><a href="https://unsloth.ai/docs/models/glm-5.2">GLM-5.2 - How to Run Locally | Unsloth Documentation</a></li>
<li><a href="https://iq.opengenus.org/int4-quantization/">INT4 Quantization (with code demonstration) - OpenGenus IQ</a></li>

</ul>
</details>

**Discussion**: Commenters discussed the practical usability of such slow speeds (0.05–0.1 tok/s), with some noting that even 1 tok/s can be useful for overnight batch tasks. Others shared similar projects like thinfer for image/video gen and mmap-based approaches, and suggested that Apple's unified memory and fast SSDs could make this approach more practical.

**Tags**: `#LLM`, `#optimization`, `#local inference`, `#quantization`, `#open source`

---

<a id="item-7"></a>
## [IMGNet: Face Verification via Sign Pattern Matching](https://www.reddit.com/r/MachineLearning/comments/1urxvxh/i_built_imgnet_a_face_verification_model_that/) ⭐️ 7.0/10

IMGNet introduces a face verification model that replaces cosine similarity with sliding window sign pattern matching, achieving 96.27% accuracy on LFW with a 10.58 MB model trained on CASIA-WebFace. 这种方法挑战了余弦相似度在度量学习中的主导地位，提供了一种轻量级且可能更鲁棒的替代方案，有望在边缘设备上实现高效的人脸验证。 The model uses a SW Block that computes pixel differences at prime window sizes, and a novel IMG Sign MSE Loss defined purely over sign pattern agreement. When applied to ArcFace embeddings without retraining, it achieves 99.58% on LFW, only 0.24% below ArcFace+Cosine.

reddit · r/MachineLearning · /u/img-_- · Jul 9, 18:00

**Background**: Face verification typically compares embedding vectors using cosine similarity. IMGNet instead uses a sliding window to compare sign patterns of differences, inspired by the idea that identity is preserved through relational structure rather than absolute values.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/imamgh11/imgnet">GitHub - imamgh11/imgnet: NEW ERA OF AI</a></li>
<li><a href="https://paperswithcode.com/dataset/casia-webface">CASIA-WebFace Dataset</a></li>

</ul>
</details>

**Tags**: `#face verification`, `#deep learning`, `#computer vision`, `#metric learning`, `#efficient models`

---

<a id="item-8"></a>
## [Tencent's Hy3 Model Free on OpenRouter, Drops in Rankings](https://hy.tencent.com/research/hy3) ⭐️ 6.0/10

Tencent's Hy3 model is now available for free on OpenRouter until July 21st, but it has fallen from the top to 8th/9th place in the rankings. This indicates that even large Chinese AI models struggle to maintain user interest without clear differentiation, and the competitive landscape for open models is intensifying. Hy3 is a 295B-parameter Mixture-of-Experts (MoE) model with 21B active parameters, developed by Tencent. Its effective input price on OpenRouter is now the same as DeepSeek-hosted DeepSeek Flash V4.

hackernews · andai · Jul 9, 15:27 · [Discussion](https://news.ycombinator.com/item?id=48847552)

**Background**: OpenRouter is a unified API platform that provides access to over 400 AI models from multiple providers. Hy3 (also known as Hunyuan) is Tencent's latest large language model, first previewed in late April 2026.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/tencent/Hy3">tencent/Hy3 · Hugging Face</a></li>
<li><a href="https://openrouter.ai/">OpenRouter</a></li>
<li><a href="https://www.tencent.com/en-us/articles/2202320.html">Tencent Unveils Hy3 preview; Model Enhances Agent Capabilities and Real-World Usability - Tencent 腾讯</a></li>

</ul>
</details>

**Discussion**: Commenters note that Hy3's free tier is likely a promotion by Novita Labs, and that the model faces stiff competition from other open Chinese models like GLM. Some users find the pricing confusing and question the model's value compared to alternatives.

**Tags**: `#AI`, `#LLM`, `#OpenRouter`, `#Tencent`

---

<a id="item-9"></a>
## [No Leap Second at End of 2026, IERS Announces](https://datacenter.iers.org/data/latestVersion/bulletinC.txt) ⭐️ 6.0/10

The International Earth Rotation and Reference Systems Service (IERS) has announced that no leap second will be introduced at the end of December 2026, maintaining the current UTC-TAI offset at -37 seconds. This routine announcement is significant for timekeeping systems worldwide, as leap seconds can disrupt computer networks, financial transactions, and satellite navigation. The continued absence of a leap second provides temporary stability for these systems. The decision is based on Earth's rotational data; all 27 leap seconds since 1972 have been positive. The IERS typically announces leap seconds six months in advance, and this bulletin confirms no adjustment is needed.

hackernews · ChrisArchitect · Jul 9, 14:16 · [Discussion](https://news.ycombinator.com/item?id=48846281)

**Background**: Leap seconds are one-second adjustments to Coordinated Universal Time (UTC) to keep it within 0.9 seconds of mean solar time (UT1), which varies due to irregularities in Earth's rotation. The IERS monitors Earth's rotation and decides when to add or remove a leap second. The last leap second was added on December 31, 2016.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Leap_second">Leap second</a></li>
<li><a href="https://en.wikipedia.org/wiki/International_Earth_Rotation_Service">International Earth Rotation Service</a></li>
<li><a href="https://en.wikipedia.org/wiki/Coordinated_Universal_Time">Coordinated Universal Time - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters discussed the unpredictability of Earth's rotation, with some noting that geological and weather factors cause variations. Others pointed out that the UTC-TAI offset remains at -37 seconds, meaning the UTC-GPS offset stays at -18 seconds, and debated the impact on UNIX timestamps and legacy systems.

**Tags**: `#leap second`, `#timekeeping`, `#UTC`, `#UNIX timestamp`, `#Earth rotation`

---

<a id="item-10"></a>
## [Damn Interesting Blog Seeks Funding to Continue](https://www.damninteresting.com/a-possible-future/) ⭐️ 6.0/10

The creator of Damn Interesting announced a funding drive to sustain the blog, which has been running for many years. This highlights the ongoing challenge of sustaining independent, high-quality content on the web, and the community's willingness to support it. The blog has a long history and is known for thorough, interesting articles; the funding request is modest, and the community response has been positive.

hackernews · mzur · Jul 9, 15:25 · [Discussion](https://news.ycombinator.com/item?id=48847511)

**Background**: Damn Interesting is a long-running blog that publishes in-depth articles on a wide range of fascinating topics. It has been a precursor to many popular podcasts and content formats. The site relies on community support to continue operating.

**Discussion**: Commenters expressed nostalgia and appreciation for the blog, with many sharing personal memories and pledging support. Some suggested using Patreon or similar models for sustainable funding.

**Tags**: `#blog`, `#community`, `#funding`, `#nostalgia`

---

<a id="item-11"></a>
## [World's First Embodied Native Pre-trained Model Released](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&mid=2247902774&idx=1&sn=55d8846a7ef42993d385848631d4cc2a) ⭐️ 6.0/10

Ant Lingbo released LingBot-VA 2.0, the industry's first embodiment-native world action model, which shifts robot foundation models from digital-world-based to physical-world-native design. This marks a key transformation in embodied AI, as robot brains no longer rely on digital simulations but are natively designed for the physical world, potentially improving real-world performance and generalization. LingBot-VA 2.0 uses a Mixture-of-Transformers (MoT) architecture for cross-modal fusion of video processing and action control, and features autoregressive prediction of future video latents and robot actions.

rss · 量子位 · Jul 10, 06:21

**Background**: Traditional robot foundation models are often pre-trained on digital simulations or internet data, which may not capture the complexity of the physical world. Embodied native models are designed from the ground up to learn directly from physical interactions, aiming for better transfer to real-world tasks.

<details><summary>References</summary>
<ul>
<li><a href="https://www.aibase.com/news/25103">World Models Enter the Physical World: Antlingbot Opens Source...</a></li>
<li><a href="https://huggingface.co/docs/lerobot/en/lingbot_va">LingBot - VA · Hugging Face</a></li>
<li><a href="https://news.aibase.com/news/29517">Pre-train from Scratch: Ant Lingbo Releases the Embodied ...</a></li>

</ul>
</details>

**Tags**: `#embodied AI`, `#robotics`, `#pre-trained model`, `#AI`

---

<a id="item-12"></a>
## [Will We Ever Find Alien Civilizations?](https://www.quantamagazine.org/will-we-ever-find-alien-civilizations-20260709/) ⭐️ 6.0/10

Astronomer David Kipping discusses the statistical challenges in searching for extraterrestrial life and argues that it is rational to consider the possibility that we may be alone. This discussion highlights the need for a more rigorous statistical approach in astrobiology, which could reshape how scientists interpret ambiguous signals and prioritize future missions. Kipping points out that many claims of extraterrestrial life have failed under scrutiny, and advocates for Bayesian statistics to quantify the probability of alien civilizations.

rss · Quanta Magazine · Jul 9, 13:39

**Background**: The search for extraterrestrial intelligence (SETI) has been ongoing for decades, but no definitive evidence has been found. Bayesian statistics provides a framework for updating beliefs based on new evidence, which can help assess the likelihood of rare events like alien civilizations.

**Tags**: `#astronomy`, `#extraterrestrial life`, `#statistics`, `#science`

---

<a id="item-13"></a>
## [Why ML Conferences Surpass Journals in Prestige](https://www.reddit.com/r/MachineLearning/comments/1urqqk6/journals_vs_conferences_ml_research_r/) ⭐️ 6.0/10

A Reddit user questions why machine learning conferences like ICML and NeurIPS have become more prestigious than traditional journals in recent years, sparking discussion about the shift in academic publishing culture. This trend affects how ML research is disseminated, evaluated, and rewarded, potentially influencing career advancement and the pace of innovation in the field. The user notes that the shift has been particularly noticeable in the last two to three years, coinciding with the AI boom and increased demand for rapid dissemination of results.

reddit · r/MachineLearning · /u/hg_wallstreetbets · Jul 9, 13:44

**Background**: In many scientific fields, journals have traditionally been the gold standard for publishing research, with rigorous peer review and high prestige. However, in machine learning, conferences such as ICML and NeurIPS have gained prominence due to faster review cycles, higher acceptance rates, and the field's emphasis on timely results.

**Tags**: `#machine learning`, `#academic publishing`, `#conferences`, `#journals`

---

<a id="item-14"></a>
## [Talos-XII: Hand-written autograd and RL in Rust for gacha simulation](https://www.reddit.com/r/MachineLearning/comments/1urvxgb/talosxii_handwritten_autograd_small_rlmlp_stack/) ⭐️ 6.0/10

A developer released Talos-XII, a CLI simulator for the gacha system in Arknights: Endfield that uses a hand-written autograd engine and reinforcement learning models (Dueling DQN, PPO) entirely in Rust, without any external ML frameworks like PyTorch or ndarray. This project demonstrates that a full ML stack—autograd, neural networks, and RL algorithms—can be built from scratch in Rust for a niche application, offering performance and portability without heavy dependencies. It also invites community benchmarking to validate its custom ACHF component across different hardware. The project includes a custom autograd engine with SIMD dispatch (scalar, AVX2, AVX-512, NEON), Rayon-parallelized simulations, BF16 inference caches, and an optional PyO3 bridge. The ACHF component blends dense and sparse paths with a gradient-sensitive gate and Sinkhorn projection, but its effectiveness on non-author hardware is unverified.

reddit · r/MachineLearning · /u/zay0kami · Jul 9, 16:52

**Background**: Autograd (automatic differentiation) is a technique that automatically computes gradients, essential for training neural networks. Reinforcement learning algorithms like Dueling DQN and PPO are used to make sequential decisions under uncertainty. Gacha systems in games involve random item draws with pity mechanics, which can be modeled as a stochastic process.

<details><summary>References</summary>
<ul>
<li><a href="https://www.evis.dev/posts/nanograd">Building an Autograd system in Rust - Evis</a></li>
<li><a href="https://medium.com/@sainijagjit/understanding-dueling-dqn-a-deep-dive-into-reinforcement-learning-575f6fe4328c">Understanding Dueling DQN: A Deep Dive into Reinforcement ...</a></li>
<li><a href="https://fer14.github.io/raice/06_ppo.html">PPO (Proximal Policy Optimization) — RL Course</a></li>

</ul>
</details>

**Tags**: `#Rust`, `#reinforcement learning`, `#autograd`, `#gacha`, `#simulation`

---
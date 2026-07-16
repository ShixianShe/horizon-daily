---
layout: default
title: "Horizon Summary: 2026-07-16 (EN)"
date: 2026-07-16
lang: en
---

> From 19 items, 14 important content pieces were selected

---

1. [xAI Open-Sources Grok Build After Privacy Scandal](#item-1) ⭐️ 9.0/10
2. [Thinking Machines AI Releases Inkling, an Open-Weights Multimodal Model](#item-2) ⭐️ 8.0/10
3. [Running Gemma 4 26B at 5 tokens/sec on 13-year-old Xeon](#item-3) ⭐️ 8.0/10
4. [Claude web_fetch bypass enables memory exfiltration](#item-4) ⭐️ 8.0/10
5. [Thermodynamic Computers Harness Random Energy Fluctuations](#item-5) ⭐️ 8.0/10
6. [Disentangling Convolutional Neurons via Hadamard Clustering](#item-6) ⭐️ 8.0/10
7. [SQLite Should Adopt Rust-Style Editions](#item-7) ⭐️ 7.0/10
8. [Call for Investment in Free Open Source AI](#item-8) ⭐️ 7.0/10
9. [Seeking Devil's Advocate on JEPA for World Models](#item-9) ⭐️ 7.0/10
10. [PyTorch model 170x slower on T4 vs A100](#item-10) ⭐️ 7.0/10
11. [Nostalgia for Specialized ML Conferences](#item-11) ⭐️ 7.0/10
12. [Does Closing Line Edge Transfer to Earlier Bets?](#item-12) ⭐️ 7.0/10
13. [Mermaid Diagrams Rendered as Unicode Box Art via WebAssembly](#item-13) ⭐️ 6.0/10
14. [Gödel's Incompleteness and Neural Network Limits](#item-14) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [xAI Open-Sources Grok Build After Privacy Scandal](https://simonwillison.net/2026/Jul/15/grok-build/#atom-everything) ⭐️ 9.0/10

xAI released the entire Grok Build codebase under an Apache 2.0 license on July 15, 2026, following severe backlash over the grok CLI tool uploading entire directories to Google Cloud. The company also deleted all retained user data and disabled default data retention. This move aims to restore user trust after a major privacy incident, and the open-sourcing of a large Rust codebase (844,530 lines) provides transparency and allows community auditing. It also sets a precedent for AI coding tools to prioritize privacy and openness. The codebase contains 844,530 lines of Rust with only about 3% vendored code, and includes a self-contained terminal renderer for Mermaid diagrams. Remnants of the upload-to-GCS code remain but are disabled, and the repository has only a single initial commit.

rss · Simon Willison · Jul 15, 23:59

**Background**: The grok CLI tool, used as a coding agent, was found to upload entire directories—including SSH keys and password databases—to xAI's Google Cloud buckets. Security researcher cereblab confirmed the data exfiltration via wire-level analysis, showing the tool sent about 27,800 times more data than needed.

<details><summary>References</summary>
<ul>
<li><a href="https://www.internationalcyberdigest.com/xais-grok-build-cli-uploads-entire-git-repositories-to-a-google-cloud-bucket/">xAI's Grok Build CLI Uploads Entire Git repositories to a Google Cloud Bucket</a></li>

</ul>
</details>

**Discussion**: Community reactions are mixed: some appreciate the open-sourcing and rapid response, while others view it as a tactical move to salvage reputation. Forks like 'gork-build' and 'dgrok' have already emerged to strip telemetry and add multi-provider support.

**Tags**: `#open source`, `#security`, `#AI`, `#privacy`, `#xAI`

---

<a id="item-2"></a>
## [Thinking Machines AI Releases Inkling, an Open-Weights Multimodal Model](https://thinkingmachines.ai/news/introducing-inkling/) ⭐️ 8.0/10

Thinking Machines AI has released Inkling, a large open-weights multimodal model that supports audio, text, and image inputs. The model is available for fine-tuning on the Tinker platform and can be run locally via llama.cpp and other tools. Inkling is the largest open-weights model to support audio, enabling enterprises to customize and deploy a frontier-capable model at lower cost. Its release strengthens the open-weights ecosystem and provides a competitive alternative to closed models. Inkling is not the strongest overall model but offers a combination of multimodal capabilities, efficient thinking, and availability for fine-tuning on Tinker. Community members have already created GGUF and NVFP4 quantizations for local deployment.

hackernews · vimarsh6739 · Jul 15, 18:12 · [Discussion](https://news.ycombinator.com/item?id=48924912)

**Background**: Open-weights models make their trained parameters publicly available, allowing anyone to use, modify, and fine-tune them. Multimodal models process multiple data types like text, images, and audio, enabling richer interactions. Inkling's audio support is a notable step forward for open-weights models.

<details><summary>References</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/open-weights-llms-in-depth-analysis-adoption-usage-performance-jha-kymhc">Open - Weights LLMs: In-Depth Analysis of Adoption, Usage, and...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Multimodal_model">Multimodal model</a></li>
<li><a href="https://www.ibm.com/think/topics/multimodal-ai">What is Multimodal AI? | IBM</a></li>

</ul>
</details>

**Discussion**: Community comments are largely positive, with users highlighting Inkling's potential for customization and local deployment. Some express hope that Thinking Machines AI could become a leading open-weights provider, similar to DeepSeek or Z.ai. Others note the complexity of modern model design and the value of open base models for enterprise fine-tuning.

**Tags**: `#open-weights`, `#multimodal`, `#AI model`, `#audio`, `#machine learning`

---

<a id="item-3"></a>
## [Running Gemma 4 26B at 5 tokens/sec on 13-year-old Xeon](https://www.neomindlabs.com/2026/06/08/running-gemma-4-26b-at-5-tokens-sec-on-a-13-year-old-xeon-with-no-gpu/) ⭐️ 8.0/10

A technical blog post demonstrates running Google's Gemma 4 26B A4B model at 5 tokens per second on a 13-year-old dual Xeon server without any GPU, using CPU-only inference. This shows that modern large language models can run on extremely old hardware, potentially lowering the barrier for local AI inference and sparking debate about cost efficiency compared to cloud APIs. The setup uses a dual Xeon E5-2697 v2 (12 cores each, 2.7 GHz) with 256 GB DDR3 RAM, achieving 5 tokens/sec for output generation. The model is Gemma 4 26B A4B, a 26B-parameter MoE model with 4B active parameters.

hackernews · neomindryan · Jul 15, 15:34 · [Discussion](https://news.ycombinator.com/item?id=48922434)

**Background**: Gemma 4 is a family of open-weight multimodal models from Google DeepMind, supporting text and image input. The 26B A4B variant uses a Mixture-of-Experts architecture, activating only 4B parameters per token, which makes CPU inference more feasible. Running LLMs on CPU is typically much slower than on GPU but can be cost-effective for certain use cases.

<details><summary>References</summary>
<ul>
<li><a href="https://ai.google.dev/gemma/docs/core">Gemma 4 model overview - Google AI for Developers</a></li>
<li><a href="https://huggingface.co/google/gemma-4-26B-A4B-it">google/gemma-4-26B-A4B-it · Hugging Face</a></li>
<li><a href="https://insiderllm.com/guides/cpu-only-llms-what-actually-works/">CPU-Only LLMs: What Actually Works | InsiderLLM</a></li>

</ul>
</details>

**Discussion**: Commenters debated the cost efficiency of local CPU inference versus cloud APIs, with estimates showing electricity costs in Germany ($0.30/kWh) making local inference more expensive per token than using OpenRouter. Some users reported faster speeds (8-12 t/s) on similar hardware, while others predicted that by mid-2027, 200B+ MoE models will run on consumer hardware.

**Tags**: `#local inference`, `#LLM`, `#hardware`, `#cost analysis`, `#Gemma`

---

<a id="item-4"></a>
## [Claude web_fetch bypass enables memory exfiltration](https://simonwillison.net/2026/Jul/15/claude-web-fetch-exfiltration/#atom-everything) ⭐️ 8.0/10

Security researcher Ayush Paul discovered a bypass in Anthropic's Claude web_fetch tool that allowed an attacker to exfiltrate user memories (name, city, employer) by tricking the model into following nested links from a malicious honeypot page. This vulnerability demonstrates a practical data exfiltration attack against an AI assistant with memory, highlighting that even well-designed protections can be circumvented by creative prompt injection, posing serious privacy risks for users who store personal information in AI memories. The attack exploited a loophole where web_fetch was allowed to visit URLs embedded in previously fetched pages; the honeypot page only served the malicious content to clients with 'Claude-User' in their user-agent to evade detection. Anthropic had already identified the issue internally and closed the hole by removing the ability for web_fetch to navigate to additional links within fetched content.

rss · Simon Willison · Jul 15, 14:21

**Background**: The 'lethal trifecta' describes a dangerous combination for AI agents: access to private data, ability to communicate externally, and exposure to untrusted content. Claude's web_fetch tool is designed to only fetch URLs explicitly provided by the user or returned from web_search, preventing direct exfiltration. However, the ability to follow links within fetched pages created a new attack surface.

<details><summary>References</summary>
<ul>
<li><a href="https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool">Web fetch tool - Claude Platform Docs</a></li>
<li><a href="https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/">The lethal trifecta for AI agents: private data, untrusted content, and...</a></li>

</ul>
</details>

**Discussion**: The Hacker News discussion (source: news.ycombinator.com/item?id=48916975) generally praised the researcher's creativity and highlighted the importance of such security research. Some commenters noted that the fix—disallowing navigation to links within fetched content—may break legitimate use cases, and debated whether Anthropic's decision not to pay a bug bounty was justified given they had already identified the issue.

**Tags**: `#AI security`, `#data exfiltration`, `#Claude`, `#prompt injection`, `#vulnerability`

---

<a id="item-5"></a>
## [Thermodynamic Computers Harness Random Energy Fluctuations](https://www.quantamagazine.org/thermodynamic-computers-go-with-the-energy-flow-20260715/) ⭐️ 8.0/10

A new paradigm called thermodynamic computing flips conventional computing on its head by using random thermal fluctuations as a resource for computation, rather than fighting them as noise. This approach is gaining traction, with recent advances in design and training of thermodynamic hardware. Thermodynamic computing could dramatically improve energy efficiency in computing, especially for AI and machine learning workloads, potentially reducing the enormous power consumption of modern GPUs. It represents a fundamental shift in computer architecture that aligns computation with natural physical processes. Unlike classical and quantum computers that seek to eliminate thermal noise, thermodynamic computers use those fluctuations as their power source. The field has been accelerating since the early 2020s, driven by the computing needs of artificial intelligence.

rss · Quanta Magazine · Jul 15, 15:24

**Background**: Conventional computers require precise control and error correction to avoid errors from random energy fluctuations. Thermodynamic computing inverts this by leveraging the natural randomness of thermal energy to perform stochastic computations, similar to how stochastic computing works but at a fundamental physical level.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Thermodynamic_computing">Thermodynamic computing - Wikipedia</a></li>
<li><a href="https://extropic.ai/writing/thermodynamic-computing-from-zero-to-one">Thermodynamic Computing: From Zero to One | Extropic</a></li>
<li><a href="https://www.nersc.gov/news-and-events/news/thermodynamic-computing-advances-with-design-and-training">Thermodynamic Computing Advances with Design and Training - NERSC: National Energy Research Scientific Computing Center</a></li>

</ul>
</details>

**Tags**: `#thermodynamic computing`, `#energy efficiency`, `#computer architecture`, `#physics of computation`

---

<a id="item-6"></a>
## [Disentangling Convolutional Neurons via Hadamard Clustering](https://www.reddit.com/r/MachineLearning/comments/1uwya70/mechanistic_interpretability_a_first_paper_on/) ⭐️ 8.0/10

A new method uses Hadamard product clustering to disentangle individual convolutional neurons in InceptionV1, revealing monosemantic clusters (e.g., cars, cats) and unexpected low-valued activations (e.g., letters) with shared dependent neurons. This work advances mechanistic interpretability by providing a novel technique to analyze convolutional neurons, potentially enabling better understanding of neural network internals and improving model transparency. The method clusters the Hadamard product of receptive field and neuron weights to identify patterns, and found that low-valued clusters have evenly distributed positive and negative weights among dependent neurons, suggesting deliberate gradient descent behavior.

reddit · r/MachineLearning · /u/narang_27 · Jul 15, 06:59

**Background**: Mechanistic interpretability aims to reverse-engineer neural networks by understanding individual components like neurons. Convolutional neurons detect patterns in images, and the Hadamard product (element-wise multiplication) of input and weights reveals what the neuron 'sees'. Monosemantic neurons respond to a single concept, while polysemantic neurons respond to multiple.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Hadamard_product_(matrices)">Hadamard product (matrices) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Inception_(deep_learning_architecture)">Inception (deep learning architecture) - Wikipedia</a></li>
<li><a href="https://transformer-circuits.pub/2024/scaling-monosemanticity/">Scaling Monosemanticity: Extracting Interpretable Features from...</a></li>

</ul>
</details>

**Discussion**: The author notes that starting with convolutions may have limited interest, and plans to shift to language models. No community comments are provided.

**Tags**: `#mechanistic interpretability`, `#convolutional neural networks`, `#neuron analysis`, `#InceptionV1`

---

<a id="item-7"></a>
## [SQLite Should Adopt Rust-Style Editions](https://mort.coffee/home/sqlite-editions/) ⭐️ 7.0/10

A proposal suggests introducing Rust-style editions in SQLite, allowing opt-in breaking changes and improved defaults while maintaining backward compatibility. This could resolve long-standing SQLite design issues without breaking existing databases, enabling the project to evolve more freely while preserving its reputation for stability. The proposal includes a PRAGMA edition statement to select the edition, similar to Rust's `edition = "2021"` in Cargo.toml, and suggests editions like 2026 for new defaults.

hackernews · gnyeki · Jul 15, 22:42 · [Discussion](https://news.ycombinator.com/item?id=48928135)

**Background**: SQLite is a widely used embedded database that prioritizes backward compatibility, making it difficult to fix design flaws or update defaults. Rust editions provide a mechanism to introduce breaking changes in a controlled, opt-in way, which SQLite could emulate.

<details><summary>References</summary>
<ul>
<li><a href="https://doc.rust-lang.org/edition-guide/editions/">What are editions ? - The Rust Edition Guide</a></li>
<li><a href="https://www.sqlite.org/docs.html?ref=srccodes.com">SQLite Documentation</a></li>

</ul>
</details>

**Discussion**: Commenters generally support the idea, noting it provides a clear opt-in path for improvements. Some raise concerns about portability of database files across SQLite versions and the inability for iOS apps to change compile-time defaults.

**Tags**: `#SQLite`, `#database design`, `#backward compatibility`, `#Rust editions`, `#software evolution`

---

<a id="item-8"></a>
## [Call for Investment in Free Open Source AI](https://www.siegelendowment.org/wp-content/uploads/2026/07/fortune-david-siegel-open-source-ai.pdf) ⭐️ 7.0/10

David Siegel, in a Fortune op-ed, argues that governments, companies, and nonprofits should invest in free, open source AI to ensure broad access and prevent monopolization. This proposal challenges the current dominance of proprietary AI models and could reshape AI development incentives, making advanced AI more accessible and equitable. The op-ed is published by the Siegel Family Endowment and appears in Fortune magazine, sparking debate on whether prizes or direct funding can effectively incentivize open source AI.

hackernews · bilsbie · Jul 15, 21:16 · [Discussion](https://news.ycombinator.com/item?id=48927095)

**Background**: Open source AI refers to models whose code and weights are publicly available, allowing anyone to use, modify, and distribute them. Currently, most powerful AI models are proprietary, controlled by a few large companies, raising concerns about access and fairness.

**Discussion**: Commenters debate the feasibility: some propose prize mechanisms to incentivize open models, while others argue that commercial AI will always dominate due to profit motives, and that goodwill alone cannot compete with paid development.

**Tags**: `#open source`, `#AI policy`, `#investment`, `#incentives`

---

<a id="item-9"></a>
## [Seeking Devil's Advocate on JEPA for World Models](https://www.reddit.com/r/MachineLearning/comments/1uxcryc/looking_for_jepa_devil_advocates_r/) ⭐️ 7.0/10

A Reddit user researching world models for robot learning is actively soliciting critical perspectives on Yann LeCun's JEPA architecture, questioning its potential downsides compared to other approaches like LLMs and RL. This discussion highlights the growing debate around JEPA as a foundation for world models, which could influence the direction of AI research in robotics and beyond. Understanding its limitations is crucial for researchers deciding whether to adopt this paradigm. The user notes that LeCun's presentations often dismiss LLMs and RL while promoting JEPA as the 'only next big thing,' prompting a search for red flags. The post has a score of 7.0/10, indicating high community interest.

reddit · r/MachineLearning · /u/Amazing-Coat5160 · Jul 15, 17:34

**Background**: JEPA (Joint Embedding Predictive Architecture) is a self-supervised learning approach proposed by Yann LeCun that predicts in abstract representation space rather than pixel space, aiming to build world models for planning and reasoning. It contrasts with generative models like LLMs and diffusion models, which predict in output space. Recent implementations like V-JEPA 2 from Meta show promise in robotics for action prediction and object interaction.

<details><summary>References</summary>
<ul>
<li><a href="https://ai.meta.com/blog/v-jepa-2-world-model-benchmarks/">Introducing the V-JEPA 2 world model and new benchmarks for ...</a></li>
<li><a href="https://arxiv.org/abs/2603.19312">[2603.19312] LeWorldModel: Stable End-to-End Joint-Embedding ... A Generalization Theory for JEPA-Based World Models Deep Dive into Yann LeCun’s JEPA | Rohit Bandaru The Anatomy of JEPA: The Architecture Behind ... - Medium Introducing V-JEPA 2 - ai.meta.com V-JEPA | Self-Supervised Visual World Model | world-models.io</a></li>
<li><a href="https://mishig-jepawiki.hf.space/wiki/concepts/jepa-vs-alternatives">JEPA vs Alternatives: LLMs, Diffusion, Contrastive, MAE - JEPA Wiki</a></li>

</ul>
</details>

**Discussion**: The post has no comments yet, but the high score suggests the topic resonates with the community. Future comments may include critiques about JEPA's training stability, theoretical guarantees, or scalability compared to alternatives.

**Tags**: `#JEPA`, `#world models`, `#robot learning`, `#Yann LeCun`, `#machine learning`

---

<a id="item-10"></a>
## [PyTorch model 170x slower on T4 vs A100](https://www.reddit.com/r/MachineLearning/comments/1ux6a9x/pytorch_model_running_170x_slower_on_t4_vs_a100/) ⭐️ 7.0/10

A PyTorch point-tracking model runs 170x slower on an NVIDIA T4 GPU (85 seconds) compared to an A100 (0.5 seconds) for a 47-frame 256x256 video, despite both GPUs being fully utilized. This extreme performance gap highlights how memory bandwidth and tensor core utilization can dominate real-world inference speed, especially for operations like 4D correlation volumes that are memory-bound in FP32. The model uses pure FP32 precision and builds 4D correlation volumes for dense matching between frames, followed by transformer layers. The T4 has only 320 GB/s memory bandwidth vs A100's 1,555 GB/s, and lacks FP32 tensor cores, forcing FP32 operations to run on CUDA cores.

reddit · r/MachineLearning · /u/Future-Structure-296 · Jul 15, 13:44

**Background**: The NVIDIA T4 (Turing architecture) and A100 (Ampere architecture) are both data center GPUs, but A100 has significantly higher memory bandwidth (1,555 GB/s vs 320 GB/s) and supports tensor cores for FP32 mixed-precision operations. 4D correlation volumes are memory-intensive operations common in optical flow and point tracking, which can bottleneck on memory bandwidth when run in FP32 without tensor core acceleration.

<details><summary>References</summary>
<ul>
<li><a href="https://www.server-parts.eu/post/nvidia-t4-vs-a100-gpu-comparison-ai-deep-learning-data-centers">NVIDIA T4 vs. NVIDIA A100 Comparison: Which GPU Should You ...</a></li>
<li><a href="https://discuss.pytorch.org/t/could-pytorch-provide-correlation-operator/84030">Could pytorch provide correlation operator? - vision - PyTorch Forums</a></li>
<li><a href="https://www.nvidia.com/content/dam/en-zz/Solutions/Data-Center/tesla-t4/t4-tensor-core-datasheet-951643.pdf">NVIDIA T4 TENSOR CORE GPU SPECIFICATIONS GPU Architecture NVIDIA Turing</a></li>

</ul>
</details>

**Discussion**: Comments suggest profiling memory bandwidth usage with tools like nvprof or Nsight Compute, and recommend switching to mixed precision (FP16) to leverage T4's tensor cores. Some note that the 4D correlation operation is inherently memory-bound and may not benefit from tensor cores even in FP16.

**Tags**: `#PyTorch`, `#GPU Performance`, `#NVIDIA T4`, `#NVIDIA A100`, `#Deep Learning`

---

<a id="item-11"></a>
## [Nostalgia for Specialized ML Conferences](https://www.reddit.com/r/MachineLearning/comments/1uwy25k/does_anyone_else_miss_the_old_conference/) ⭐️ 7.0/10

A Reddit discussion laments the decline of specialized ML conferences like BMVC, ACCV, FG, ICIP, and ICASSP, as research concentrates into a few flagship venues. This trend risks reducing diversity in research dissemination, potentially burying high-quality papers in non-archival submissions or arXiv-only publications, and fragmenting focused communities. The original poster notes that conferences like FG were once the hub for face analysis and ICASSP for signal processing, but now submission numbers explode while review capacity remains limited, leading to inconsistent reviews.

reddit · r/MachineLearning · /u/Sep29493919 · Jul 15, 06:47

**Background**: In machine learning, conferences are primary venues for publishing research. Flagship conferences (e.g., NeurIPS, ICML, CVPR) have grown extremely large, while smaller specialized conferences struggle to attract submissions and attendees. Non-archival submissions are papers presented at conferences but not included in official proceedings, often leading to less visibility.

<details><summary>References</summary>
<ul>
<li><a href="https://www.bmva.org/bmvc">The British Machine Vision Association : The British Machine Vision Conference (BMVC)</a></li>
<li><a href="https://accv2026.org/">ACCV 2026 – Asian Conference on Computer Vision</a></li>
<li><a href="https://logconference.org/cfp/">Learning on Graphs Conference</a></li>

</ul>
</details>

**Discussion**: The discussion resonates with many users who share similar nostalgia and concerns about paper quality and community fragmentation. Some argue that flagship conferences still publish excellent work, but others worry that good papers are lost in the noise.

**Tags**: `#machine learning`, `#conferences`, `#research ecosystem`, `#peer review`, `#academia`

---

<a id="item-12"></a>
## [Does Closing Line Edge Transfer to Earlier Bets?](https://www.reddit.com/r/MachineLearning/comments/1ux1n0v/if_your_model_finds_edge_against_closing_lines/) ⭐️ 7.0/10

A sports prediction modeler found consistent edge against closing lines in backtesting, but at inference time (12-24 hours before events) the strongest feature—line movement—is incomplete, raising a paradox about whether that edge transfers to earlier, less efficient lines. This question is critical for sports prediction practitioners because it highlights a common backtesting pitfall: using features that are unavailable at inference time can lead to overestimated real-world performance. Resolving this tradeoff could improve model evaluation and betting strategy design. The model's strongest feature is line movement from opening to closing implied probability, but at prediction time only the current line (not the closing line) is available, making the feature incomplete. The user wonders whether the edge against efficient closing lines persists when betting against earlier, less efficient lines with a weaker signal.

reddit · r/MachineLearning · /u/MrProbability101 · Jul 15, 10:11

**Background**: In sports betting, closing lines are considered highly efficient because they incorporate all public information, sharp money, and late-breaking news. Closing Line Value (CLV) is a widely used metric to evaluate model quality: positive CLV indicates the model beats the market. However, backtesting with features that are not available at inference time (like full line movement) introduces lookahead bias, potentially inflating backtest results.

<details><summary>References</summary>
<ul>
<li><a href="https://fastercapital.com/content/Lookahead-Bias-in-Sports-Predictions--The-Science-of-Accurate-Forecasts.html">Lookahead Bias in Sports Predictions: The Science of Accurate Forecasts - FasterCapital</a></li>
<li><a href="https://app.olympus-bets.com/guides/closing-line-value">Closing Line Value (CLV): The Best Predictor of Long-Term ...</a></li>
<li><a href="https://www.odinpicks.com/en/blog/pinnacle-closing-line-market-efficiency-analysis">Pinnacle Closing Line Analysis: How Efficient Are Sports ...</a></li>

</ul>
</details>

**Discussion**: The Reddit discussion likely includes comments warning about lookahead bias and suggesting that the edge may not transfer because the incomplete feature weakens predictions. Some may argue that earlier lines are less efficient, offering more opportunities, but the model's signal degradation could offset that advantage.

**Tags**: `#machine learning`, `#sports prediction`, `#backtesting`, `#feature engineering`, `#model evaluation`

---

<a id="item-13"></a>
## [Mermaid Diagrams Rendered as Unicode Box Art via WebAssembly](https://simonwillison.net/2026/Jul/16/grok-mermaid/#atom-everything) ⭐️ 6.0/10

Simon Willison created a WebAssembly-based tool called grok-mermaid that converts Mermaid diagrams into Unicode box art for terminal display, porting a Rust renderer from xAI's Grok CLI codebase to the browser. This tool bridges the gap between diagramming and terminal-based workflows, enabling developers to view Mermaid diagrams directly in CLI environments without a graphical browser, which is especially useful for remote SSH sessions or documentation in code comments. The tool is built by compiling the Rust crate xai-grok-markdown to WebAssembly, allowing it to run entirely in the browser. It includes a live editor where users can input Mermaid syntax and see the Unicode box art output in real time, with options to copy as text or share via link.

rss · Simon Willison · Jul 16, 00:33

**Background**: Mermaid is an open-source diagramming tool that uses a Markdown-like syntax to generate flowcharts, sequence diagrams, and more. WebAssembly (Wasm) is a binary instruction format that allows code written in languages like Rust to run in web browsers with near-native performance. The Grok CLI is an open-source coding agent from xAI that includes a terminal renderer for Mermaid diagrams.

<details><summary>References</summary>
<ul>
<li><a href="https://mermaid.js.org/">Mermaid | Diagramming and charting tool</a></li>
<li><a href="https://en.wikipedia.org/wiki/WebAssembly">WebAssembly</a></li>
<li><a href="https://github.com/superagent-ai/grok-cli">GitHub - superagent-ai/ grok - cli : An open-source coding agent for the...</a></li>

</ul>
</details>

**Tags**: `#Mermaid`, `#WebAssembly`, `#Rust`, `#diagramming`, `#CLI`

---

<a id="item-14"></a>
## [Gödel's Incompleteness and Neural Network Limits](https://www.reddit.com/r/MachineLearning/comments/1uwxveq/infinities_impossibilities_and_the_man_in_the/) ⭐️ 6.0/10

A blog post by Iain Harper connects Gödel's incompleteness theorems to the fundamental limitations of neural networks, drawing on Matthew Colbrook's 2022 PNAS paper on unstable neural networks. This perspective challenges the prevailing assumption that more data and compute can solve any problem, highlighting deep theoretical limits in AI that echo foundational issues in mathematics and logic. Colbrook's paper shows a paradox: training algorithms often find unstable neural networks despite the existence of stable ones, relating to Smale's 18th problem on AI limits. Gödel's theorems state that any consistent formal system cannot prove all truths about arithmetic.

reddit · r/MachineLearning · /u/iainrfharper · Jul 15, 06:36

**Background**: Gödel's incompleteness theorems, published in 1931, show inherent limits in formal axiomatic systems: there are true statements that cannot be proven within the system. Neural networks, as computational models, may face analogous limitations in learning certain functions or achieving stability, as explored by Colbrook's work on instability in deep learning.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Gödel's_incompleteness_theorems">Gödel's incompleteness theorems</a></li>
<li><a href="https://www.pnas.org/doi/10.1073/pnas.2107151119">The difficulty of computing stable and accurate neural ... - PNAS</a></li>
<li><a href="https://plato.stanford.edu/entries/goedel-incompleteness/">Gödel’s Incompleteness Theorems - Stanford Encyclopedia of ...</a></li>

</ul>
</details>

**Tags**: `#Gödel`, `#neural networks`, `#limitations`, `#machine learning`, `#philosophy`

---
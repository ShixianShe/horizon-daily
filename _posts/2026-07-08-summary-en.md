---
layout: default
title: "Horizon Summary: 2026-07-08 (EN)"
date: 2026-07-08
lang: en
---

> From 26 items, 17 important content pieces were selected

---

1. [Hidden Admin Backdoor Found in Tenda Router Firmware](#item-1) ⭐️ 9.0/10
2. [MIRA: 5B Parameter Multiplayer World Model for Rocket League](#item-2) ⭐️ 9.0/10
3. [FlashAttention Algebraic Foundation Tutorial Released](#item-3) ⭐️ 9.0/10
4. [MIT SICP Video Lectures (1986) Shared Online](#item-4) ⭐️ 8.0/10
5. [Kokoro: Local, CPU-Friendly High-Quality TTS](#item-5) ⭐️ 8.0/10
6. [EU Chat Control Proposals Explained](#item-6) ⭐️ 8.0/10
7. [OpenAI to Launch GPT-5.6 Sol, Terra, Luna on Thursday](#item-7) ⭐️ 8.0/10
8. [sqlite-utils 4.0 Adds Schema Migrations and More](#item-8) ⭐️ 8.0/10
9. [Ph.D. Thesis on Differentiable Ray Tracing for Radio Propagation](#item-9) ⭐️ 8.0/10
10. [Mozilla CTO Hosts AMA on Open Source AI Report](#item-10) ⭐️ 8.0/10
11. [Constraining Fine-Tuning to Trusted LoRA Subspace](#item-11) ⭐️ 8.0/10
12. [GAO: DOE Prematurely Excludes Cheaper Nuclear Cleanup Options](#item-12) ⭐️ 7.0/10
13. [TorchJD: Jacobian Descent for Multi-Loss Training in PyTorch](#item-13) ⭐️ 7.0/10
14. [LingBot-Depth 2.0: Sensor-validity masking tops 7/8 benchmarks](#item-14) ⭐️ 7.0/10
15. [30papers.com: Ilya's 30 ML Papers in Beginner-Friendly Format](#item-15) ⭐️ 6.0/10
16. [Davit: A Native Swift UI for Apple Containers](#item-16) ⭐️ 6.0/10
17. [New closed-source runtime for k and q languages](#item-17) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Hidden Admin Backdoor Found in Tenda Router Firmware](https://kb.cert.org/vuls/id/213560) ⭐️ 9.0/10

CERT/CC disclosed that multiple versions of Tenda firmware contain an undocumented authentication backdoor (CVE-2026-11405) that grants administrative access to the web management interface without proper credentials. This backdoor affects a wide range of Tenda home and business network devices, potentially allowing attackers to fully compromise routers, switches, and surveillance equipment, leading to network breaches and data theft. The backdoor bypasses the password verification process, and the hidden password for the 'sys.rzadmin.password' field is 'rzadmin', as disclosed in a 2022 writeup. The vulnerability is tracked as CVE-2026-11405.

hackernews · miniBill · Jul 8, 00:08 · [Discussion](https://news.ycombinator.com/item?id=48825749)

**Background**: Tenda is a Chinese manufacturer of networking equipment including routers, switches, and surveillance cameras. Firmware is the low-level software that controls device hardware. An authentication backdoor is a hidden method to bypass normal login procedures, often intentionally inserted for debugging or malicious purposes.

<details><summary>References</summary>
<ul>
<li><a href="https://kb.cert.org/vuls/id/213560">VU#213560 - Tenda firmware (multiple versions) contains hidden authentication backdoor</a></li>
<li><a href="https://thehackernews.com/2026/07/certcc-warns-of-hidden-admin-backdoor.html">CERT/CC Warns of Hidden Admin Backdoor in Tenda Router Firmware</a></li>
<li><a href="https://www.bleepingcomputer.com/news/security/hidden-backdoor-in-tenda-router-firmware-grants-admin-access/">Hidden backdoor in Tenda router firmware grants admin access</a></li>

</ul>
</details>

**Discussion**: Community comments reveal the backdoor password 'rzadmin' and note that Tenda may rebrand products. Some users express distrust of devices manufactured in Shenzhen, while others compare Tenda unfavorably to brands like MikroTik.

**Tags**: `#security`, `#backdoor`, `#firmware`, `#vulnerability`, `#Tenda`

---

<a id="item-2"></a>
## [MIRA: 5B Parameter Multiplayer World Model for Rocket League](https://www.reddit.com/r/MachineLearning/comments/1upofuw/mira_multiplayer_interactive_world_models_trained/) ⭐️ 9.0/10

MIRA is a 5 billion parameter interactive world model trained on 10,000 hours of synthetic Rocket League data, capable of running a full 2v2 match at 20 FPS for four players on a single NVIDIA B200 GPU. The team released a playable online demo, a technical report, and a 1,000-hour dataset of 4-player gameplay. This is the first interactive multiplayer world model for a highly dynamic environment, demonstrating that large-scale world models can simulate complex multi-agent interactions in real time. It opens the door to new applications in game AI, simulation, and robotics where multiple agents must coordinate in a shared environment. MIRA uses a latent diffusion model with diffusion forcing, compressing each frame into a compact latent via a video representation codec. The model scales from 500M to 5B parameters and was trained on 10,000 hours of data, revealing emergent capabilities and characteristic failure modes as size and data increase.

reddit · r/MachineLearning · /u/MasterScrat · Jul 7, 07:59

**Background**: World models are AI systems that learn an internal simulation of an environment, enabling agents to plan and reason without constant real-world interaction. Unlike traditional generative models that only produce outputs, world models simulate dynamics such as physics and object interactions. MIRA builds on prior work like Genie and interactive video world models, but is the first to handle multiple interactive players in real time.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/mira-wm/mira">GitHub - mira-wm/mira: Code for MIRA: Multiplayer Interactive World Models with Representation Autoencoders · GitHub</a></li>
<li><a href="https://mira-wm.com/paper">MIRA Multiplayer Interactive World Models with Representation Autoencoders</a></li>
<li><a href="https://mira-wm.com/blog-post/">MIRA - Blog post</a></li>

</ul>
</details>

**Tags**: `#world models`, `#multiplayer`, `#Rocket League`, `#deep learning`, `#interactive AI`

---

<a id="item-3"></a>
## [FlashAttention Algebraic Foundation Tutorial Released](https://www.reddit.com/r/MachineLearning/comments/1uqcglz/learning_flashattention_the_hard_way_part_1_the/) ⭐️ 9.0/10

A new tutorial series, 'Learning FlashAttention the Hard Way,' has been released, with Part 1 revealing that FlashAttention is an associative operation via a twisted monoid, enabling GPU scheduling optimizations. This algebraic framing simplifies FlashAttention's implementation and optimization, making it accessible to a broader audience and influencing future efficient attention mechanisms in machine learning. The tutorial covers safe softmax, Welford's variance, the twisted monoid, and derives the qk_scale factor log2(e)/√D used in FlashAttention-2 and Triton kernels, along with numerical analysis of overflow bounds and error limits.

reddit · r/MachineLearning · /u/NoVibeCoding · Jul 7, 23:57

**Background**: FlashAttention is a fast and memory-efficient attention mechanism for transformers, originally introduced to reduce the quadratic memory cost of standard attention. Its key insight is tiling the attention computation over blocks, which requires the underlying operation to be associative. This tutorial formalizes that associativity using algebraic structures like twisted monoids, linking it to well-known algorithms like Welford's method for variance.

<details><summary>References</summary>
<ul>
<li><a href="https://softwarebits.substack.com/p/the-one-property-that-makes-flashattention">The One Property That Makes FlashAttention Possible</a></li>
<li><a href="https://courses.cs.washington.edu/courses/cse599m/23sp/notes/flashattn.pdf">From Online Softmax to FlashAttention by Zihao Ye Email: zhye@cs.washington.edu</a></li>
<li><a href="https://en.wikipedia.org/wiki/Algorithms_for_calculating_variance">Algorithms for calculating variance - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#FlashAttention`, `#machine learning`, `#CUDA`, `#algebraic foundations`, `#MLSys`

---

<a id="item-4"></a>
## [MIT SICP Video Lectures (1986) Shared Online](https://ocw.mit.edu/courses/6-001-structure-and-interpretation-of-computer-programs-spring-2005/video_galleries/video-lectures/) ⭐️ 8.0/10

MIT has made the classic 1986 video lectures for Structure and Interpretation of Computer Programs (SICP) available online, featuring Harold Abelson and Gerald Jay Sussman teaching the course. SICP is a foundational computer science resource, and these lectures are highly valued for their pedagogical clarity, making them a timeless tool for learning programming concepts. The lectures use the Scheme programming language, but community members recommend using Racket with the sicp package as a modern alternative for exercises.

hackernews · gjvc · Jul 7, 23:57 · [Discussion](https://news.ycombinator.com/item?id=48825664)

**Background**: SICP, also known as the "Wizard Book," is a classic computer science textbook by Harold Abelson and Gerald Jay Sussman. It uses Scheme, a dialect of Lisp, to teach fundamental programming concepts like abstraction, recursion, and metalinguistic abstraction. The video lectures from 1986 capture the original MIT course and are praised for their engaging presentation.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Structure_and_Interpretation_of_Computer_Programs">Structure and Interpretation of Computer Programs - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Racket_(programming_language)">Racket (programming language)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Scheme_(programming_language)">Scheme (programming language) - Wikipedia The Scheme Programming Language, 4th Edition The Scheme Programming Language - Massachusetts Institute of ... Scheme Documentation Getting Started - scheme Overview - MIT/GNU Scheme 9.2</a></li>

</ul>
</details>

**Discussion**: Community members highly recommend the lectures, with one user stating they are better than reading the book alone. There is discussion about using Racket with the sicp package for exercises, and a question about whether to use the JavaScript or Scheme version of SICP.

**Tags**: `#SICP`, `#computer science education`, `#Scheme`, `#video lectures`, `#programming`

---

<a id="item-5"></a>
## [Kokoro: Local, CPU-Friendly High-Quality TTS](https://ariya.io/2026/03/local-cpu-friendly-high-quality-tts-text-to-speech-with-kokoro/) ⭐️ 8.0/10

Kokoro is an open-weight text-to-speech model with 82 million parameters that runs efficiently on CPU without requiring a GPU, delivering high-quality voice synthesis locally. This makes advanced TTS accessible to users without dedicated GPUs, lowering the barrier for accessibility tools, content creation, and personal use, and promoting local AI inference on common hardware. Kokoro is built on the StyleTTS 2 architecture and supports manual IPA pronunciation guides to correct homograph errors, though it may struggle with single-word utterances.

hackernews · speckx · Jul 7, 18:24 · [Discussion](https://news.ycombinator.com/item?id=48821576)

**Background**: Text-to-speech (TTS) models convert written text into spoken audio. Many high-quality TTS models require powerful GPUs for inference, limiting their use to users with expensive hardware. Kokoro addresses this by being optimized for CPU inference, making it practical for a wider audience.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/hexgrad/kokoro">GitHub - hexgrad/kokoro: https://hf.co/hexgrad/Kokoro-82M · GitHub</a></li>
<li><a href="https://huggingface.co/hexgrad/Kokoro-82M">hexgrad/Kokoro-82M · Hugging Face</a></li>
<li><a href="https://kokorottsai.com/">Kokoro TTS: Advanced AI Text-to-Speech Model with 82M parameters</a></li>

</ul>
</details>

**Discussion**: Community members praised Kokoro for its accessibility and GPU-free operation, with one user integrating it into an accessibility product and another using it for an article reader podcast. Some noted limitations with single-word pronunciation and homograph handling, but overall sentiment was very positive.

**Tags**: `#text-to-speech`, `#machine learning`, `#accessibility`, `#open source`, `#CPU inference`

---

<a id="item-6"></a>
## [EU Chat Control Proposals Explained](https://fightchatcontrol.eu/chat-control-overview) ⭐️ 8.0/10

The EU's Chat Control 1.0 expired on April 3, 2026, ending the legal basis for voluntary scanning of private messages, while negotiations for Chat Control 2.0 continue, which would mandate scanning for CSAM. These proposals threaten end-to-end encryption and mass surveillance of all private communications, affecting millions of users and raising fundamental privacy and digital rights concerns. Chat Control 1.0 allowed voluntary scanning under a temporary derogation from the ePrivacy Directive; Chat Control 2.0 would make scanning mandatory. Despite the expiry, major platforms like Google and Meta stated they will continue scanning.

hackernews · gasull · Jul 7, 14:23 · [Discussion](https://news.ycombinator.com/item?id=48818311)

**Background**: Chat Control refers to EU regulations aimed at combating child sexual abuse material (CSAM) by requiring digital platforms to scan private messages. Critics argue this undermines end-to-end encryption and violates privacy rights. The proposals have sparked significant debate between child protection advocates and digital rights groups.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Chat_Control">Chat Control - Wikipedia</a></li>
<li><a href="https://fightchatcontrol.eu/chat-control-overview">Chat Control 1.0 vs 2.0 - Fight Chat Control</a></li>
<li><a href="https://stateofsurveillance.org/news/eu-chat-control-expires-april-3-scanning-ends-whats-next-2026/">Chat Control Is Dead. Long Live Chat Control. - State of ...</a></li>

</ul>
</details>

**Discussion**: Commenters express strong opposition, viewing the proposals as a surveillance overreach that threatens encryption and privacy. Some question how scanning would work with E2EE, while others note that despite the expiry of Chat Control 1.0, companies continue scanning voluntarily.

**Tags**: `#privacy`, `#encryption`, `#surveillance`, `#EU regulation`, `#digital rights`

---

<a id="item-7"></a>
## [OpenAI to Launch GPT-5.6 Sol, Terra, Luna on Thursday](https://twitter.com/OpenAI/status/2074704958419792299) ⭐️ 8.0/10

OpenAI announced that GPT-5.6 Sol, along with Terra and Luna, will launch publicly this Thursday, July 9, 2026, expanding from a limited preview to global availability. This release introduces a tri-model architecture that offers different capability and cost tiers, potentially reshaping competition with Claude models and making advanced AI more accessible. Sol is the flagship model for frontier reasoning and long-horizon agentic work, Terra offers balanced performance at 2x lower cost than GPT-5.5, and Luna is the fastest, most affordable option.

hackernews · jfrbfbreudh · Jul 8, 04:12 · [Discussion](https://news.ycombinator.com/item?id=48827402)

**Background**: GPT-5.6 is a limited preview family from OpenAI, with Sol, Terra, and Luna representing different tiers. Early access reports highlight Sol's strong capabilities in coding, science, and cybersecurity, with improved efficiency and speed compared to previous GPT models.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/previewing-gpt-5-6-sol/">Previewing GPT‑5.6 Sol: a next-generation model - OpenAI</a></li>
<li><a href="https://help.openai.com/en/articles/20001325-a-preview-of-gpt-56-sol-terra-and-luna">A preview of GPT-5.6 Sol, Terra, and Luna - OpenAI Help Center</a></li>
<li><a href="https://www.explainx.ai/blog/gpt-5-6-release-date-features-benchmarks-2026">GPT-5.6: Public Launch July 9 — Sol, Terra, Luna - explainx.ai</a></li>

</ul>
</details>

**Discussion**: Community members expressed excitement about the launch, with some praising GPT models for being faster and cheaper than Claude models. Others noted they might switch back from Claude if Sol proves comparable to Fable, and some speculated that Anthropic's extension of Fable 5 access was a response to this release.

**Tags**: `#AI`, `#LLM`, `#OpenAI`, `#GPT-5.6`, `#model release`

---

<a id="item-8"></a>
## [sqlite-utils 4.0 Adds Schema Migrations and More](https://simonwillison.net/2026/Jul/7/sqlite-utils-4/#atom-everything) ⭐️ 8.0/10

sqlite-utils 4.0, the first major version bump since 3.0 in November 2020, introduces database schema migrations, nested transactions via a new db.atomic() method, and support for compound foreign keys. This release significantly enhances sqlite-utils as a tool for managing SQLite databases, providing built-in migration capabilities that previously required external libraries, and enabling more complex schema changes and transaction handling. Migrations are defined in Python files using the Migrations class and the table.transform() method, which implements SQLite's recommended pattern of creating a new table, copying data, and renaming. The upgrade guide details breaking changes for users of previous versions.

rss · Simon Willison · Jul 7, 19:32

**Background**: sqlite-utils is a Python CLI utility and library for manipulating SQLite databases, widely used for tasks like importing data, running queries, and transforming tables. Schema migrations allow developers to version-control and apply incremental changes to database schemas, a feature SQLite's ALTER TABLE alone cannot fully support.

<details><summary>References</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Jul/7/sqlite-utils-4/">sqlite-utils 4.0, now with database schema migrations</a></li>
<li><a href="https://sqlite-utils.datasette.io/en/latest/migrations.html">Database migrations - sqlite-utils</a></li>
<li><a href="https://github.com/simonw/sqlite-utils">GitHub - simonw/sqlite-utils: Python CLI utility and library ... Managing Database Versions and Migrations in SQLite sqlite-utils 4.0rc1 adds migrations and nested transactions SQLite Versioning & Migration Strategies for Evolving Apps sqlite-utils 4.0, now with database schema migrations #Shorts</a></li>

</ul>
</details>

**Tags**: `#sqlite`, `#database`, `#python`, `#migrations`, `#open-source`

---

<a id="item-9"></a>
## [Ph.D. Thesis on Differentiable Ray Tracing for Radio Propagation](https://www.reddit.com/r/MachineLearning/comments/1upvkp5/phd_thesis_on_differentiable_ray_tracing_for/) ⭐️ 8.0/10

A Ph.D. thesis titled 'Differentiable Ray Tracing for Radio Propagation Modeling' has been published, presenting a self-contained textbook that integrates automatic differentiation with ray tracing for wireless communications. This work bridges physics simulation and machine learning, enabling gradient-based optimization and inverse problems in radio propagation, which is crucial for next-generation wireless system design. The thesis is split into three parts: physics fundamentals, algorithmic core with GPU-accelerated path tracing and discontinuity smoothing, and practical applications like channel modeling and material calibration. It heavily relies on JAX and its ecosystem (jaxtyping, equinox, optimistix).

reddit · r/MachineLearning · /u/jeertmans · Jul 7, 13:45

**Background**: Differentiable ray tracing combines automatic differentiation with ray tracing to compute gradients through physical simulations. Radio propagation modeling predicts how radio waves travel, which is essential for wireless network planning. Traditional models are empirical, but differentiable simulation allows direct integration with machine learning for optimization.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/jeertmans/DiffeRT2d">GitHub - jeertmans/DiffeRT2d: 2D Toolbox for Differentiable ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Radio_propagation">Radio propagation - Wikipedia</a></li>
<li><a href="https://www.emergentmind.com/topics/differentiable-simulation-and-automatic-differentiation">Differentiable Simulation & Automatic Differentiation</a></li>

</ul>
</details>

**Discussion**: The Reddit community responded positively, with the author actively answering questions about differentiable simulation and JAX-based ray tracing. Users praised the textbook-style presentation and the open-source libraries like DiffeRT.

**Tags**: `#differentiable ray tracing`, `#radio propagation`, `#automatic differentiation`, `#machine learning`, `#wireless communications`

---

<a id="item-10"></a>
## [Mozilla CTO Hosts AMA on Open Source AI Report](https://www.reddit.com/r/MachineLearning/comments/1upxdvc/raffi_krikorian_cto_mozilla_ama_on_the_state_of/) ⭐️ 8.0/10

Mozilla CTO Raffi Krikorian will host an AMA on July 14, 2025, to discuss the inaugural State of Open Source AI report, covering real-world costs, enterprise adoption, China's influence, and developer trust. This AMA provides a rare opportunity to hear directly from a major foundation's CTO about the practical challenges and strategic shifts in open source AI, which affects developers, enterprises, and the broader ecosystem. The report is based on a survey of over 950 developers and explores topics like the hidden costs of 'free' models, the real state of enterprise adoption, the impact of Chinese AI models, and the concept of an 'agentic harness' as the new battleground.

reddit · r/MachineLearning · /u/raffikrikorian · Jul 7, 14:51

**Background**: Open source AI refers to AI models and tools whose source code is publicly available for use, modification, and distribution. The 'agentic harness' is the infrastructure layer that manages an AI model's lifecycle, tool access, and safety in production, which is becoming a key area of competition beyond the model itself.

<details><summary>References</summary>
<ul>
<li><a href="https://www.mozilla.org/en-US/foundation/annualreport/2024/article/evolving-together-redefining-mozilla-in-the-ai-era/">Evolving Together: Redefining Mozilla in the AI Era</a></li>
<li><a href="https://harness-engineering.ai/blog/agent-harness-complete-guide/">The Complete Guide to Agent Harness: What It Is and Why It ...</a></li>

</ul>
</details>

**Tags**: `#open source`, `#AI`, `#Mozilla`, `#enterprise`, `#developer trust`

---

<a id="item-11"></a>
## [Constraining Fine-Tuning to Trusted LoRA Subspace](https://www.reddit.com/r/MachineLearning/comments/1uq68li/what_if_a_model_could_only_learn_what_trusted/) ⭐️ 8.0/10

A new paper proposes constraining fine-tuning to a subspace learned from trusted LoRA adapters, preventing the model from learning malicious updates that fall outside this subspace. This approach offers a novel defense against fine-tuning poisoning attacks, which are a critical security threat for large language models, by geometrically restricting what the model can learn rather than detecting malicious data. The method was tested on 196 public LoRA adapters, including adaptive attacks designed to bypass the defense, and showed sharp drops in attack success while preserving useful adaptation on tasks covered by the adapter pool.

reddit · r/MachineLearning · /u/Bright_Warning_8406 · Jul 7, 20:00

**Background**: LoRA (Low-Rank Adaptation) is a parameter-efficient fine-tuning technique that trains small weight matrices while freezing the base model. Fine-tuning poisoning attacks inject malicious data to cause the model to learn hidden backdoors or undesirable behaviors. Existing defenses typically focus on detecting poisoned data or reducing its impact, but this work takes a different approach by constraining the update space.

<details><summary>References</summary>
<ul>
<li><a href="https://www.geeksforgeeks.org/deep-learning/low-rank-adaptation-lora/">Low Rank Adaptation (LoRA) - GeeksforGeeks</a></li>
<li><a href="https://arxiv.org/html/2402.12168v2">Defending Against Weight-Poisoning Backdoor Attacks for ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Multilinear_subspace_learning">Multilinear subspace learning - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#machine learning`, `#security`, `#LoRA`, `#fine-tuning`, `#poisoning defense`

---

<a id="item-12"></a>
## [GAO: DOE Prematurely Excludes Cheaper Nuclear Cleanup Options](https://www.gao.gov/products/gao-26-108193) ⭐️ 7.0/10

A new GAO report (GAO-26-108193) criticizes the Department of Energy for prematurely excluding less expensive cleanup options, potentially wasting billions of taxpayer dollars. This report highlights systemic planning flaws that could lead to significant cost overruns in nuclear waste cleanup, a mission that already costs billions annually. The findings could push DOE to adopt more cost-effective approaches and improve accountability. The report notes that DOE often identifies a need with a particular solution already in mind, rather than evaluating a range of alternatives. GAO recommends that DOE align its planning with leading practices to ensure cost-effectiveness.

hackernews · Jimmc414 · Jul 7, 22:23 · [Discussion](https://news.ycombinator.com/item?id=48824826)

**Background**: The Department of Energy (DOE) is responsible for cleaning up nuclear waste from decades of weapons production and research. This involves decontaminating facilities, remediating soil and groundwater, and disposing of various types of radioactive waste. GAO reports have repeatedly flagged cost and schedule issues in DOE's cleanup projects.

<details><summary>References</summary>
<ul>
<li><a href="https://www.gao.gov/products/gao-26-108193">Nuclear Waste Cleanup: Changes Needed to Ensure DOE Is Not ...</a></li>
<li><a href="https://www.energy.gov/environmental-cleanup">Environmental Cleanup - Department of Energy</a></li>
<li><a href="https://www.gao.gov/products/gao-24-105975">Nuclear Waste Cleanup: Closer Alignment with Leading ...</a></li>

</ul>
</details>

**Discussion**: Commenters praised the GAO report for its clear communication and actionable recommendations. One user noted it as an excellent example of how to present investigation findings, while another humorously called nuclear cleanup a future $100 billion industry.

**Tags**: `#nuclear cleanup`, `#government accountability`, `#cost efficiency`, `#policy`

---

<a id="item-13"></a>
## [TorchJD: Jacobian Descent for Multi-Loss Training in PyTorch](https://www.reddit.com/r/MachineLearning/comments/1upzxk2/torchjd_training_with_multiple_losses_in_pytorch_p/) ⭐️ 7.0/10

TorchJD, a library implementing Jacobian descent methods for training with multiple losses, has been accepted into the PyTorch ecosystem and now includes most existing aggregation methods from the literature. This provides a practical alternative to scalarization for multi-task learning, enabling models to decrease all losses simultaneously rather than just the average, which can improve performance when objectives conflict. TorchJD supports both scalarization and Jacobian descent methods, allowing users to switch between them with minimal code changes. The library is in beta (0.x.y) and follows semantic versioning.

reddit · r/MachineLearning · /u/Skeylos2 · Jul 7, 16:20

**Background**: In multi-task learning, models are trained with multiple loss functions. Traditional scalarization combines losses into a single weighted sum, which can be suboptimal when gradients conflict. Jacobian descent computes the Jacobian matrix of all losses and aggregates gradients to decrease each loss individually, offering a more principled approach.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2406.16232">[2406.16232] Jacobian Descent for Multi-Objective Optimization Understanding the Jacobian – A Beginner’s Guide with 2D & 3D ... TorchJD Jacobian Descent: Optimizing Vector Objectives GitHub - SimplexLab/TorchJD: Library for Jacobian descent ... JACOBIAN DESCENT FOR MULTI-OBJECTIVE OPTIMIZATION</a></li>
<li><a href="https://torchjd.org/stable/index.html">TorchJD</a></li>
<li><a href="https://pypi.org/project/torchjd/">torchjd · PyPI</a></li>

</ul>
</details>

**Tags**: `#PyTorch`, `#multi-task learning`, `#Jacobian descent`, `#loss aggregation`, `#machine learning`

---

<a id="item-14"></a>
## [LingBot-Depth 2.0: Sensor-validity masking tops 7/8 benchmarks](https://www.reddit.com/r/MachineLearning/comments/1upqghy/masked_depth_modeling_with_sensorvalidity_masking/) ⭐️ 7.0/10

LingBot-Depth 2.0 introduces sensor-validity masking for depth completion, achieving best RMSE on 7 of 8 masked/sparse depth benchmarks and 6 of 8 real camera configurations. The paper also presents a controlled encoder initialization study showing that the LingBot-Vision backbone outperforms DINOv2 on most benchmarks. This work demonstrates that using sensor-invalid regions as natural training targets significantly improves depth completion, especially on challenging transparent and reflective surfaces. The approach could enhance robotic perception and embodied AI systems by making them more robust to real-world sensor failures. The model uses a Vision Transformer encoder with depth-aware attention mechanisms, and only the encoder initialization and data scale differ from version 1.0. Weights for LingBot-Depth 2.0 are not released, but four Vision backbones are open-source under Apache-2.0 at https://github.com/robbyant/lingbot-vision.

reddit · r/MachineLearning · /u/Ok-Line2658 · Jul 7, 09:54

**Background**: Depth completion aims to fill missing or invalid depth values from RGB-D sensors, which often fail on specular, transparent, or textureless surfaces. Masked depth modeling (MDM) treats these missing regions as natural masks for self-supervised learning. LingBot-Depth 2.0 is developed by Robbyant, an embodied AI company under Ant Group.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2601.17895">[2601.17895] Masked Depth Modeling for Spatial Perception Images GitHub - Robbyant/lingbot-vision: Self-supervised learning ... Masked Depth Modeling for Spatial Perception (PDF) Masked Depth Modeling for Spatial Perception - ResearchGate Masked Depth Modeling Techniques - emergentmind.com</a></li>
<li><a href="https://github.com/Robbyant/lingbot-depth">GitHub - Robbyant/lingbot-depth: Masked Depth Modeling for ...</a></li>
<li><a href="https://github.com/Robbyant/lingbot-vision">GitHub - Robbyant/lingbot-vision: Self-supervised learning ...</a></li>

</ul>
</details>

**Discussion**: The Reddit discussion is substantive, with users asking whether sensor-validity masking generalizes to other modalities like LiDAR or thermal. The author responds that it's an open question and invites further research. Overall sentiment is positive, with appreciation for the clean ablation study.

**Tags**: `#depth estimation`, `#masked modeling`, `#computer vision`, `#self-supervised learning`, `#embodied AI`

---

<a id="item-15"></a>
## [30papers.com: Ilya's 30 ML Papers in Beginner-Friendly Format](https://30papers.com/) ⭐️ 6.0/10

A website called 30papers.com has been launched, presenting a list of 30 essential machine learning papers attributed to Ilya Sutskever in a beginner-friendly format with explanations and toggles for animations. This curated list could help newcomers navigate the vast ML literature, but the unverified origin and usability issues raise concerns about its reliability and accessibility. The site includes toggles to reduce motion and background intensity, addressing complaints about distracting animations. The list's origin is an unverified X post claiming Ilya gave the list to John Carmack.

hackernews · notmcrowley · Jul 7, 15:58 · [Discussion](https://news.ycombinator.com/item?id=48819608)

**Background**: Ilya Sutskever is a co-founder of OpenAI and a prominent figure in deep learning, known for contributions to sequence-to-sequence learning and GPT models. The list of 30 papers is rumored to be his recommended reading for understanding modern ML, but its authenticity has not been confirmed by Sutskever or Carmack.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Ilya_Sutskever">Ilya Sutskever - Wikipedia</a></li>
<li><a href="https://github.com/dzyim/ilya-sutskever-recommended-reading">dzyim/ilya-sutskever-recommended-reading - GitHub</a></li>
<li><a href="https://rottenpanda.com/science-nature/30papers-com-ilya-s-30-essential-ml-papers-in-a-beginner-friendly-format/">30Papers.com – Ilya's 30 Essential ML Papers, In A Beginner ...</a></li>

</ul>
</details>

**Discussion**: Community comments express skepticism about the list's authenticity, with one user noting the lack of source and connection to Ilya or Carmack. The author, a first-year CS student, acknowledged usability flaws and added toggles for animations. Some users suggested organizing papers in a logical reading order.

**Tags**: `#machine learning`, `#research papers`, `#education`, `#curation`

---

<a id="item-16"></a>
## [Davit: A Native Swift UI for Apple Containers](https://davit.app/) ⭐️ 6.0/10

Davit is a native macOS app built with Swift that provides a graphical user interface for Apple Containers, Apple's open-source container runtime for macOS. It was developed in just 3 days with heavy AI assistance (28 commits, all co-authored by Claude Fable 5) and is only 17 MB in size. Davit offers a lightweight, native alternative to Orbstack for managing Apple Containers, appealing to developers who prefer a GUI over command-line tools. Its small size and use of native APIs demonstrate that high-quality container management tools can be built without Electron or web views. The app uses Apple's ContainerAPIClient library directly and is signed and notarized for macOS. On first launch, it automatically downloads the necessary container platform components. The source code is available on GitHub.

hackernews · xinit · Jul 7, 18:44 · [Discussion](https://news.ycombinator.com/item?id=48821848)

**Background**: Apple Containers is an open-source command-line tool introduced by Apple in 2025 that runs Linux containers on macOS using a one-VM-per-container architecture for improved security. Orbstack is a popular commercial alternative to Docker Desktop for macOS, known for its speed and integration. 'Vibe coding' refers to AI-assisted software development where the developer describes the project in natural language and the AI generates most of the code.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Apple_container">Apple container</a></li>
<li><a href="https://opensource.apple.com/projects/container/">Apple Open Source</a></li>
<li><a href="https://en.wikipedia.org/wiki/Vibe_coded">Vibe coded</a></li>

</ul>
</details>

**Discussion**: The community response is largely positive, with users praising the app's quality, small size, and native approach. Some users expressed interest in features like choosing which terminal app containers open in, and one user noted they would try it as an alternative to Orbstack.

**Tags**: `#Apple Containers`, `#macOS`, `#Docker`, `#Swift`, `#Developer Tools`

---

<a id="item-17"></a>
## [New closed-source runtime for k and q languages](https://lv1.sh/) ⭐️ 6.0/10

A new closed-source runtime called 'l' has been released for the array programming languages k and q, as announced on lv1.sh. The runtime is described as 'vibecoded' and is not open source. This runtime explores a niche design space in array programming, potentially offering new performance or features for k and q users. However, its closed-source nature limits adoption and trust, especially in a community that values openness. The runtime is closed-source and its website is described as 'vibecoded', which reduces credibility. It claims to benchmark well, but no direct comparisons with existing k runtimes are provided.

hackernews · skruger · Jul 7, 18:08 · [Discussion](https://news.ycombinator.com/item?id=48821378)

**Background**: K and q are array programming languages developed by Arthur Whitney, used primarily for high-performance data analysis and time-series databases like kdb+. They are known for their terse syntax and speed, but many implementations are proprietary. Open-source alternatives like Klong and BQN exist.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/K_(programming_language)">K (programming language) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Q_(programming_language_from_Kx_Systems)">Q (programming language from Kx Systems) - Wikipedia</a></li>
<li><a href="https://code.kx.com/q/">Developing with kdb+ and the q language - kdb+ and q ...</a></li>

</ul>
</details>

**Discussion**: Community comments are mixed: some see the design space as interesting and encourage more experimentation, while others criticize the closed-source and 'vibecoded' nature as a non-starter. Comparisons to existing runtimes are requested, and proprietary licensing is noted as common in the APL/K family.

**Tags**: `#k`, `#q`, `#runtime`, `#array programming`, `#APL`

---
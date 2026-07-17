---
layout: default
title: "Horizon Summary: 2026-07-17 (EN)"
date: 2026-07-17
lang: en
---

> From 27 items, 20 important content pieces were selected

---

1. [Firefox Runs Inside Another Browser via WebAssembly](#item-1) ⭐️ 9.0/10
2. [Kimi K3: Open-Weight Frontier Model with 1M Context](#item-2) ⭐️ 8.0/10
3. [LM Studio Launches Bionic AI Agent for Open Models](#item-3) ⭐️ 8.0/10
4. [Rust-to-Zig Compiler Rewrite: A Detailed Account](#item-4) ⭐️ 8.0/10
5. [GPT-5.6 Codex Bug Can Accidentally Delete Files](#item-5) ⭐️ 8.0/10
6. [Thinking Machines Lab Releases Inkling Open-Weights Model](#item-6) ⭐️ 8.0/10
7. [Linus Torvalds: Linux Is Not Anti-AI](#item-7) ⭐️ 8.0/10
8. [ExTernD: Ternary LLM Quantization with Expanded-Rank Decomposition](#item-8) ⭐️ 8.0/10
9. [PnP-CoSMo: Multi-Contrast MRI Reconstruction via Content/Style Modeling](#item-9) ⭐️ 8.0/10
10. [Schema Harness Achieves 99% on ARC-AGI-3 Public Set](#item-10) ⭐️ 8.0/10
11. [New Book on Mathematics of Data Science Released](#item-11) ⭐️ 7.0/10
12. [Classical ML for LLM Detection](#item-12) ⭐️ 7.0/10
13. [Interactive Linear Algebra Book from 2015 Still Inspires](#item-13) ⭐️ 7.0/10
14. [DABSN: New Recurrent LM Seeks Collaborators for Scaling](#item-14) ⭐️ 7.0/10
15. [QLoRA Default Learning Rate 2e-4 Fails on Small Datasets](#item-15) ⭐️ 7.0/10
16. [Rethinking AI Memory: From Facts to Reasoning Patterns](#item-16) ⭐️ 7.0/10
17. [Microsoft Open-Sources 1990s IRC Client Comic Chat](#item-17) ⭐️ 6.0/10
18. [Decoy Font Tricks AI with Hidden Text](#item-18) ⭐️ 6.0/10
19. [Offset Data Center Water Use by Converting Golf Courses](#item-19) ⭐️ 6.0/10
20. [Mermaid Diagrams Converted to Color ASCII Art via WebAssembly](#item-20) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Firefox Runs Inside Another Browser via WebAssembly](https://simonwillison.net/2026/Jul/16/firefox-in-webassembly/#atom-everything) ⭐️ 9.0/10

Puter has compiled the entire Firefox browser (Gecko engine) to WebAssembly, allowing it to run inside another browser. The project uses the Wisp protocol to proxy all network traffic through Puter's server. This is a groundbreaking technical achievement that demonstrates the power of WebAssembly to run complex, native applications in the browser. It opens up possibilities for cross-browser testing, legacy browser access, and new forms of web-based computing. The compiled Firefox binary includes a 233MB gecko.wasm file and an 18MB chrome-assets archive. The project cost an estimated $25,000 in AI tokens (Claude Opus and Fable) but used a subscription plan to reduce actual expenses.

rss · Simon Willison · Jul 16, 23:34

**Background**: WebAssembly (Wasm) is a low-level binary instruction format that runs in modern browsers at near-native speed. The Wisp protocol is a WebSocket-based protocol that enables network communication for WebAssembly applications, which cannot open raw TCP connections due to browser security restrictions.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/HeyPuter/firefox-wasm">GitHub - HeyPuter/ firefox -wasm: Firefox in WebAssembly · GitHub</a></li>
<li><a href="https://news.ycombinator.com/item?id=48926939">Show HN: Firefox in WebAssembly | Hacker News</a></li>
<li><a href="https://simonwillison.net/2026/Jul/16/firefox-in-webassembly/">Firefox in WebAssembly</a></li>

</ul>
</details>

**Discussion**: The Hacker News discussion was highly positive, with many impressed by the engineering effort. Some commenters noted the high server costs for proxying traffic, and the team confirmed they had to scale up servers to handle the traffic spike.

**Tags**: `#WebAssembly`, `#Firefox`, `#browser`, `#compilation`, `#Wisp`

---

<a id="item-2"></a>
## [Kimi K3: Open-Weight Frontier Model with 1M Context](https://www.kimi.com/blog/kimi-k3) ⭐️ 8.0/10

Moonshot AI released Kimi K3, an open-weight frontier model with 2.8 trillion parameters and a 1M-token context window, claiming competitive performance with Anthropic's Sonnet series at similar pricing. This release marks a significant step in commoditizing frontier AI, as a Chinese lab offers a powerful open-weight model that challenges US dominance and lowers barriers for developers and enterprises. Kimi K3 uses Kimi Delta Attention (KDA), a hybrid linear attention mechanism, and Attention Residuals, with native visual understanding. Pricing is $3/$15 per 1M tokens (input/output), matching Anthropic's Sonnet rates.

hackernews · vincent_s · Jul 16, 14:46 · [Discussion](https://news.ycombinator.com/item?id=48935342)

**Background**: Open-weight models allow anyone to download and run the model on their own infrastructure, democratizing access to AI. A 1M-token context window can hold entire codebases or long documents, enabling tasks like code review without retrieval augmentation.

<details><summary>References</summary>
<ul>
<li><a href="https://platform.kimi.ai/">Kimi API Platform</a></li>
<li><a href="https://platform.kimi.ai/docs/guide/kimi-k3-quickstart">Kimi K3 - Kimi API Platform</a></li>
<li><a href="https://kie.ai/blog/what-is-kimi-k3">What Is Kimi K3? Moonshot's 2.8T, 1M-Context Flagship</a></li>

</ul>
</details>

**Discussion**: Community comments highlight the model's massive size (2.8T parameters) and high pricing, with some seeing it as commoditization of intelligence by Chinese labs. Others note the cost is justified if performance truly matches frontier models like Sonnet.

**Tags**: `#AI`, `#LLM`, `#open-weight`, `#Chinese AI`, `#frontier model`

---

<a id="item-3"></a>
## [LM Studio Launches Bionic AI Agent for Open Models](https://lmstudio.ai/blog/introducing-lm-studio-bionic) ⭐️ 8.0/10

LM Studio has launched Bionic, a new AI agent app for macOS that uses open models to perform coding, research, and document manipulation tasks, either locally or via cloud-hosted open-source models. Bionic brings agentic capabilities to open models, offering a privacy-focused alternative to proprietary AI agents, which could accelerate adoption of local AI for real-world tasks among developers and enterprises. Bionic supports two project types: 'Code' for coding and 'Work' for document creation/manipulation with automatic checkpointing. It integrates with LM Studio's existing model library and offers a zero data retention policy.

hackernews · minimaxir · Jul 16, 20:18 · [Discussion](https://news.ycombinator.com/item?id=48939662)

**Background**: LM Studio is a popular desktop application for running local large language models (LLMs) on consumer hardware. Bionic extends this by adding agentic capabilities—autonomous task execution—using open models, competing with tools like OpenAI's Codex or Anthropic's Claude.

<details><summary>References</summary>
<ul>
<li><a href="https://lmstudio.ai/blog/introducing-lm-studio-bionic">Introducing LM Studio Bionic: the AI agent for open models</a></li>
<li><a href="https://9to5mac.com/2026/07/16/lm-studio-expands-beyond-chat-with-bionic-a-new-ai-agent-app-for-open-models/">LM Studio launches Bionic, a new AI agent app for open models</a></li>
<li><a href="https://aitoolly.com/ai-news/article/2026-07-17-lm-studio-launches-bionic-a-privacy-focused-ai-agent-designed-for-open-source-model-workflows">LM Studio Bionic: Privacy-First AI Agent for Open Models | AIToolly</a></li>

</ul>
</details>

**Discussion**: Community feedback is largely positive, with users praising the familiar UI and effective local model integration. Some users noted rough edges like directory restrictions and lack of SSH support, while the founder actively engaged by offering free credits for testing.

**Tags**: `#AI agents`, `#local LLMs`, `#open source`, `#LM Studio`, `#developer tools`

---

<a id="item-4"></a>
## [Rust-to-Zig Compiler Rewrite: A Detailed Account](https://rtfeldman.com/rust-to-zig) ⭐️ 8.0/10

The author details their experience rewriting a compiler from Rust to Zig, highlighting Zig's memory control and safety features. This post sparks debate on the necessity of unsafe code in compilers and showcases Zig as a viable alternative for systems programming, potentially influencing language choices for performance-critical projects. The rewrite focuses on Zig's incremental builds and memory control, though community comments question whether unsafe code is truly required for typical compilation tasks.

hackernews · jorangreef · Jul 16, 11:39 · [Discussion](https://news.ycombinator.com/item?id=48933149)

**Background**: Rust and Zig are modern systems programming languages. Rust emphasizes memory safety without garbage collection, while Zig offers manual memory management with safety checks. Compilers often need low-level control, leading to debates about unsafe code usage.

<details><summary>References</summary>
<ul>
<li><a href="https://pedropark99.github.io/zig-book/Chapters/01-memory.html">3 Memory and Allocators – Introduction to Zig - GitHub Pages</a></li>
<li><a href="https://www.scattered-thoughts.net/writing/how-safe-is-zig/">How (memory) safe is zig?</a></li>

</ul>
</details>

**Discussion**: Steveklabnik argues that emitting machine code does not inherently require unsafe code, contrary to the post's claim. Landr0id questions Zig's ability to catch use-after-free errors. Others praise Zig's incremental builds but wonder if Rust will adopt similar features soon.

**Tags**: `#Rust`, `#Zig`, `#compilers`, `#memory safety`, `#programming languages`

---

<a id="item-5"></a>
## [GPT-5.6 Codex Bug Can Accidentally Delete Files](https://simonwillison.net/2026/Jul/16/bad-codex-bug/#atom-everything) ⭐️ 8.0/10

A bug in GPT-5.6 Codex can cause accidental file deletions when full access mode is enabled without sandboxing, due to the model mishandling the $HOME environment variable. This bug highlights critical safety concerns for AI coding agents that have file system access, as even a well-intentioned model can make a catastrophic mistake. Developers using such tools must implement sandboxing and review mechanisms to prevent data loss. The bug occurs when Codex attempts to override $HOME to define a temporary directory but mistakenly deletes $HOME instead. OpenAI has investigated the issue and confirmed it happens most often without sandboxing or auto-review enabled.

rss · Simon Willison · Jul 16, 17:45

**Background**: GPT-5.6 Codex is an AI coding agent from OpenAI that can autonomously read, write, and execute code, including running shell commands. The $HOME environment variable points to the user's home directory, which contains critical personal files. Sandboxing isolates the agent's actions to prevent harm to the host system.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GPT-5.3-Codex">GPT-5.3-Codex</a></li>
<li><a href="https://amux.io/guides/ai-agent-sandboxing/">AI Agent Sandboxing in 2026: Docker, E2B, Firecracker... — amux</a></li>

</ul>
</details>

**Tags**: `#codex`, `#coding-agents`, `#generative-ai`, `#ai-safety`, `#bug`

---

<a id="item-6"></a>
## [Thinking Machines Lab Releases Inkling Open-Weights Model](https://simonwillison.net/2026/Jul/16/inkling/#atom-everything) ⭐️ 8.0/10

Mira Murati's Thinking Machines Lab released Inkling, an open-weights Mixture-of-Experts multimodal model with 975B total parameters (41B active), licensed under Apache-2.0 and trained on 45 trillion tokens of text, images, audio, and video. This release strengthens the US open-weights ecosystem, providing a competitive alternative to models from China and other labs, and offers a strong base for fine-tuning via the Tinker platform. Inkling is not a frontier model but a strong base for customization; the model card and training data documentation are notably sparse, with vague descriptions of data sources.

rss · Simon Willison · Jul 16, 15:35

**Background**: Mixture-of-Experts (MoE) models use multiple specialized sub-networks (experts) and activate only a subset per input, enabling larger total parameters with lower computational cost. Open-weights models release trained parameters publicly, allowing anyone to download and use them. Apache-2.0 is a permissive license that permits free use, modification, and distribution.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>
<li><a href="https://opensource.org/ai/open-weights">Open Weights: not quite what you’ve been told</a></li>
<li><a href="https://en.wikipedia.org/wiki/Apache_License">Apache License</a></li>

</ul>
</details>

**Tags**: `#AI`, `#open-weights`, `#Mixture-of-Experts`, `#multimodal`, `#Thinking Machines Lab`

---

<a id="item-7"></a>
## [Linus Torvalds: Linux Is Not Anti-AI](https://simonwillison.net/2026/Jul/16/linus-torvalds/#atom-everything) ⭐️ 8.0/10

Linus Torvalds, the creator of Linux, explicitly stated that Linux is not an anti-AI project and that AI is a clearly useful tool, warning that those who disagree can fork the project or leave. This strong endorsement from the top Linux maintainer signals a definitive shift in the project's stance on AI, potentially influencing the broader open-source community and encouraging AI integration in kernel development. Torvalds made the remarks on the Linux Media Mailing List, emphasizing that while questions about AI's economy remain, its usefulness is no longer in question, and anyone who doubts it clearly hasn't used it.

rss · Simon Willison · Jul 16, 13:26

**Background**: Linus Torvalds is the creator and lead maintainer of the Linux kernel, one of the largest open-source projects. The Linux community has historically had diverse opinions on AI, with some members expressing concerns about its impact on open-source values and code quality. Torvalds' statement directly addresses this internal debate, asserting his authority as maintainer.

**Tags**: `#Linux`, `#AI`, `#Linus Torvalds`, `#open source`, `#kernel development`

---

<a id="item-8"></a>
## [ExTernD: Ternary LLM Quantization with Expanded-Rank Decomposition](https://www.reddit.com/r/MachineLearning/comments/1uy2zb3/externd_expandedrank_ternary_decomposition/) ⭐️ 8.0/10

ExTernD proposes a post-training quantization method that decomposes each LLM weight matrix into two ternary matrices and a diagonal scaling matrix, allowing the inner rank to be arbitrarily large to achieve accuracy approaching any quantization level. This approach overcomes the fixed matrix size limitation of previous ternary quantization methods, potentially enabling high-accuracy LLM compression with only modest VRAM overhead, which is critical for deploying large models on resource-constrained devices. The inner rank k is a free parameter; larger k yields higher accuracy but increases VRAM usage. The method claims to use only slightly more VRAM than current quantization methods while leveraging efficient ternary arithmetic.

reddit · r/MachineLearning · /u/LMTLS5 · Jul 16, 13:31

**Background**: Post-training quantization (PTQ) reduces model size and speeds up inference by converting weights to lower precision without retraining. Ternary quantization uses values -1, 0, +1, enabling multiplication-free computation via additions and subtractions. Previous ternary methods were limited by fixed matrix size, which constrained accuracy.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2607.13511">ExTernD : Expanded-Rank Ternary Decomposition Ternary LLM PTQ...</a></li>
<li><a href="https://arxiv.org/html/2607.13511">ExTernD: Expanded-Rank Ternary Decomposition Ternary LLM PTQ...</a></li>
<li><a href="https://github.com/phiennd/td">GitHub - phiennd/td: A complete stack to run AI models in ternary ...</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#quantization`, `#ternary`, `#model compression`, `#PTQ`

---

<a id="item-9"></a>
## [PnP-CoSMo: Multi-Contrast MRI Reconstruction via Content/Style Modeling](https://www.reddit.com/r/MachineLearning/comments/1uy2h66/pnpcosmo_a_multicontrast_mri_reconstruction/) ⭐️ 8.0/10

PnP-CoSMo is a plug-and-play framework for multi-contrast MRI reconstruction that learns contrast-invariant content and style from image data only, eliminating the need for raw k-space training data. The method has been published in Medical Image Analysis. This work addresses a key data bottleneck in deep learning-based MRI reconstruction by removing the requirement for raw k-space data, which is often difficult to obtain. It also generalizes across different MR contrasts and forward operators, potentially accelerating clinical adoption of advanced reconstruction methods. The framework consists of two stages: first, a content/style model is learned from unpaired image-domain data; second, the frozen model serves as a plug-and-play prior in iterative reconstruction. It provides a built-in explanatory framework and achieves competitive performance with state-of-the-art unrolled networks.

reddit · r/MachineLearning · /u/void_gear · Jul 16, 13:10

**Background**: Multi-contrast MRI reconstruction aims to reconstruct high-quality images from undersampled k-space data, often leveraging information from a fully sampled reference contrast. Traditional deep learning methods require raw k-space data for training, which is a major bottleneck due to proprietary formats and storage constraints. Content/style modeling disentangles anatomical content (shared across contrasts) from contrast-specific style, enabling effective multi-contrast reconstruction without paired k-space data.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2409.13477">A Plug-and-Play Method for Guided Multi-contrast MRI Reconstruction based on Content/Style Modeling</a></li>
<li><a href="https://www.researchgate.net/publication/384245741_A_Plug-and-Play_Method_for_Guided_Multi-contrast_MRI_Reconstruction_based_on_ContentStyle_Modeling">(PDF) A Plug-and-Play Method for Guided Multi-contrast MRI Reconstruction based on Content/Style Modeling</a></li>

</ul>
</details>

**Tags**: `#MRI reconstruction`, `#deep learning`, `#medical imaging`, `#plug-and-play`, `#content/style modeling`

---

<a id="item-10"></a>
## [Schema Harness Achieves 99% on ARC-AGI-3 Public Set](https://www.reddit.com/r/MachineLearning/comments/1uyf8oo/new_fable5opus48_harness_called_schema_claims_99/) ⭐️ 8.0/10

A new AI reasoning harness called Schema has achieved 99% on the ARC-AGI-3 Public set using Claude Opus 4.8 and Fable 5, and 95.35% using GPT-5.6 Sol, without modifying any model weights. This near-perfect score on a challenging interactive reasoning benchmark demonstrates that improving the reasoning process around models can dramatically boost performance, potentially shifting focus from scaling models to engineering better harnesses. Schema uses a fixed fallback rule: Opus 4.8 and Sol xhigh run first; games scoring below 80 are rerun with Fable 5 and Sol max, and the higher per-game score is retained.

reddit · r/MachineLearning · /u/we_are_mammals · Jul 16, 21:02

**Background**: ARC-AGI-3 is an interactive reasoning benchmark that challenges AI agents to explore novel environments, infer goals, and plan actions. A harness is an external system that orchestrates how a model interacts with its environment, including observation processing, prediction testing, and plan revision. This approach improves performance without changing the underlying model weights.

<details><summary>References</summary>
<ul>
<li><a href="https://arcprize.org/arc-agi/3">ARC-AGI-3</a></li>
<li><a href="https://arcprize.org/competitions/2026/arc-agi-3">ARC Prize 2026 - ARC-AGI-3 Competition</a></li>
<li><a href="https://arxiv.org/abs/2603.24621">[2603.24621] ARC-AGI-3: A New Challenge for Frontier Agentic Intelligence</a></li>

</ul>
</details>

**Discussion**: The president of ARC Prize tweeted that the result "looks cool - need to dig into it," indicating cautious interest. The Reddit poster hopes to revive technical discussions in the community.

**Tags**: `#ARC-AGI`, `#AI reasoning`, `#harness`, `#LLM`, `#machine learning`

---

<a id="item-11"></a>
## [New Book on Mathematics of Data Science Released](https://arxiv.org/abs/2607.11938) ⭐️ 7.0/10

A new book titled 'Mathematics of Data Science' has been published on arXiv, focusing on high-dimensional intuition and foundational concepts for data science. This book addresses a critical gap in data science education by providing rigorous mathematical foundations for high-dimensional phenomena, which are essential for modern machine learning and statistics. The book emphasizes building intuition in high-dimensional spaces, covering topics like spikiness, volumes, and their implications for model fitting and optimization.

hackernews · Anon84 · Jul 16, 20:38 · [Discussion](https://news.ycombinator.com/item?id=48939896)

**Background**: Data science often relies on high-dimensional data, where human intuition fails. Understanding the geometry of high-dimensional spaces is crucial for grasping algorithms like stochastic gradient descent and regularization.

**Discussion**: Commenters praised the book for starting with high-dimensional intuition, calling it fundamental for modern data science. They noted that strong statistical basics and judgment are now the priority skills in the field.

**Tags**: `#data science`, `#mathematics`, `#high-dimensional`, `#statistics`, `#machine learning`

---

<a id="item-12"></a>
## [Classical ML for LLM Detection](https://blog.lyc8503.net/en/post/llm-classifier/) ⭐️ 7.0/10

A blog post explores using classical machine learning (e.g., TF-IDF with logistic regression) to detect LLM-generated text, achieving promising results on a small dataset. This approach offers a lightweight, interpretable alternative to deep learning detectors, potentially enabling browser extensions or real-time detection tools to combat the flood of AI-generated content online. The classifier uses features like n-grams and punctuation patterns, trained on a dataset of human and LLM-written texts. However, the author notes that such detectors may become less effective as LLMs evolve.

hackernews · uneven9434 · Jul 16, 16:41 · [Discussion](https://news.ycombinator.com/item?id=48936880)

**Background**: Detecting LLM-generated text is an active research area, with methods divided into black-box (training classifiers on text samples) and white-box (watermarking or analyzing model internals). Classical ML approaches like TF-IDF and logistic regression are simpler and more transparent than deep neural networks, but may struggle with generalization across different LLMs.

<details><summary>References</summary>
<ul>
<li><a href="https://medium.com/better-programming/detecting-llm-generated-texts-befce4426da9">Detecting LLM - Generated Texts . Is it possible to differentiate between</a></li>
<li><a href="https://cacm.acm.org/research/the-science-of-detecting-llm-generated-text/">The Science of Detecting LLM-Generated Text – Communications of the ACM</a></li>
<li><a href="https://arxiv.org/pdf/2303.07205">The Science of Detecting LLM - Generated Texts</a></li>

</ul>
</details>

**Discussion**: Commenters expressed skepticism about the long-term reliability of such detectors, comparing them to tarot card reading. Some proposed alternative approaches like estimating the effort put into writing, regardless of AI assistance, as a more robust metric.

**Tags**: `#LLM detection`, `#machine learning`, `#AI-generated text`, `#NLP`, `#classical ML`

---

<a id="item-13"></a>
## [Interactive Linear Algebra Book from 2015 Still Inspires](https://immersivemath.com/ila/) ⭐️ 7.0/10

The immersive linear algebra book at immersivemath.com, published in 2015, features interactive figures that allow readers to manipulate 3D visualizations directly in the browser. This book demonstrates how interactive visualization can significantly enhance understanding of abstract mathematical concepts, and its positive reception suggests a growing demand for such educational tools. The book covers standard linear algebra topics like vectors, matrices, and eigenvalues, with each interactive figure built using JavaScript and WebGL for real-time manipulation.

hackernews · srean · Jul 16, 15:32 · [Discussion](https://news.ycombinator.com/item?id=48935951)

**Background**: Linear algebra is a foundational branch of mathematics used in computer graphics, machine learning, and engineering. Traditional textbooks present static diagrams, which can make abstract concepts like vector spaces difficult to grasp. Interactive figures allow learners to rotate, scale, and explore geometric representations, bridging the gap between theory and intuition.

**Discussion**: Commenters express strong appreciation for the book, with many wishing similar resources existed for other subjects like statistics and robotics. Some note that modern AI tools like LLMs could make creating such interactive content even easier, potentially leading to a new wave of enhanced educational materials.

**Tags**: `#linear algebra`, `#interactive learning`, `#mathematics education`, `#visualization`

---

<a id="item-14"></a>
## [DABSN: New Recurrent LM Seeks Collaborators for Scaling](https://www.reddit.com/r/MachineLearning/comments/1uycffg/seeking_collaborators_for_scaling_and_independent/) ⭐️ 7.0/10

A researcher has released a preprint and open-source code for DABSN, a new recurrent language model architecture that shows promising results on reasoning and memory benchmarks, and is now seeking collaborators for scaling and independent evaluation. If DABSN scales competitively with transformers, it could offer a more efficient alternative for long-context language modeling, potentially reducing computational costs and enabling new applications in memory-intensive tasks. The architecture has been tested on benchmarks like MQAR, Copy, Key-Value retrieval, and A5/60, and a 24M-parameter language model was trained on 1B tokens with a GPT-2 tokenizer. The author is looking for help with independent reproduction, stronger baselines, and access to larger GPU clusters.

reddit · r/MachineLearning · /u/BleedingXiko · Jul 16, 19:17

**Background**: Recurrent language models process sequences by maintaining a hidden state, which can be more memory-efficient than transformers for long sequences but often underperforms on reasoning tasks. DABSN introduces a dynamic adaptive bias mechanism to improve memory and reasoning capabilities. The MQAR benchmark tests a model's ability to retrieve multiple associated items from memory, while A5/60 is a synthetic task for evaluating long-range dependencies.

<details><summary>References</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/multi-query-associative-recall-mqar">MQAR : Multi-Query Associative Recall</a></li>

</ul>
</details>

**Tags**: `#recurrent architecture`, `#language model`, `#open source`, `#collaboration`, `#scaling`

---

<a id="item-15"></a>
## [QLoRA Default Learning Rate 2e-4 Fails on Small Datasets](https://www.reddit.com/r/MachineLearning/comments/1uy1z8b/the_qlora_2e4_default_is_wrong_under_10k_samples/) ⭐️ 7.0/10

A Reddit user reports that the default learning rate of 2e-4 for QLoRA fine-tuning causes overfitting on datasets with fewer than 10,000 samples, and that reducing it to 1e-4 with more epochs significantly improves evaluation performance. This finding challenges a widely adopted default in the LLM fine-tuning community, potentially saving practitioners weeks of wasted effort on small datasets. It highlights the need for dataset-size-aware hyperparameter tuning in parameter-efficient fine-tuning methods. The user observed that with 2e-4, training loss decreases while eval loss stagnates or climbs, indicating overfitting. Switching to 1e-4 and increasing epochs from 3 to 5 produced the best eval gains. The user suggests that for datasets above 30k samples, 2e-4 may still be fine.

reddit · r/MachineLearning · /u/Pretty-Ad774 · Jul 16, 12:50

**Background**: QLoRA is a parameter-efficient fine-tuning technique that combines 4-bit quantization with Low-Rank Adaptation (LoRA) to reduce memory usage. The default learning rate of 2e-4 originates from the Alpaca dataset (52k samples) and is widely copied in tutorials and code examples without adjustment for smaller datasets.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2305.14314">[2305.14314] QLoRA: Efficient Finetuning of Quantized LLMs</a></li>
<li><a href="https://grokipedia.com/page/QLoRA">QLoRA</a></li>

</ul>
</details>

**Discussion**: The Reddit post received strong community validation, with many users sharing similar experiences of overfitting on small datasets with 2e-4. Some suggested using learning rate finders or cosine schedules, while others agreed that the default should be dataset-dependent.

**Tags**: `#QLoRA`, `#fine-tuning`, `#learning rate`, `#LLM`, `#practical advice`

---

<a id="item-16"></a>
## [Rethinking AI Memory: From Facts to Reasoning Patterns](https://www.reddit.com/r/MachineLearning/comments/1uy6yht/are_current_ai_memory_architectures_optimizing/) ⭐️ 7.0/10

A Reddit post questions whether current AI memory architectures should shift from storing descriptive facts to inferring higher-level reasoning patterns, such as explanatory frameworks and reasoning styles. This perspective could reshape how persistent context is designed in AI systems, potentially leading to more adaptive and personalized AI that understands how users think, not just what they say. The post contrasts current descriptive memory (e.g., 'user is interested in economics') with inferential memory (e.g., 'user explains economics through incentives and constraints'), and asks whether such representations require fundamentally new architectures.

reddit · r/MachineLearning · /u/Boris_Ljevar · Jul 16, 16:00

**Background**: Current AI memory systems, such as those in chatbots and agents, store facts, preferences, and conversation summaries to maintain context. These systems are primarily descriptive and rely on retrieval-augmented generation or summarization. Cognitive architectures, like the Semantic Pointer Architecture, explore how AI can model human-like reasoning and learning over time, but most commercial systems do not yet infer deep reasoning patterns.

<details><summary>References</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/memory-architectures-ai-agents-short-term-context-long-term-gareth-e7vuf">Memory Architectures for AI Agents: Short-Term Context, Long-Term...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Cognitive_architecture">Cognitive architecture - Wikipedia</a></li>
<li><a href="https://mem0.ai/">Mem0 - AI Memory Layer for your Agents & Apps | Persistent Context</a></li>

</ul>
</details>

**Discussion**: The Reddit discussion is substantive, with users debating whether current memory architectures are too shallow and whether inferential patterns could emerge from scaling existing models or require new designs. Some express skepticism about feasibility, while others see it as a natural evolution.

**Tags**: `#AI memory`, `#machine learning`, `#cognitive architectures`, `#persistent context`

---

<a id="item-17"></a>
## [Microsoft Open-Sources 1990s IRC Client Comic Chat](https://opensource.microsoft.com/blog/2026/07/16/microsoft-comic-chat-is-now-open-source/) ⭐️ 6.0/10

On July 16, 2026, Microsoft released the source code for Comic Chat (later renamed Microsoft Chat), a graphical IRC client from the 1990s, under an open-source license. This release preserves a piece of internet history and allows developers to study, modify, and run a unique chat client that visualized conversations as comic strips, reflecting the experimental spirit of the early web. Comic Chat was originally developed by Microsoft researcher David Kurlander and first shipped with Internet Explorer 3.0 in 1996. The open-source release was made possible by Robert Standefer and Scott Hanselman after six years of effort.

hackernews · jervant · Jul 16, 16:06 · [Discussion](https://news.ycombinator.com/item?id=48936426)

**Background**: IRC (Internet Relay Chat) is a text-based chat protocol popular in the 1990s and early 2000s. Comic Chat was a graphical IRC client that automatically rendered conversations as comic panels with customizable avatars and expressions, extending the IRC protocol with additional commands.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Microsoft_Comic_Chat">Microsoft Comic Chat</a></li>
<li><a href="https://en.wikipedia.org/wiki/IRC_client">IRC client</a></li>

</ul>
</details>

**Discussion**: Community comments are nostalgic and appreciative, with users sharing personal stories about being inspired by Comic Chat. Some note that it was controversial in its time due to protocol extensions, but overall the sentiment is positive about preserving this experimental software.

**Tags**: `#open source`, `#microsoft`, `#irc`, `#nostalgia`, `#history`

---

<a id="item-18"></a>
## [Decoy Font Tricks AI with Hidden Text](https://www.mixfont.com/experiments/decoy-font) ⭐️ 6.0/10

A new font called Decoy Font hides one text in the outlines and another in the shading, causing AI models to read the decoy text while humans can see both. This demonstrates a simple yet effective adversarial attack on AI text recognition, highlighting vulnerabilities in how multimodal models process visual text. The font works by exploiting the difference in spatial frequency: AI models tend to read the sharper outline text, while humans perceive both layers. Zoom level affects which text is legible to AI.

hackernews · ray__ · Jul 16, 16:18 · [Discussion](https://news.ycombinator.com/item?id=48936584)

**Background**: Adversarial typography is a technique that manipulates text appearance to fool AI models. Decoy Font is a form of font steganography, where information is hidden in plain sight by altering glyph shapes or shading.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2405.20090v1">Typography Leads Semantic Diversifying: Amplifying Adversarial Transferability across Multimodal Large Language Models</a></li>
<li><a href="https://www.emergentmind.com/topics/fontcode-steganography">FontCode Steganography</a></li>

</ul>
</details>

**Discussion**: Comments note that while the font is cool, it is not practically useful as AI can still read the intended text by downsampling. Tests show GPT-4o can identify the hidden text when prompted, but Claude fails.

**Tags**: `#font`, `#AI`, `#typography`, `#adversarial`

---

<a id="item-19"></a>
## [Offset Data Center Water Use by Converting Golf Courses](https://simonwillison.net/2026/Jul/17/spot-birds-not-golf/#atom-everything) ⭐️ 6.0/10

A proposal suggests hyperscalers like Google could offset their data center water consumption by purchasing golf courses in the Coachella Valley and converting them into public parks for birdwatching. Google used 10.9 billion gallons of water in 2025, while each of the 120 local golf courses uses about 750,000 gallons per day. This thought experiment highlights the growing water footprint of AI and data centers, and creatively links it to the high water consumption of golf courses in arid regions. It could spark discussion on sustainable offsets and land-use trade-offs. The proposal calculates that buying 40 of the 120 Coachella Valley golf courses (about one-third) would offset Google's daily water usage. The numbers are based on Google's 2025 environmental report and Coachella Valley water district data.

rss · Simon Willison · Jul 17, 02:58

**Background**: Data centers, especially those using evaporative cooling, consume large amounts of water. A single hyperscale data center can use 171 million liters annually. Meanwhile, golf courses in the Coachella Valley use about 800 acre-feet per year each, drawing from the Colorado River and groundwater.

<details><summary>References</summary>
<ul>
<li><a href="https://www.weforum.org/stories/2026/01/ai-water-data-centres-opportunity-am26-wef-xylem/">Why AI's water problem might actually be an opportunity</a></li>
<li><a href="https://www.latimes.com/california/story/2021-10-09/steve-lopez-column-heat-drought-coachella-valley-golf-courses-water-use">Column: Are desert golf courses doing enough to conserve?</a></li>

</ul>
</details>

**Tags**: `#data centers`, `#water usage`, `#sustainability`, `#AI energy`

---

<a id="item-20"></a>
## [Mermaid Diagrams Converted to Color ASCII Art via WebAssembly](https://simonwillison.net/2026/Jul/16/mermaid-ascii/#atom-everything) ⭐️ 6.0/10

Simon Willison compiled the Go library AlexanderGrooff/mermaid-ascii to WebAssembly, enabling in-browser conversion of Mermaid diagrams to ASCII art with color support. This tool makes Mermaid diagrams accessible in plain-text environments like terminals or code comments, with color support improving readability over previous ASCII-only converters. The tool supports flowcharts with labeled edges, subgraphs, and multi-line labels, and runs entirely client-side via WebAssembly without server dependencies.

rss · Simon Willison · Jul 16, 14:57

**Background**: Mermaid is a popular diagramming tool that uses text-based syntax to generate diagrams. ASCII art conversion allows these diagrams to be displayed in environments that lack graphical rendering, such as terminals or plain-text documents. WebAssembly enables running compiled code from languages like Go directly in the browser at near-native speed.

<details><summary>References</summary>
<ul>
<li><a href="https://tools.simonwillison.net/mermaid-ascii">Mermaid to ASCII art ( mermaid - ascii )</a></li>
<li><a href="https://simonwillison.net/2026/jul/16/mermaid-ascii/">Tool: Mermaid to ASCII art ( mermaid - ascii ) | Simon Willison’s Weblog</a></li>

</ul>
</details>

**Tags**: `#Mermaid`, `#ASCII art`, `#WebAssembly`, `#developer tools`

---
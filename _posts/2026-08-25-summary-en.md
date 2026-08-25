---
layout: default
title: "Horizon Summary: 2026-08-25 (EN)"
date: 2026-08-25
lang: en
---

> From 19 items, 14 important content pieces were selected

---

1. [MS Paint and Photos Embed Invisible GUID Watermarks in AI Images](#item-1) ⭐️ 8.0/10
2. [Interactive Moon Visualization by Ciechanowski](#item-2) ⭐️ 8.0/10
3. [Your Executable Is a SQLite Database: A Clever Linux Hack](#item-3) ⭐️ 8.0/10
4. [LLMs as Spatial Software Generators for Programmable 3D Objects](#item-4) ⭐️ 8.0/10
5. [Xiaomi's New CPU Matches Apple Single-Core, Leads Multi-Core](#item-5) ⭐️ 7.0/10
6. [EU Rules Threaten Makers and Micro-Entrepreneurs](#item-6) ⭐️ 7.0/10
7. [San Francisco Recreated as Playable 3D Web Game](#item-7) ⭐️ 7.0/10
8. [XMPP Celebrates 25 Years of Digital Independence](#item-8) ⭐️ 7.0/10
9. [New Framework: Brain Compresses Noisy World via Prediction](#item-9) ⭐️ 7.0/10
10. [Unbounded Labs Unveils Bart, a Vintage LLM Trained on Pre-1931 English](#item-10) ⭐️ 7.0/10
11. [Delay-Corrected Bellman Operator and Causal Attribution for Constrained RL](#item-11) ⭐️ 7.0/10
12. [Apple Confirms iCloud+ Hide My Email Addresses Stay on icloud.com](#item-12) ⭐️ 6.0/10
13. [Hyperparameter Unification in MARL Comparative Studies](#item-13) ⭐️ 6.0/10
14. [AAAI 2027 Acknowledges Reviewer Collusion in 2-Cycles](#item-14) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [MS Paint and Photos Embed Invisible GUID Watermarks in AI Images](https://xusheng.dev/posts/reversing/mspaint_invisible_watermark/main/) ⭐️ 8.0/10

Microsoft Paint and Photos now embed a server-issued GUID as an invisible watermark in AI-manipulated images, even when generated locally. The watermark is added silently and cannot be disabled, as revealed by reverse engineering of Watermarker.dll. This raises significant privacy and anonymity concerns, as the GUID can be linked to a Microsoft account, potentially allowing authorities or third parties to trace image creators. It also highlights a broader trend of hidden provenance tracking in AI-generated content, affecting user trust and legal implications. The watermark is a 16-byte GUID embedded across roughly 74% of image pixels, and it is added after a mandatory remote moderation request to an Azure Front Door endpoint. If the watermarking step fails, the image generation is cancelled. The watermark is invisible and cannot be disabled by the user.

hackernews · ComputerGuru · Aug 24, 15:28 · [Discussion](https://news.ycombinator.com/item?id=49421158)

**Background**: Microsoft Paint and Photos use local ONNX models for AI image generation on Copilot+ PCs, but prompt moderation is handled by remote servers. Invisible watermarking is a technique that embeds imperceptible data into digital content for authentication or tracking. This practice is becoming common in AI-generated media to ensure content provenance, but it raises concerns when done without user consent.

<details><summary>References</summary>
<ul>
<li><a href="https://xusheng.dev/posts/reversing/mspaint_invisible_watermark/main/">Microsoft Paint and Photos Embed Server-Issued GUIDs as ...</a></li>
<li><a href="https://www.theregister.com/ai-and-ml/2026/08/25/microsoft-ai-watermarks-in-paint-and-photos-are-linked-to-user-ids-researcher-finds/5292034">Microsoft AI watermarks in Paint and Photos are linked to ...</a></li>
<li><a href="https://mangodeveloper.com/articles/microsoft-paint-embeds-invisible-guid-watermarks-in-local-ai-images-via-remote-moderation-server">Microsoft Paint Embeds Invisible GUID Watermarks in Local AI ...</a></li>

</ul>
</details>

**Discussion**: Community comments express shock that MS Paint has evolved beyond a simple pixel editor and criticize Microsoft for silently adding unique identifiers to user-generated images. Some argue the AI aspect is a red herring, with the real issue being the erosion of internet anonymity, as the GUID could be used to subpoena user data. Others note Microsoft's past sloppy implementations of similar features, recommending caution.

**Tags**: `#privacy`, `#watermarking`, `#Microsoft`, `#AI`, `#security`

---

<a id="item-2"></a>
## [Interactive Moon Visualization by Ciechanowski](https://ciechanow.ski/moon/) ⭐️ 8.0/10

Bartosz Ciechanowski released an interactive, detailed visualization of the Moon, continuing his signature style of making complex topics intuitive through web-based graphics. This visualization exemplifies the potential of interactive web content for education, offering an engaging alternative to static diagrams. It also highlights a growing trend of using such techniques, possibly accelerated by AI-assisted development, to enhance learning experiences. The visualization includes multiple perspectives, such as a virtual planet view, which users found particularly enlightening. It is part of Ciechanowski's portfolio of similarly detailed interactive explanations on topics like gears, cameras, and the solar system.

hackernews · simonebrunozzi · Aug 24, 22:06 · [Discussion](https://news.ycombinator.com/item?id=49426466)

**Background**: Bartosz Ciechanowski is known for creating highly detailed, interactive web pages that explain complex concepts through intuitive visualizations. His work often uses WebGL and custom graphics to simulate physical phenomena, making them accessible to a broad audience. This Moon visualization follows that tradition, offering a deep dive into lunar features and motions.

**Discussion**: Community members praised the visualization's detail and educational value, with some noting that Ciechanowski's style has influenced their own AI-assisted development. There was also a discussion about the ethics of mimicking his style, and a suggestion for adding a table of contents to his long-form pages.

**Tags**: `#interactive visualization`, `#education`, `#web development`, `#astronomy`, `#data visualization`

---

<a id="item-3"></a>
## [Your Executable Is a SQLite Database: A Clever Linux Hack](https://simonwillison.net/2026/Aug/24/your-executable-is-a-sqlite-database/) ⭐️ 8.0/10

Farid Zakaria has demonstrated a technique to create a SQLite database file that can also be executed as a Linux binary. By setting the SQLite application ID to 'SELF' and storing ELF components in tables, the file can be run directly via a custom interpreter. This hack blurs the line between data and code, offering a novel way to create self-describing executables. It could inspire new approaches in software distribution, where a single file contains both executable logic and structured data, potentially simplifying deployment and inspection. The technique uses the SQLite file format's 4-byte application ID (at offset 68) set to 'SELF'. The ELF components are arranged into SQLite tables using a specific schema, and a custom interpreter (self-exec) extracts and executes them. Additionally, binfmt_misc can be configured to automatically invoke the interpreter for files with this pattern.

rss · Simon Willison · Aug 24, 11:38

**Background**: SQLite is a widely used embedded database that stores data in a single file, with a well-documented file format. ELF is the standard executable format on Linux, containing headers, sections, and segments. binfmt_misc is a Linux kernel feature that allows custom binary formats to be executed by associating them with an interpreter.

<details><summary>References</summary>
<ul>
<li><a href="https://www.sqlite.org/fileformat.html">Database File Format</a></li>
<li><a href="https://en.wikipedia.org/wiki/Executable_and_Linkable_Format">Executable and Linkable Format - Wikipedia</a></li>
<li><a href="https://docs.kernel.org/admin-guide/binfmt-misc.html">Kernel Support for miscellaneous Binary Formats (binfmt_misc) — The Linux Kernel documentation</a></li>

</ul>
</details>

**Discussion**: The Hacker News discussion likely praised the creativity and technical depth of the hack, with some users discussing potential use cases and limitations. There may be debates about the practicality compared to traditional ELF executables and the overhead of using SQLite as a container.

**Tags**: `#SQLite`, `#ELF`, `#Linux`, `#executable`, `#hack`

---

<a id="item-4"></a>
## [LLMs as Spatial Software Generators for Programmable 3D Objects](https://www.reddit.com/r/MachineLearning/comments/1vxcc1h/r_using_ai_as_a_spatial_software_generator_to/) ⭐️ 8.0/10

The paper introduces a novel approach where LLMs generate 3D objects as spatial software, making them inherently programmable, hierarchically structured, and animation-ready from inception. The authors provide visual demonstrations at nova3d.xyz and a GitHub repository. This approach could significantly disrupt industries like industrial design, game development, simulations, and AR/VR/XR by enabling 3D objects that are more useful than traditional monolithic mesh blobs. It suggests a future where code eventually 'eats' all 3D, as LLMs improve in spatial coding. The generated 3D objects can adapt their appearance based on compute environment (e.g., mobile vs. game engines) and include hinge/socket articulation at authoring time. However, the approach currently lags behind traditional AI 3D generators in creating complex organic shapes.

reddit · r/MachineLearning · /u/mhb_11 · Aug 24, 19:10

**Background**: Traditional AI 3D generators typically output monolithic mesh blobs that are not easily editable or animatable. Procedural modeling, which uses rules to create 3D models, is a related concept that allows for easy changes over time. This paper leverages LLMs' growing spatial reasoning capabilities to generate 3D objects as code, offering a new paradigm for 3D content creation.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2504.05786v1">How to Enable LLM with 3D Capacity? A Survey of Spatial ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Procedural_modeling">Procedural modeling - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Procedural_generation">Procedural generation - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#3D generation`, `#spatial programming`, `#AI research`, `#procedural generation`

---

<a id="item-5"></a>
## [Xiaomi's New CPU Matches Apple Single-Core, Leads Multi-Core](https://twitter.com/lemire/status/2091894299289874926) ⭐️ 7.0/10

Xiaomi has announced a new CPU, the XRing O3, which reportedly matches Apple's single-threaded performance and surpasses it in multithreaded benchmarks. The chip is based on an ARM design and is manufactured on TSMC's 3nm process. This marks Xiaomi's entry into the competitive mobile chip market, potentially challenging Qualcomm and MediaTek. As the third-largest smartphone maker by shipments, Xiaomi's in-house chip could reshape the industry landscape and increase competition. The XRing O3 is essentially an ARM reference design, similar to the one used in MediaTek's Dimensity 9500, with Xiaomi customizing the bus interconnect, physical implementation, NPU, and LPDDR6 memory support. Benchmarks show single-core scores around 3,945 and multi-core around 15,221, but real-world performance may be lower due to thermal and power constraints.

hackernews · tosh · Aug 24, 15:08 · [Discussion](https://news.ycombinator.com/item?id=49420873)

**Background**: ARM designs are licensed to companies like Xiaomi and MediaTek, who often use reference designs with minor modifications. Apple, in contrast, designs fully custom CPUs that only comply with the ARM instruction set, allowing for superior performance-per-watt. Single-threaded performance is crucial for everyday tasks, while multi-core performance benefits heavy workloads.

<details><summary>References</summary>
<ul>
<li><a href="https://coderfacts.com/coding-news/xiaomi-new-cpu-matches-apple-cores-single-threaded-much-faster-multithreaded/">Xiaomi : New CPU Matches Apple Cores Single Threaded , Much...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Thermal_design_power">Thermal design power - Wikipedia</a></li>
<li><a href="https://semiengineering.com/power-trip-advisor/">Power Trip Advisor | Semiconductor Engineering</a></li>

</ul>
</details>

**Discussion**: Commenters noted that the XRing O3 is an ARM design, not a fully custom Xiaomi chip, and that power efficiency is a critical missing metric. Some pointed out that Apple's M5 Max still leads in multi-core, and that the comparison is unfair due to core count differences (10 vs 6). Overall sentiment is cautious, acknowledging Xiaomi's progress but questioning the hype.

**Tags**: `#CPU`, `#Xiaomi`, `#Apple`, `#ARM`, `#semiconductors`

---

<a id="item-6"></a>
## [EU Rules Threaten Makers and Micro-Entrepreneurs](https://lectronz.com/u/lectronz/articles/how-europe-is-killing-makers-and-micro-entrepreneurs) ⭐️ 7.0/10

An article argues that EU regulations, particularly the Packaging and Packaging Waste Regulation (PPWR), are harming small-scale makers and micro-entrepreneurs, sparking a large discussion with over 1,100 points and 675 comments on Hacker News. This matters because it highlights a potential conflict between EU environmental and safety regulations and the viability of small-scale entrepreneurship, which could stifle innovation and economic diversity. The discussion reveals significant community concern and differing perspectives on the actual impact of these rules. Commenters point out that the EU FAQ clarifies that micro-enterprises and generic packaging are exempt, suggesting the article may exaggerate the impact. Additionally, the EU Commission originally proposed a central registry, but member states blocked it, and the EU now advises against enforcement until corrections are made.

hackernews · l-one-lone · Aug 24, 13:05 · [Discussion](https://news.ycombinator.com/item?id=49419237)

**Background**: The EU has been introducing regulations to reduce packaging waste and improve e-commerce safety, such as the PPWR and revised Payment Services Directive. These rules aim to make e-commerce sustainable and competitive, but they can impose compliance burdens on small businesses. The article and discussion focus on how these regulations affect micro-entrepreneurs who sell physical products online, potentially requiring them to meet complex packaging and labeling requirements.

<details><summary>References</summary>
<ul>
<li><a href="https://digital-strategy.ec.europa.eu/en/policies/e-commerce-rules-eu">e - Commerce rules in the EU | Shaping Europe ’s digital future</a></li>
<li><a href="https://www.thisismoney.co.uk/money/cars/article-14719077/EU-regulations-making-small-cars-expensive-bosses-two-major-manufacturers.html">EU regulations are making small cars too expensive... | This is Money</a></li>

</ul>
</details>

**Discussion**: The community discussion is divided: some commenters criticize the EU for overregulation and lack of harmonization, while others defend the EU, noting that member states are responsible for implementation issues. A commenter shares China's approach of regulating choke points like platforms and logistics, and another points out that micro-enterprises are exempt, suggesting the article may be misleading.

**Tags**: `#EU regulation`, `#makers`, `#micro-entrepreneurs`, `#e-commerce`, `#policy`

---

<a id="item-7"></a>
## [San Francisco Recreated as Playable 3D Web Game](https://sf.thijs.gg/) ⭐️ 7.0/10

A web-based interactive 3D recreation of San Francisco has been launched at sf.thijs.gg, allowing users to explore the city and drive vehicles. The project has gained significant community attention, with 387 points and 129 comments on Hacker News. This project showcases a novel use of mapping data to create an immersive, playable city experience directly in the browser, which could inspire future applications in urban planning, gaming, and virtual tourism. It demonstrates the potential of web-based 3D technologies for large-scale interactive environments. The game includes features such as driving vehicles and collecting coins, but lacks some expected elements like street names or landmarks. Users have noted limitations such as the inability to walk through certain yards and a glider being the only alternative transportation when vehicles are unavailable.

hackernews · centrosphere · Aug 24, 17:05 · [Discussion](https://news.ycombinator.com/item?id=49422784)

**Background**: The project leverages web-based 3D rendering technologies, likely using WebGL, to create a real-time interactive cityscape. Similar platforms like Babylon.js and Sketchfab demonstrate the capabilities of browser-based 3D graphics, which have advanced significantly in recent years, enabling complex scenes without requiring downloads or high-end hardware.

<details><summary>References</summary>
<ul>
<li><a href="https://www.babylonjs.com/">Babylon.js: Powerful, Beautiful, Simple, Open - Web -Based 3 D At Its...</a></li>
<li><a href="https://sketchfab.com/">Sketchfab - The best 3 D viewer on the web</a></li>

</ul>
</details>

**Discussion**: The community response has been overwhelmingly positive, with users expressing emotional connections to the city and enthusiasm for potential improvements. Suggestions include adding street names, landmarks, teleportation, and even transforming it into a live MMO. Some users also noted technical quirks and limitations, such as walking on water under the bridge.

**Tags**: `#3D visualization`, `#gaming`, `#mapping`, `#interactive`, `#San Francisco`

---

<a id="item-8"></a>
## [XMPP Celebrates 25 Years of Digital Independence](https://gultsch.de/posts/25-years-of-digital-independence/) ⭐️ 7.0/10

An article by gultsch.de reflects on XMPP's 25-year legacy, highlighting its current relevance and the community's hopes for its future. The piece underscores XMPP's enduring role as a decentralized, open messaging protocol. This milestone matters because XMPP remains a foundational open protocol for decentralized communication, contrasting with centralized alternatives. It highlights the ongoing importance of open standards in messaging and the potential for community-driven innovation. The article likely discusses XMPP's extensibility via XEPs, its federated architecture using JIDs, and its use in IoT and enterprise systems. It may also address challenges such as competition from Matrix and the need for modern features like end-to-end encryption.

hackernews · inputmice · Aug 24, 15:51 · [Discussion](https://news.ycombinator.com/item?id=49421536)

**Background**: XMPP, originally named Jabber, is an open, XML-based protocol for instant messaging and presence, designed to be decentralized and federated. It has been used by major companies like Google and Facebook in the past, and remains relevant in niche communities and IoT applications.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/XMPP">XMPP - Wikipedia</a></li>
<li><a href="https://xmpp.org/about/technology-overview/">An Overview of XMPP | XMPP - The universal messaging standard</a></li>
<li><a href="https://conversations.im/">Conversations: the very last word in instant messaging</a></li>

</ul>
</details>

**Discussion**: The HN discussion shows mixed sentiment: some users praise XMPP's flexibility and current projects like Movim and Fluux, while others lament Matrix's divergence and question XMPP's mainstream adoption. Practical use cases, such as agent communication and telephony bridges, are highlighted as strengths.

**Tags**: `#XMPP`, `#open protocols`, `#decentralization`, `#messaging`, `#anniversary`

---

<a id="item-9"></a>
## [New Framework: Brain Compresses Noisy World via Prediction](https://www.quantamagazine.org/a-new-framework-for-how-the-brain-compresses-our-noisy-world-20260824/) ⭐️ 7.0/10

Quanta Magazine published an article presenting an updated framework for brain categorization, viewing the brain as a prediction engine that compresses noisy sensory data through categorization, rather than a passive filing cabinet. The framework, proposed by Barrett and Miller, suggests categorization occurs across the entire brain, not in a specific area. This framework challenges traditional neuroscience views and could influence predictive processing models in AI and machine learning. It offers a unifying perspective on brain function, potentially impacting fields like cognitive science and artificial intelligence. The article highlights that categorization is not a late-stage process but operates throughout all brain processing. It also proposes that the brain uses predictive processing to anticipate sensory input and guide action, aligning with modern predictive coding theories.

rss · Quanta Magazine · Aug 24, 14:00

**Background**: Predictive processing is a theory in neuroscience proposing that the brain constantly generates and updates a mental model of the environment, predicting sensory input and updating based on prediction errors. Traditional views held that categorization occurs at the end of sensory processing, but this new framework integrates categorization into the predictive processing loop, suggesting it is a fundamental aspect of brain function.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Predictive_coding">Predictive coding - Wikipedia</a></li>
<li><a href="https://www.sciencedirect.com/topics/psychology/predictive-processing">Predictive Processing - an overview | ScienceDirect Topics</a></li>
<li><a href="https://neurosity.co/guides/predictive-processing-brain-prediction-machine">What Is Predictive Processing? Your Brain Predicts | Neurosity</a></li>

</ul>
</details>

**Tags**: `#neuroscience`, `#predictive processing`, `#categorization`, `#AI`, `#brain`

---

<a id="item-10"></a>
## [Unbounded Labs Unveils Bart, a Vintage LLM Trained on Pre-1931 English](https://www.reddit.com/r/MachineLearning/comments/1vx94er/bart_a_vintage_llm_r/) ⭐️ 7.0/10

Unbounded Labs has introduced Bart, a 2.82B parameter LLM trained from scratch on 20.1B tokens of pre-1931 English, along with a demo, blog post, and open-source model. The project aims to explore whether LLMs can generate original ideas akin to historical scientists, as proposed by Demis Hassabis. This project directly tests a provocative hypothesis about AI's potential for scientific discovery, potentially influencing future research directions. By open-sourcing everything, it provides a valuable resource for the community to study historical reasoning and generalization in LLMs. Bart was trained in 5 days on a single H100 with 60% MFU, and the team cleaned Harvard's Institutional Books from 242B to 23B tokens. They also created Vintage CORE, a suite of 20 benchmarks for vintage LLMs, and released a 416k-pair SFT dataset grounded in pre-1930s text.

reddit · r/MachineLearning · /u/soggydoggy8 · Aug 24, 17:20

**Background**: Demis Hassabis, CEO of Google DeepMind, proposed that an LLM trained on data up to 1911 could independently discover relativity, serving as a benchmark for AGI. This project is part of a broader trend of training LLMs on historical corpora, such as Talkie-1930, to study reasoning and generalization. The debate over whether LLMs are 'stochastic parrots' or capable of original thought is central to this research.

<details><summary>References</summary>
<ul>
<li><a href="https://officechai.com/ai/someone-built-an-llm-to-test-out-demis-hassabis-agi-definition-of-pre-1900-science-discovering-relativity/">Someone Built An LLM To Test Out Demis Hassabis' AGI ...</a></li>
<li><a href="https://www.marktechpost.com/2026/04/27/meet-talkie-1930-a-13b-open-weight-llm-trained-on-pre-1931-english-text-for-historical-reasoning-and-generalization-research/">Meet Talkie-1930: A 13B Open-Weight LLM Trained on Pre - 1931 ...</a></li>
<li><a href="https://medium.com/data-science-collective/can-an-llm-predict-the-future-if-its-stuck-in-1930-297fc5ab1cd2">Can an LLM Predict the Future If It’s Stuck in 1930? | Medium</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#vintage corpus`, `#research`, `#AI`, `#training`

---

<a id="item-11"></a>
## [Delay-Corrected Bellman Operator and Causal Attribution for Constrained RL](https://www.reddit.com/r/MachineLearning/comments/1vx11hz/delaycorrected_bellman_operator_causal/) ⭐️ 7.0/10

The author introduces a delay-corrected Bellman operator that uses an adaptive effective discount learned from the consequence-delay distribution, with a contraction proof that holds under unknown stochastic delay. They also propose an Interventional Consequence Net (ICN) pretrained on structural causal model labels to estimate marginal causal contribution per action for attribution. This work addresses a critical gap in constrained RL where violations are delayed and stochastic, which is common in real-world settings. By correcting for delays and using causal attribution, it could improve the safety and reliability of RL systems in applications like autonomous driving, finance, and healthcare. The ICN currently requires access to the environment's structural causal model to generate pretraining labels, which limits its applicability to settings where the SCM is known or can be reasonably specified. The contraction proof is a notable theoretical contribution, but the method is not yet end-to-end learned from observational or interventional data alone.

reddit · r/MachineLearning · /u/No_Cauliflower7923 · Aug 24, 12:11

**Background**: In standard constrained RL, it is assumed that consequences are immediate and attributable to the current action, which fails when violations are delayed and stochastic. The Bellman operator is a fundamental concept in RL used to iteratively update value functions, and its contraction property ensures convergence. Causal inference aims to determine the true effect of actions, which is relevant for attribution in delayed settings.

<details><summary>References</summary>
<ul>
<li><a href="https://prismix.dev/news/f1072ba9e03c">Delay-corrected Bellman operator + causal attribution for ...</a></li>
<li><a href="https://arxiv.org/abs/2403.14508">[2403.14508] Constrained Reinforcement Learning with Smoothed...</a></li>
<li><a href="https://proceedings.mlr.press/v162/miryoosefi22a/miryoosefi22a.pdf">Proceedings of the International Conference on Machine Learning 2022</a></li>

</ul>
</details>

**Discussion**: The discussion is likely substantive given the technical depth, with users possibly appreciating the theoretical contribution and the honest acknowledgment of limitations. Some may question the practicality of requiring a structural causal model, while others might suggest extensions to learn the SCM or use interventional data.

**Tags**: `#reinforcement learning`, `#constrained RL`, `#causal inference`, `#Bellman operator`, `#stochastic delay`

---

<a id="item-12"></a>
## [Apple Confirms iCloud+ Hide My Email Addresses Stay on icloud.com](https://developer.apple.com/news/?id=1ptvdtcm) ⭐️ 6.0/10

Apple has confirmed that iCloud+ Hide My Email addresses will continue to be hosted on the icloud.com domain, addressing user concerns about potential changes. This announcement clarifies the future of the privacy feature for existing and new users. This decision is significant because it ensures the continued usability of Hide My Email, a key privacy feature for iCloud+ subscribers. It also differentiates Apple from other providers by maintaining a stable, recognizable domain for masked addresses, which can help avoid email blocking issues. Hide My Email allows users to generate unique, random email addresses that forward to their personal inbox, and it is available on iPhone, iPad, Mac, and iCloud.com. The feature is part of iCloud+ and can be used with Sign in with Apple, but the addresses will remain on the icloud.com domain as confirmed.

hackernews · K7PJP · Aug 24, 22:13 · [Discussion](https://news.ycombinator.com/item?id=49426564)

**Background**: Hide My Email is a privacy feature in iCloud+ that lets users create random email addresses to protect their real email from being shared. It is part of Apple's broader privacy efforts, similar to email aliases offered by other services, but with the distinction of using Apple's own domain. The confirmation addresses concerns that Apple might change this, which could have affected user trust and feature reliability.

<details><summary>References</summary>
<ul>
<li><a href="https://support.apple.com/guide/icloud/set-up-hide-my-email-mm9d9012c9e8/icloud">Set up and use Hide My Email in iCloud+ on all your devices</a></li>
<li><a href="https://support.apple.com/en-us/105078">How to use Hide My Email with Sign in with Apple</a></li>
<li><a href="https://www.applemust.com/how-to-use-hide-my-email-in-icloud/">How to use Hide My Email in iCloud+ to protect your privacy ...</a></li>

</ul>
</details>

**Discussion**: Community comments express relief and approval, with users like joshuat glad that Apple listened. Some users highlight the benefit of using a common domain to avoid email blocking, while others note potential lock-in concerns but acknowledge the practical necessity. A few users express unrelated wishes, such as cheaper developer licenses for Sign in with Apple.

**Tags**: `#Apple`, `#Privacy`, `#Email`, `#iCloud`

---

<a id="item-13"></a>
## [Hyperparameter Unification in MARL Comparative Studies](https://www.reddit.com/r/MachineLearning/comments/1vxfmms/hyperparameters_fine_tuning_for_marl_comparative/) ⭐️ 6.0/10

A researcher training PPO variants on VMAS tasks asks whether hyperparameters must be unified across models for fair comparison, noting that unification can lead to non-convergence. This question highlights a common methodological challenge in MARL research: balancing fair comparison with optimal performance. The answer affects how researchers evaluate and report results, influencing the credibility and reproducibility of comparative studies. The researcher uses Independent PPO, Graph PPO, and HetGPPO on VMAS scenarios, and notes that optimal hyperparameters (e.g., learning rate, entropy coefficient, KL coefficient, SGD batch size) vary per architecture-scenario pair. Their goal is to test robustness under adversarial attacks on frozen models.

reddit · r/MachineLearning · /u/ham_bam0 · Aug 24, 21:10

**Background**: Multi-agent reinforcement learning (MARL) involves training multiple agents in shared environments. VMAS is a vectorized simulator for MARL, and HetGPPO is a framework that uses graph neural networks for heterogeneous multi-robot cooperation. Hyperparameter tuning is critical for convergence, but unifying hyperparameters across different architectures may not yield optimal results for each.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/proroklab/HetGPPO">GitHub - proroklab/ HetGPPO : Heterogeneous Multi-Robot...</a></li>
<li><a href="https://matteobettini.com/publication/vmas-a-vectorized-multi-agent-simulator-for-collective-robot-learning/VMAS-A-Vectorized-Multi-Agent-Simulator-for-Collective-Robot-Learning.pdf">VMAS : A Vectorized Multi - Agent Simulator for</a></li>
<li><a href="https://arxiv.org/html/2408.06503">Enhancing Heterogeneous Multi-Agent Cooperation in Decentralized...</a></li>

</ul>
</details>

**Tags**: `#MARL`, `#hyperparameter tuning`, `#research methodology`, `#PPO`, `#VMAS`

---

<a id="item-14"></a>
## [AAAI 2027 Acknowledges Reviewer Collusion in 2-Cycles](https://www.reddit.com/r/MachineLearning/comments/1vwujcy/aaai_2027_reviewer_bidding_and_assignment/) ⭐️ 6.0/10

AAAI 2027 organizers sent an email acknowledging collusion in the review process, specifically highlighting 2-cycles where authors review each other's papers. This marks a rare official admission of such integrity issues by a top AI conference. This acknowledgment is significant because it validates long-standing community suspicions about collusion in top conferences like AAAI, NeurIPS, ICLR, and ICML. It could prompt other conferences to address similar issues and improve review integrity, affecting thousands of researchers who rely on fair peer review. The post notes that most submissions come from a single country, increasing the likelihood of natural 2-cycles among authors from that country, which may lead to collusion. The author also questions whether AAAI released submission statistics and highlights that many accepted papers lack public code, forcing reimplementation efforts.

reddit · r/MachineLearning · /u/Fragrant_Fan_6751 · Aug 24, 06:11

**Background**: AAAI is a prestigious annual conference on artificial intelligence, and its peer review process involves assigning reviewers to papers. A 2-cycle occurs when two authors review each other's papers, which can be exploited for mutual favors. The review process typically uses an automated assignment algorithm, and the high concentration of submissions from one country can inadvertently create such cycles. The community has long suspected collusion, but official acknowledgment is rare.

<details><summary>References</summary>
<ul>
<li><a href="https://ojs.aaai.org/index.php/AAAI/article/view/17325">ojs. aaai .org/index.php/ AAAI /article/view/17325</a></li>
<li><a href="https://academia.stackexchange.com/questions/49406/aaai-review-criteria">conference - AAAI review criteria - Academia Stack Exchange</a></li>
<li><a href="https://aaai.org/conference/aaai/aaai-27/submission-instructions/">AAAI-27 Submission Instructions - AAAI</a></li>

</ul>
</details>

**Discussion**: The Reddit discussion likely reflects a mix of validation and concern, with users agreeing that collusion is a known issue and appreciating the official acknowledgment. Some may debate the extent of the problem or suggest solutions, while others might criticize the lack of concrete data or the focus on a single country.

**Tags**: `#AAAI`, `#reviewer collusion`, `#academic integrity`, `#conference review`, `#machine learning`

---
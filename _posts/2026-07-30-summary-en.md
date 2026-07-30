---
layout: default
title: "Horizon Summary: 2026-07-30 (EN)"
date: 2026-07-30
lang: en
---

> From 24 items, 22 important content pieces were selected

---

1. [Open-source engine runs Gemma 4 26B in 2 GB RAM on M-series Macs](#item-1) ⭐️ 9.0/10
2. [Self-Replicating AI Worm Targets Microsoft Word via Copilot](#item-2) ⭐️ 9.0/10
3. [Muon Puzzle Solved, But New Tensions Emerge](#item-3) ⭐️ 9.0/10
4. [AI startups increasingly withhold research publications](#item-4) ⭐️ 8.0/10
5. [Anthropic's AI Finds Cryptographic Weaknesses in HAWK and AES](#item-5) ⭐️ 8.0/10
6. [Matthew Green on AI's Role in Post-Quantum Crypto Shift](#item-6) ⭐️ 8.0/10
7. [AI Security Leaderboard Ranks Model Robustness via Automated Jailbreak Tests](#item-7) ⭐️ 8.0/10
8. [Mitchell Hashimoto Launches Superlogical with Non-Profit Model](#item-8) ⭐️ 7.0/10
9. [The Productivity Mirage: Tools vs. Real Work](#item-9) ⭐️ 7.0/10
10. [The Power of Cold Emailing](#item-10) ⭐️ 7.0/10
11. [AI Firms Hire Thousands of Tradespeople for Data Centers](#item-11) ⭐️ 7.0/10
12. [Kimi K3-256k: Tiered Pricing Halves Costs for Most Users](#item-12) ⭐️ 7.0/10
13. [Renter-Friendly Smart PTAC Retrofit with Raspberry Pi](#item-13) ⭐️ 7.0/10
14. [ICLR 2027 Deadline Conflicts with NeurIPS 2026 Decisions](#item-14) ⭐️ 7.0/10
15. [PostSlate achieves 10x speedup with vendor-agnostic Vulkan ML inference](#item-15) ⭐️ 7.0/10
16. [NeurIPS Reviewer Ghosting Sparks Debate](#item-16) ⭐️ 7.0/10
17. [Vision Pro Used for Architectural Walkthroughs](#item-17) ⭐️ 6.0/10
18. [Keychron Announces Open-Source Firmware for Gaming Mice](#item-18) ⭐️ 6.0/10
19. [CheapFoodMap: Crowdsourced Map of Meals Under $10](#item-19) ⭐️ 6.0/10
20. [SQL Replaced COBOL Programmers, Not Jobs](#item-20) ⭐️ 6.0/10
21. [GANFS: GAN-Based Automated Feature Selection for High-Dimensional Data](#item-21) ⭐️ 6.0/10
22. [TanML: Open-source tabular model validation toolkit seeks feedback](#item-22) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Open-source engine runs Gemma 4 26B in 2 GB RAM on M-series Macs](https://github.com/drumih/turbo-fieldfare) ⭐️ 9.0/10

TurboFieldfare, an open-source inference engine written in Swift and Metal, can run the 4-bit quantized Gemma 4 26B-A4B-IT model on any M-series Mac using only about 2 GB of RAM by streaming routed experts from SSD. This technique dramatically lowers the hardware barrier for running large language models on consumer devices, enabling powerful on-device AI on memory-constrained Macs without expensive upgrades. The engine achieves 5–6 tok/s on an 8 GB M2 MacBook Air and 31–35 tok/s on an M5 MacBook Pro, and includes an experimental OpenAI-compatible local server with streaming and tool call support.

hackernews · gitpusher42 · Jul 29, 15:05 · [Discussion](https://news.ycombinator.com/item?id=49098510)

**Background**: Gemma 4 26B-A4B-IT is a Mixture-of-Experts (MoE) model from Google DeepMind, where only a subset of experts is activated per token. TurboFieldfare exploits this sparsity by keeping shared layers and KV cache in RAM while streaming the required experts from SSD on demand, using a small expert cache and parallel pread to hide latency.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/google/gemma-4-26B-A4B-it">google/gemma-4-26B-A4B-it · Hugging Face</a></li>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Community members praised the approach, with some noting that llama.cpp with mmap can also run large models with low RAM but lacks the expert-streaming optimization. Users reported even higher speeds on high-end M4 Max Macs due to faster SSD and page cache, and one contributor provided a workaround for older macOS versions.

**Tags**: `#LLM inference`, `#on-device AI`, `#model quantization`, `#Swift/Metal`, `#memory optimization`

---

<a id="item-2"></a>
## [Self-Replicating AI Worm Targets Microsoft Word via Copilot](https://simonwillison.net/2026/Jul/29/ai-worming-through-word/#atom-everything) ⭐️ 9.0/10

Security researcher Håkon Måløy discovered a new prompt injection variant that turns Microsoft Copilot in Word into a self-replicating worm. Hidden instructions in a document cause Copilot to manipulate the document and copy the instructions into new documents, enabling propagation without the original attacker document. This is the first demonstration of a self-replicating prompt injection attack against an AI assistant, representing a paradigm shift in LLM security threats. It could lead to widespread data breaches and manipulation of enterprise documents if not mitigated. The attack uses hidden white-on-white text in Word documents that Copilot interprets as part of the user's request, causing it to manipulate the document and copy the instructions into the output. Microsoft was notified and had 144 days to respond, but no comprehensive fix has been released yet.

rss · Simon Willison · Jul 29, 18:43

**Background**: Prompt injection is a cybersecurity exploit where malicious inputs cause LLMs to behave unintentionally. Self-replicating worms are programs that copy themselves to spread across systems. This attack combines both concepts, using Copilot's ability to read and write documents to propagate hidden instructions.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Prompt_injection_attack">Prompt injection attack</a></li>
<li><a href="https://en.wikipedia.org/wiki/Self-replicating_computer_program">Self-replicating computer program</a></li>
<li><a href="https://en.wikipedia.org/wiki/Computer_worm">Computer worm - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Hacker News commenters expressed concern about the severity of the attack and the difficulty of defending against it, noting that similar hidden text techniques have been used in job applications. Some questioned whether Microsoft's 144-day response window was sufficient given the potential impact.

**Tags**: `#prompt injection`, `#AI security`, `#Microsoft Copilot`, `#self-replicating worm`, `#LLM vulnerabilities`

---

<a id="item-3"></a>
## [Muon Puzzle Solved, But New Tensions Emerge](https://www.quantamagazine.org/physicists-solve-a-muon-mystery-now-old-results-dont-add-up-20260729/) ⭐️ 9.0/10

New calculations have resolved the 25-year-old muon g-2 anomaly, but the updated Standard Model prediction now disagrees with other experimental results, creating a new puzzle. This resolution challenges the Standard Model of particle physics, potentially pointing to new physics beyond our current understanding. It affects how physicists interpret decades of experimental data and search for new particles. The muon g-2 experiment at Fermilab measured the muon's magnetic moment with unprecedented precision, but the new theoretical calculation aligns with the experimental value, eliminating the previous discrepancy. However, this same calculation now conflicts with other precision measurements, such as those from electron g-2.

rss · Quanta Magazine · Jul 29, 14:53

**Background**: The muon g-2 anomaly was a long-standing discrepancy between the measured and predicted magnetic moment of the muon, hinting at new physics. The Standard Model describes fundamental particles and forces, but has known gaps. The new calculation uses lattice quantum chromodynamics to improve the theoretical prediction.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Muon_g-2">Muon g-2 - Wikipedia</a></li>
<li><a href="https://muon-g-2.fnal.gov/">Fermilab | Muon g-2</a></li>
<li><a href="https://en.wikipedia.org/wiki/Standard_Model_of_particle_physics">Standard Model of particle physics</a></li>

</ul>
</details>

**Tags**: `#particle physics`, `#quantum mechanics`, `#muon`, `#standard model`, `#physics breakthrough`

---

<a id="item-4"></a>
## [AI startups increasingly withhold research publications](https://www.science.org/content/article/ai-s-top-startups-are-barely-publishing-their-research) ⭐️ 8.0/10

A new analysis reveals that top AI startups are publishing fewer research papers and sharing less of their work publicly, reversing the trend of open science that characterized earlier AI breakthroughs. This decline in transparency could slow down the pace of innovation, make it harder for the broader community to build on each other's work, and concentrate knowledge within a few well-funded companies. The study measured research output by tracking publications and citations, and found that startups like OpenAI and Anthropic have reduced their publication rates. The paper notes that while OpenAI still leads in cumulative citations, its publication frequency has dropped significantly.

hackernews · YeGoblynQueenne · Jul 29, 21:25 · [Discussion](https://news.ycombinator.com/item?id=49103285)

**Background**: Historically, AI research flourished through open publication and sharing of code and models, enabling rapid progress. However, as AI becomes more commercially valuable, startups face competitive pressure to keep their innovations secret to maintain a competitive edge.

**Discussion**: Commenters shared personal experiences: one noted that after struggling to publish in tier-1 journals, their startup stopped publishing to avoid competitors copying their work. Another expressed concern that the 'blogification' of AI research allows unverified claims to spread like social media, harming the field's integrity.

**Tags**: `#AI research`, `#open science`, `#startups`, `#transparency`

---

<a id="item-5"></a>
## [Anthropic's AI Finds Cryptographic Weaknesses in HAWK and AES](https://blog.cryptographyengineering.com/2026/07/29/some-notes-about-anthropics-new-results/) ⭐️ 8.0/10

Anthropic published two cryptanalysis results from their unreleased advanced model Claude Mythos, which autonomously discovered a lattice attack halving the security of the HAWK signature scheme and a Möbius Bridge speedup on 7-round AES. These results demonstrate that AI models are becoming highly capable in cryptanalysis, challenging the notion that progress is slowing and raising important questions about AI safety and the need for robust filters to prevent misuse. The attacks cost approximately $100,000 each and did not break any live systems; the HAWK attack reduces its security from 128 bits to 64 bits, and the AES attack improves upon the best known cryptanalysis of 7-round AES.

hackernews · supermatou · Jul 29, 16:42 · [Discussion](https://news.ycombinator.com/item?id=49099804)

**Background**: Cryptanalysis is the study of analyzing cryptographic systems to find weaknesses. HAWK is a post-quantum signature scheme, and AES is a widely used symmetric encryption standard. Anthropic's Claude Mythos is an advanced AI model that can autonomously conduct research, including posing hypotheses and running experiments.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/research/discovering-cryptographic-weaknesses">Discovering cryptographic weaknesses with Claude \ Anthropic</a></li>
<li><a href="https://blog.cryptographyengineering.com/2026/07/29/some-notes-about-anthropics-new-results/">Some thoughts about Anthropic’s new cryptanalysis results</a></li>
<li><a href="https://www.explainx.ai/blog/anthropic-mythos-cryptographic-weaknesses-hawk-aes-july-2026">Mythos Cryptanalysis HAWK AES — Anthropic July 2026 ...</a></li>

</ul>
</details>

**Discussion**: Community comments highlight the impressive autonomous capability of the model, with one user noting the prompt essentially told the model to keep going until results were found. There is also discussion about safety filters, as the model used (Mythos) is filtered in the publicly available version (Fable) to prevent misuse in cybersecurity and biology.

**Tags**: `#AI`, `#cryptanalysis`, `#Anthropic`, `#machine learning`, `#safety`

---

<a id="item-6"></a>
## [Matthew Green on AI's Role in Post-Quantum Crypto Shift](https://simonwillison.net/2026/Jul/29/matthew-green/#atom-everything) ⭐️ 8.0/10

Matthew Green, a respected cryptographer, commented on the historic transition from traditional public-key algorithms to post-quantum cryptography, highlighting that this is an opportune moment for AI to advance cryptanalysis. This commentary underscores the critical timing for AI-driven cryptanalysis to either strengthen confidence in new post-quantum algorithms or reveal vulnerabilities, which could shape the future of global cybersecurity. Green references standards like HAWK being considered in NIST's post-quantum signature competition, and mentions Impagliazzo's Five Worlds, specifically Minicrypt, as a possible scenario where public-key cryptography might not exist.

rss · Simon Willison · Jul 29, 18:18

**Background**: Post-quantum cryptography (PQC) aims to develop algorithms secure against both classical and quantum computers. Current public-key algorithms like RSA and ECC are vulnerable to quantum attacks via Shor's algorithm. NIST has been standardizing PQC algorithms since 2016, with HAWK being a candidate in the third round of the additional digital signature process announced in May 2026.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Post-quantum_cryptography">Post-quantum cryptography</a></li>
<li><a href="https://csrc.nist.gov/projects/post-quantum-cryptography">Post - Quantum Cryptography | CSRC</a></li>
<li><a href="https://blog.computationalcomplexity.org/2004/06/impagliazzos-five-worlds.html">Computational Complexity: Impagliazzo 's Five Worlds</a></li>

</ul>
</details>

**Tags**: `#cryptography`, `#post-quantum`, `#AI`, `#cryptanalysis`, `#security`

---

<a id="item-7"></a>
## [AI Security Leaderboard Ranks Model Robustness via Automated Jailbreak Tests](https://www.reddit.com/r/MachineLearning/comments/1vaargb/ai_security_leaderboard_benchmarking_model/) ⭐️ 8.0/10

A new leaderboard ranks frontier AI models by their security robustness, using an automated test suite that runs 1,500 jailbreak attempts per model and measures the number of universal jailbreaks. The initial results reveal a significant gap between the most and least robust models. As AI deployment decisions increasingly hinge on security—with governments pulling models for cybersecurity jailbreaks and developers hesitating on agent deployments—this benchmark provides a much-needed standardized measure of model robustness. It helps organizations compare and select models based on security, not just capability. The benchmark defines a universal jailbreak as a prompt that elicits compliant, detailed responses to over 75% of clearly harmful questions within a domain (e.g., offensive cybersecurity). The current version (v1.0) focuses on CBRNE and cybersecurity domains, and the authors plan to add open-weight models, new domains, and stronger attacks in future iterations.

reddit · r/MachineLearning · /u/ARGleave · Jul 29, 22:09

**Background**: AI security benchmarking has lagged behind capability benchmarking, despite the growing importance of model robustness for safe deployment. Universal jailbreaks are systematic inputs that can reliably bypass safety guardrails across multiple models. Automated jailbreak testing frameworks like Microsoft's PyRIT and FuzzyAI exist, but this leaderboard offers a standardized, public ranking specifically for frontier models.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cyberark.com/resources/threat-research-blog/jailbreaking-every-llm-with-one-simple-click">Jailbreaking Every LLM With One Simple Click</a></li>
<li><a href="https://www.sandgarden.com/learn/jailbreak-testing">Jailbreak Testing: Attempting to Bypass an AI Model's Safety Guardrails</a></li>
<li><a href="https://www.frontiermodelforum.org/">Frontier Model Forum</a></li>

</ul>
</details>

**Discussion**: The Reddit community provided substantive methodological feedback, with discussions on how to fairly compare open-weight models (which have a larger attack surface via weight perturbations) to proprietary ones. Suggestions included adding more realistic domains like agent hijacking and stronger adaptive attacks such as boundary point jailbreaking.

**Tags**: `#AI security`, `#benchmarking`, `#jailbreak`, `#model robustness`, `#red teaming`

---

<a id="item-8"></a>
## [Mitchell Hashimoto Launches Superlogical with Non-Profit Model](https://www.superlogical.com/) ⭐️ 7.0/10

Mitchell Hashimoto announced Superlogical, a new company building on the open-source libghostty terminal library, with a non-profit ownership model and remote-first hiring in Los Angeles, London, and New York. This marks a novel approach to open-source sustainability, where the founder transfers ownership of the core library to a non-profit and builds a commercial entity on top as an equal consumer. It could inspire similar models for other open-source projects. Superlogical will consume libghostty under the same MIT license as everyone else and contribute upstream improvements. The company is hiring in three cities with an expectation for flexible in-office schedules.

hackernews · yan · Jul 29, 15:41 · [Discussion](https://news.ycombinator.com/item?id=49098965)

**Background**: Ghostty is a popular terminal emulator created by Mitchell Hashimoto, known for its performance and features. libghostty is the underlying library extracted from Ghostty, providing terminal emulation APIs for other applications. The non-profit ownership model ensures the library remains community-governed.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/Uzaaft/awesome-libghostty">GitHub - Uzaaft/awesome-libghostty</a></li>
<li><a href="https://mitchellh.com/writing/libghostty-is-coming">Libghostty Is Coming – Mitchell Hashimoto</a></li>
<li><a href="https://docsmith.aigne.io/docs/ghostty/en/libghostty-ed730d">libghostty API - docsmith.aigne.io</a></li>

</ul>
</details>

**Discussion**: The community praised the non-profit ownership transfer and the commitment to building on libghostty as an open dependency. Some drew parallels to OLE/COM, while others expressed frustration with the enigmatic title of the announcement post.

**Tags**: `#terminal`, `#open-source`, `#startup`, `#remote-work`, `#libghostty`

---

<a id="item-9"></a>
## [The Productivity Mirage: Tools vs. Real Work](https://frantic.im/mirage/) ⭐️ 7.0/10

A reflective essay argues that obsessing over productivity tools often distracts from the actual work of thinking and building, sparking a community discussion with 157 points and 50 comments. This matters because many developers and technologists fall into the trap of optimizing their setup instead of focusing on the core tasks, leading to wasted time and reduced effectiveness. The essay highlights that 90% of a coder's time should be spent thinking and reading, not typing, and that a good craftsman cares about tools but as a means to an end, not a toy.

hackernews · msephton · Jul 29, 23:18 · [Discussion](https://news.ycombinator.com/item?id=49104335)

**Background**: Productivity culture in software engineering often emphasizes tooling, shortcuts, and automation to speed up coding. However, the hardest part of software development is understanding the problem, designing solutions, and making decisions, not typing code. This essay challenges the common obsession with productivity hacks and encourages a focus on deep work.

**Discussion**: Commenters generally agree, with some noting that customizing tools can be valuable if it genuinely improves workflow, but many warn against spending more time on setup than on actual work. One commenter suggests that productivity obsession may be a way to avoid the ambiguity and risk of real problem-solving.

**Tags**: `#productivity`, `#developer experience`, `#tooling`, `#software engineering`

---

<a id="item-10"></a>
## [The Power of Cold Emailing](https://zachholman.com/posts/cold-email) ⭐️ 7.0/10

Zach Holman published a personal essay recounting how cold emailing led to meaningful connections and opportunities, and provides practical tips for crafting effective outreach. This essay validates cold emailing as a powerful networking tool in an era dominated by social media, offering actionable advice that can help professionals and job seekers build valuable relationships. The essay emphasizes personalization, brevity, and genuine curiosity as key to successful cold emails, and shares specific examples from the author's experience.

hackernews · holman · Jul 29, 21:06 · [Discussion](https://news.ycombinator.com/item?id=49103089)

**Background**: Cold emailing refers to sending an unsolicited email to someone you don't know, typically for networking, job hunting, or business development. It requires careful crafting to avoid being ignored or marked as spam.

**Discussion**: Commenters shared personal success stories, such as reaching out to Joe Armstrong and getting a detailed reply, and noted that many perceived 'celebrities' are approachable. Some contrasted the practice with modern HR processes like LinkedIn.

**Tags**: `#career`, `#networking`, `#communication`, `#personal-development`

---

<a id="item-11"></a>
## [AI Firms Hire Thousands of Tradespeople for Data Centers](https://www.nytimes.com/2026/07/29/business/economy/data-center-electricians-training.html) ⭐️ 7.0/10

AI companies are recruiting thousands of electricians and carpenters to build data centers, highlighting a shift in labor demand toward construction trades. This trend underscores the massive physical infrastructure required for AI, potentially reshaping the labor market by offering high wages to tradespeople but also raising concerns about boom-and-bust cycles. The hiring surge is driven by the construction of new data centers, which require extensive electrical and carpentry work. Critics warn that such demand is cyclical and may not provide stable long-term careers.

hackernews · thm · Jul 29, 14:43 · [Discussion](https://news.ycombinator.com/item?id=49098198)

**Background**: Data centers are facilities that house computer systems and associated components, such as telecommunications and storage systems. They are critical for AI companies that rely on vast computing power for training and running models. The construction of these centers requires a wide range of skilled tradespeople, including electricians and carpenters.

**Discussion**: Commenters expressed mixed views: some warned that data center construction is boom-and-bust, making it risky for career planning, while others noted that these are infrastructure companies, not pure AI firms. There was also positive sentiment about tradespeople earning good wages.

**Tags**: `#AI`, `#data centers`, `#labor market`, `#infrastructure`, `#trades`

---

<a id="item-12"></a>
## [Kimi K3-256k: Tiered Pricing Halves Costs for Most Users](https://www.kimi.com/code/docs/en/kimi-code/models) ⭐️ 7.0/10

Kimi introduced a new tiered pricing model for its K3 model, with a hard cutoff at 256k context length, effectively halving costs for users who stay within that limit. This pricing change makes Kimi K3 significantly more affordable for the majority of users, potentially accelerating adoption in cost-sensitive applications and intensifying competition among AI model providers. The hard cutoff at 256k context is similar to OpenAI's pricing step at 272k tokens, and some coding tools like Kimi Code CLI will compact context when switching from the 1M version to the 256k version.

hackernews · monneyboi · Jul 29, 19:25 · [Discussion](https://news.ycombinator.com/item?id=49101852)

**Background**: Kimi K3 is a 2.8 trillion parameter Mixture-of-Experts model with 104 billion activated parameters and a native 1-million-token context window. The new K3-256k variant offers a lower-cost option for users who do not need the full 1M context, with the API enforcing a hard cutoff at 256k tokens.

<details><summary>References</summary>
<ul>
<li><a href="https://www.kimi.com/code/docs/en/kimi-code/models">Model Configuration | Kimi Code Docs</a></li>
<li><a href="https://arxiv.org/pdf/2607.24653">Kimi K3: Open Frontier Intelligence - arXiv.org</a></li>
<li><a href="https://platform.kimi.ai/docs/models">Model List - Kimi API Platform</a></li>

</ul>
</details>

**Discussion**: Commenters noted the similarity to OpenAI's pricing step and expressed surprise at the hard cutoff instead of a smooth gradient. Some highlighted the massive VRAM requirements (1.5TB) of the full model, though compression techniques can reduce it to ~570GB.

**Tags**: `#AI`, `#pricing`, `#context length`, `#LLM`, `#Kimi`

---

<a id="item-13"></a>
## [Renter-Friendly Smart PTAC Retrofit with Raspberry Pi](https://prilik.com/blog/post/automating-ac-nyc/) ⭐️ 7.0/10

A detailed guide shows how to retrofit a dumb PTAC unit with smart controls using a Raspberry Pi and relays, designed to be fully reversible for renters. The project replaces the physical control knob with relay-based electronic control, enabling remote and automated operation. This project addresses a common pain point for renters who cannot modify permanent fixtures, offering a practical way to gain smart home benefits without losing a security deposit. It also sparks discussion on standardizing appliance interfaces for easier automation. The guide uses a Raspberry Pi to control relays that simulate button presses on the PTAC's control panel, with software written in Python. The setup is designed to be easily removed, leaving no permanent modifications to the unit.

hackernews · austinallegro · Jul 29, 18:28 · [Discussion](https://news.ycombinator.com/item?id=49101198)

**Background**: PTAC (Packaged Terminal Air Conditioner) units are common in older buildings, especially in New York City, and typically have simple mechanical controls with no smart features. Retrofitting such units often involves irreversible modifications, which is problematic for renters. This project uses a Raspberry Pi and relays to interface with the existing controls without soldering or cutting wires.

<details><summary>References</summary>
<ul>
<li><a href="https://www.electronicshub.org/control-a-relay-using-raspberry-pi/">Raspberry Pi Relay Control: Power Up Your Projects (Easy Guide)</a></li>
<li><a href="https://newbiely.com/tutorials/raspberry-pi/raspberry-pi-relay">Raspberry Pi - Relay | Raspberry Pi Tutorial</a></li>
<li><a href="https://us.shelly.com/pages/existing-home">Existing Home - Shelly USA</a></li>

</ul>
</details>

**Discussion**: Commenters suggested alternative approaches like using an ESP32 with IR control (vrighter) or ESPhome for easier software setup (vayun). Some discussed the broader issue of appliance standardization, wishing for simple analog/digital interfaces like HVAC thermostats (EvanAnderson).

**Tags**: `#smart home`, `#DIY`, `#IoT`, `#HVAC`, `#home automation`

---

<a id="item-14"></a>
## [ICLR 2027 Deadline Conflicts with NeurIPS 2026 Decisions](https://www.reddit.com/r/MachineLearning/comments/1v9v4e7/iclr_2027_deadline_is_before_neurips_2026/) ⭐️ 7.0/10

ICLR 2027 has set its full paper deadline for September 16, 2026, which is 8 days before NeurIPS 2026 releases its acceptance decisions, creating a scheduling conflict. This scheduling overlap may disadvantage authors who wish to revise and resubmit papers rejected from NeurIPS, potentially reducing the quality of submissions to ICLR and affecting fairness in the review process. The ICLR 2027 deadline is set before authors receive NeurIPS 2026 decisions, meaning they cannot incorporate feedback from NeurIPS into their ICLR submissions. This may force authors to choose between submitting to ICLR without knowing NeurIPS results or waiting for NeurIPS decisions and missing the ICLR deadline.

reddit · r/MachineLearning · /u/1414vo · Jul 29, 12:43

**Background**: ICLR (International Conference on Learning Representations) and NeurIPS (Conference on Neural Information Processing Systems) are two of the top-tier conferences in machine learning. Authors often submit their work to multiple conferences, revising based on feedback from earlier rejections. The typical conference cycle allows for a gap between deadlines and decisions to accommodate such revisions.

**Discussion**: The Reddit post expresses concern that the scheduling will hurt papers that have improved since NeurIPS submission or were unfairly rejected. Commenters likely discuss the implications for submission strategies and the potential for reduced paper quality at ICLR.

**Tags**: `#machine learning`, `#conference deadlines`, `#ICLR`, `#NeurIPS`, `#research community`

---

<a id="item-15"></a>
## [PostSlate achieves 10x speedup with vendor-agnostic Vulkan ML inference](https://www.reddit.com/r/MachineLearning/comments/1v9s4mz/vendoragnostic_ml_inference_on_production_edge/) ⭐️ 7.0/10

PostSlate, a video editing tool, achieved vendor-agnostic ML inference on production edge devices using ncnn's Vulkan backend, yielding a 10x speedup over ONNX CPU inference for face detection and embedding models. This demonstrates a practical, cross-platform solution for running ML inference on diverse GPUs without vendor-specific dependencies, enabling broader deployment of on-device AI in consumer applications. On an NVIDIA 4070 with fp16, ArcFace R50 runs in 3 ms (vs. 30 ms on ONNX CPU) and SCRFD face detection in 2.5 ms (vs. 25 ms). Model size is halved from 174 MB (ONNX fp32) to 87 MB (ncnn fp16).

reddit · r/MachineLearning · /u/ppchaos · Jul 29, 10:22

**Background**: ncnn is a high-performance neural network inference framework optimized for mobile and edge devices. Its Vulkan backend leverages the cross-platform Vulkan API to run on GPUs from any vendor (NVIDIA, AMD, Intel, Apple) without requiring CUDA or other proprietary runtimes.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/upscayl/upscayl-ncnn">GitHub - upscayl/upscayl-ncnn: The Upscayl backend powered by the NCNN framework and Real-ESRGAN architecture. · GitHub</a></li>
<li><a href="https://sourceforge.net/projects/real-esrgan-ncnn-vulkan.mirror/">Real-ESRGAN ncnn Vulkan download | SourceForge.net</a></li>
<li><a href="https://github.com/deepinsight/insightface/blob/master/detection/scrfd/README.md">insightface/detection/scrfd/README.md at master - GitHub</a></li>

</ul>
</details>

**Tags**: `#ML inference`, `#Vulkan`, `#edge computing`, `#vendor-agnostic`, `#ncnn`

---

<a id="item-16"></a>
## [NeurIPS Reviewer Ghosting Sparks Debate](https://www.reddit.com/r/MachineLearning/comments/1va5io6/neurips_reviewers_not_engaging_d/) ⭐️ 7.0/10

A Reddit discussion highlights the persistent problem of NeurIPS reviewers failing to engage during the rebuttal period, with users proposing penalties such as withholding scores for reviewers who ghost. Reviewer ghosting undermines the peer review process, potentially leading to unfair rejections and eroding trust in top ML conferences like NeurIPS. The original poster suggests that NeurIPS could penalize reviewers' own papers if they fail to engage, similar to how area chairs who miss meta-review deadlines have their scores withheld.

reddit · r/MachineLearning · /u/grumpket · Jul 29, 18:59

**Background**: NeurIPS is a premier machine learning conference where submitted papers undergo peer review, including a rebuttal phase where authors respond to reviewer comments. Reviewer ghosting—when reviewers ignore or fail to respond during rebuttals—has been a recurring complaint, exacerbated by the growing scale of submissions.

<details><summary>References</summary>
<ul>
<li><a href="https://www.singularitymoments.com/content/peer-review-is-broken-and-neurips-2026s-review-drop-proves-it/">Peer review is broken and NeurIPS 2026's review drop proves it</a></li>
<li><a href="https://neurips.cc/Conferences/2025/ReviewerGuidelines">2025 Reviewer Guidelines</a></li>
<li><a href="https://neurips.cc/Conferences/2025/AC-Guidelines">NeurIPS 2025 AC Guidelines</a></li>

</ul>
</details>

**Discussion**: The discussion shows mixed sentiment: some users share strategies like politely nudging reviewers, while others support stronger penalties. A few argue that reviewer ghosting is a symptom of systemic overload rather than malice.

**Tags**: `#NeurIPS`, `#peer review`, `#conference`, `#machine learning`, `#community`

---

<a id="item-17"></a>
## [Vision Pro Used for Architectural Walkthroughs](https://christianselig.com/2026/07/vision-pro-house/) ⭐️ 6.0/10

Christian Selig describes using Apple Vision Pro for immersive architectural walkthroughs of house designs, allowing intuitive spatial understanding and real-time adjustments. This showcases a practical, high-value use case for spatial computing in architecture, potentially transforming how architects and clients collaborate on design. The walkthrough uses Apple Vision Pro with visionOS, leveraging 3D tracking and camera passthrough for mixed reality. Users can walk around virtual models and assess proportions instantly.

hackernews · robbiet480 · Jul 29, 20:39 · [Discussion](https://news.ycombinator.com/item?id=49102774)

**Background**: Apple Vision Pro is a spatial computer that blends digital content with the physical world. It uses eye tracking, hand gestures, and voice input for interaction. Architectural walkthroughs are a natural application, allowing designers to experience spaces at full scale before construction.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Apple_Vision_Pro">Apple Vision Pro</a></li>
<li><a href="https://www.apple.com/apple-vision-pro/">Apple Vision Pro - Apple</a></li>
<li><a href="https://www.meegle.com/en_us/topics/spatial-computing/spatial-computing-in-architecture">Spatial Computing In Architecture</a></li>

</ul>
</details>

**Discussion**: Commenters share positive experiences using VR headsets like Quest 3 and HTC Vive for similar architectural walkthroughs, emphasizing the value of instant spatial judgment. One suggests simulating sun angles for lighting analysis. A negative comment calls it 'creepy and expensive crap.'

**Tags**: `#AR/VR`, `#Architecture`, `#Vision Pro`, `#Design`

---

<a id="item-18"></a>
## [Keychron Announces Open-Source Firmware for Gaming Mice](https://www.digitalfoundry.net/news/2026/07/keychron-announces-first-open-source-firmware-for-gaming-mice) ⭐️ 6.0/10

Keychron has announced ZGM (Zephyr Gaming Mouse), an open-source firmware for gaming mice based on Zephyr RTOS, with a planned release in Q1 2027. However, no source code has been released yet, leading to skepticism. This could expand open-source firmware options for gaming mice, but the lack of code and distant release date make it currently vaporware. The community is skeptical about its novelty given existing QMK-based mice like Ploopy. The firmware is built on Zephyr RTOS, targeting ultra-low power and high performance. Keychron has set up a GitHub repository (github.com/Keychron/zgm) and a website (zgm.gg), but both currently contain no source code.

hackernews · JLO64 · Jul 29, 16:36 · [Discussion](https://news.ycombinator.com/item?id=49099715)

**Background**: QMK (Quantum Mechanical Keyboard) is a popular open-source firmware originally for keyboards, but has been ported to some mice like Ploopy. Keychron's ZGM aims to create a dedicated open-source firmware for gaming mice using Zephyr RTOS, a real-time operating system for embedded devices.

<details><summary>References</summary>
<ul>
<li><a href="https://qmk.fm/">QMK Firmware</a></li>
<li><a href="https://zgm.gg/">ZGM Firmware — Zephyr Gaming Mouse</a></li>

</ul>
</details>

**Discussion**: Community comments express skepticism, noting that announcements without code are vaporware. Some question the need for a new project when QMK already supports mice, while others hope for features like device-to-device communication.

**Tags**: `#open-source`, `#firmware`, `#gaming mice`, `#keychron`, `#qmk`

---

<a id="item-19"></a>
## [CheapFoodMap: Crowdsourced Map of Meals Under $10](https://cheapfoodmap.com/) ⭐️ 6.0/10

A developer launched CheapFoodMap, a crowdsourced map of local meals under $10, inspired by Korea's 'Beggar's Map', with initial data covering 1,200 meals across 15 US cities. This tool helps budget-conscious diners find affordable local eats, addressing a practical need amid rising food prices. It also explores a community-driven model for price freshness, which could influence similar crowdsourced platforms. The seed data was sourced from Google Reviews with 4.2+ stars and 500+ reviews, manually verified for menu items under $10. The creator is seeking feedback on a price-freshness model to keep prices current amid inflation.

hackernews · jaep1 · Jul 29, 16:59 · [Discussion](https://news.ycombinator.com/item?id=49100043)

**Background**: The project is inspired by 거지맵 (Beggar's Map), a Korean crowdsourced map that helps students find cheap meals. The creator, recently laid off, built the site publicly over 100 days. The map currently excludes franchises, focusing on local eateries.

<details><summary>References</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=49100043">Show HN: CheapFoodMap – A map of good meals under $10 | Hacker News</a></li>
<li><a href="https://world.storm.mg/articles/1123112">"Beggar Map" Tracks Rising Lunch Prices in Seoul as Middle East Tensions Drive Inflation | International News Center | World - The Storm Media</a></li>
<li><a href="https://oneulkorea.com/articles/trends/geojimap-korea-viral-budget-food-map-2026">Geojimap: Korea's Viral Budget Food Map That 400,000 Koreans Are Using Right Now | OneulKorea Articles</a></li>

</ul>
</details>

**Discussion**: Commenters compared it to GasBuddy, noting the challenge of maintaining price accuracy without business incentives. Some suggested targeting specific user groups like truck drivers, while others raised concerns about price variability across regions and the difficulty of comparing non-uniform food items.

**Tags**: `#crowdsourcing`, `#food`, `#web app`, `#maps`, `#personal project`

---

<a id="item-20"></a>
## [SQL Replaced COBOL Programmers, Not Jobs](https://simonwillison.net/2026/Jul/29/d-richard-hipp/#atom-everything) ⭐️ 6.0/10

D. Richard Hipp, creator of SQLite, observed that SQL replaced the need for dedicated COBOL programmers to write data querying code, but programming jobs evolved rather than disappeared. This historical perspective challenges the fear that automation eliminates jobs, showing instead that technology shifts roles and creates new opportunities for programmers. Hipp's comment was made during a YouTube talk, simplifying the transition: SQL allowed users to specify queries declaratively, replacing the manual coding previously done by COBOL programmers.

rss · Simon Willison · Jul 29, 21:15

**Background**: COBOL is a business-oriented programming language from the 1960s, widely used for data processing on mainframes. SQL, introduced in the 1970s, provides a declarative way to query databases, reducing the need for custom procedural code.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/COBOL_programming_language">COBOL programming language</a></li>
<li><a href="https://en.wikipedia.org/wiki/D._Richard_Hipp">D. Richard Hipp</a></li>

</ul>
</details>

**Tags**: `#sql`, `#programming-history`, `#careers`, `#d-richard-hipp`

---

<a id="item-21"></a>
## [GANFS: GAN-Based Automated Feature Selection for High-Dimensional Data](https://www.reddit.com/r/MachineLearning/comments/1vahcwo/i_built_ganfs_a_python_package_that_uses_gans_to/) ⭐️ 6.0/10

A new Python package called ganfs uses Generative Adversarial Networks (GANs) to automate feature selection by analyzing discriminator sensitivity to perturbations, ranking features based on which are hardest to fake. This approach addresses a key bottleneck in machine learning—feature selection for high-dimensional datasets—without requiring domain expertise, potentially improving model performance and reducing computational costs across many fields. The package is available via pip, follows a scikit-learn-like API, and was originally developed for DDoS detection. The accompanying arXiv paper provides mathematical details and experimental validation on the CIC-DDoS2019 dataset.

reddit · r/MachineLearning · /u/One_Crow_4710 · Jul 30, 02:54

**Background**: Feature selection is the process of choosing the most useful input features for a machine learning model, which helps improve performance, reduce noise, and enhance interpretability. Traditional methods like filter, wrapper, or embedded approaches often struggle with scalability or capturing nonlinear relationships. GANs consist of a generator and a discriminator that compete adversarially; ganfs leverages the discriminator's sensitivity to perturbations to identify informative features.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2504.18566">[2504.18566] Feature Selection via GANs (GANFS): Enhancing ... A GAN and Feature Selection-Based Oversampling Technique for ... GAN-Driven Feature Selection and GraphSAGE for Advanced ... Inferential Gans and Deep Feature Selection with Applications Feature Selection Techniques in Machine Learning Recent advances in genetic algorithm-based feature selection ...</a></li>
<li><a href="https://arxiv.org/html/2504.18566v1">Feature Selection via GANs (GANFS): Enhancing Machine ...</a></li>

</ul>
</details>

**Tags**: `#feature selection`, `#GANs`, `#Python`, `#machine learning`

---

<a id="item-22"></a>
## [TanML: Open-source tabular model validation toolkit seeks feedback](https://www.reddit.com/r/MachineLearning/comments/1va7w4p/opensource_tabular_model_validation_toolkit_tanml/) ⭐️ 6.0/10

TanML, an MIT-licensed automated model-validation toolkit for tabular machine learning models, has been released as an open-source project and is seeking community feedback. It provides an end-to-end workflow including data profiling, preprocessing, feature ranking, model development, evaluation, drift analysis, stress testing, SHAP explainability, and audit-ready Word reports. This toolkit addresses the growing need for rigorous model validation in regulated industries like banking and insurance, where compliance and auditability are critical. By automating validation workflows, TanML could help organizations reduce manual effort, ensure consistency, and meet regulatory requirements more efficiently. TanML runs locally, ensuring data privacy, and generates audit-ready Word reports. It includes drift analysis and stress testing, which are essential for monitoring model performance over time and under adverse conditions.

reddit · r/MachineLearning · /u/AccomplishedLeg1508 · Jul 29, 20:22

**Background**: Model validation is a critical step in deploying machine learning models, especially in regulated industries where models must be transparent, explainable, and compliant with standards. SHAP (SHapley Additive exPlanations) is a popular method for explaining model predictions using Shapley values from game theory. Drift analysis detects changes in data distribution or model performance over time, which is important for maintaining model reliability.

<details><summary>References</summary>
<ul>
<li><a href="https://shap.readthedocs.io/en/latest/example_notebooks/overviews/An+introduction+to+explainable+AI+with+Shapley+values.html">An introduction to explainable AI with Shapley values — SHAP ...</a></li>
<li><a href="https://medium.com/data-science/drift-in-machine-learning-e49df46803a">Drift in Machine Learning . Why is it hard and what to do... | Medium</a></li>

</ul>
</details>

**Tags**: `#tabular models`, `#model validation`, `#open source`, `#MLOps`, `#regulated industries`

---
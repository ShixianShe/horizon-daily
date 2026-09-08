---
layout: default
title: "Horizon Summary: 2026-09-08 (EN)"
date: 2026-09-08
lang: en
---

> From 25 items, 22 important content pieces were selected

---

1. [OpenAI Accused of Pressuring Researcher to Downplay Navier-Stokes Work](#item-1) ⭐️ 9.0/10
2. [Researcher Factors 1990s CA's RSA Keys with Consumer GPU](#item-2) ⭐️ 8.0/10
3. [Mistral Raises €3B to Boost European Sovereign Open-Weight AI](#item-3) ⭐️ 8.0/10
4. [D2's TALA Layout Engine Goes Open Source](#item-4) ⭐️ 8.0/10
5. [Jellyfin 12.0 Released with Major Improvements](#item-5) ⭐️ 8.0/10
6. [Linux Kernel Git Server Overwhelmed by Abusive Crawlers](#item-6) ⭐️ 8.0/10
7. [Two Child Gene-Therapy Deaths in China Expose Regulatory Gaps](#item-7) ⭐️ 8.0/10
8. [Tiny RNN Autonomously Generates Bad Apple Video from Single Initial State](#item-8) ⭐️ 8.0/10
9. [Rustuna: High-Performance Rust Implementation of Optuna](#item-9) ⭐️ 8.0/10
10. [LLM-guided program evolution improves 10 circle-packing solutions](#item-10) ⭐️ 8.0/10
11. [Yandex Research Proposes KV Cache as Agent Runtime for Interactive LLMs](#item-11) ⭐️ 8.0/10
12. [Australia's 'My Feed, My Way' to Let Users Opt Out of Algorithms](#item-12) ⭐️ 7.0/10
13. [Google's Algorithm Creates 'Google Jail' for Independent Wikis](#item-13) ⭐️ 7.0/10
14. [Interactive Map Visualizes LA Building Construction Timeline (1880-2026)](#item-14) ⭐️ 7.0/10
15. [Broadcom Pulls VDDK Downloads, Complicating VMware Migration](#item-15) ⭐️ 7.0/10
16. [OpenAI Chief Scientist Advocates Defensive AI, Warns Against Reckless Racing](#item-16) ⭐️ 7.0/10
17. [EmbedFlow: Zero-Downtime Embedding Model Migration](#item-17) ⭐️ 7.0/10
18. [AI Threat Spurs Call for Year-Long Global Security Fix](#item-18) ⭐️ 6.0/10
19. [llm 0.35 Adds Support for OpenAI's GPT-6 Astra](#item-19) ⭐️ 6.0/10
20. [Simon Willison Builds WebAssembly FFmpeg Video Compressor](#item-20) ⭐️ 6.0/10
21. [Animated Mercator to Equal Earth Transition Tool Built with D3 and GPT-6 Astra](#item-21) ⭐️ 6.0/10
22. [Proposal: Stockfish-like Decision Quality and Anti-Cheat for Dynamic Games](#item-22) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [OpenAI Accused of Pressuring Researcher to Downplay Navier-Stokes Work](https://cims.nyu.edu/~tristanb/statement.pdf) ⭐️ 9.0/10

Tristan Buckmaster, a mathematician at NYU's Courant Institute, released a statement alleging that OpenAI pressured him to downplay his progress on the Navier-Stokes problem and threatened his career if he did not comply. The statement, posted as a PDF, has sparked widespread discussion on Hacker News. This controversy raises serious concerns about corporate ethics and intellectual property in AI research, particularly regarding the use of researchers' work without permission and potential intimidation. It could impact trust in AI companies' collaborations with academia and influence discussions on AI's role in scientific discovery. Buckmaster claims OpenAI used data from his Codex sessions and publicly available information about his work to prompt their internal models, then attempted to co-opt his results. He also alleges that OpenAI misrepresented the level of human input involved, saying 'very little human input' was used when that was not true.

hackernews · procedurecall · Sep 8, 05:42 · [Discussion](https://news.ycombinator.com/item?id=49605915)

**Background**: The Navier-Stokes equations describe the motion of viscous fluids and are central to fluid dynamics. The question of whether smooth solutions always exist in three dimensions is one of the Clay Mathematics Institute's Millennium Prize Problems, with a $1 million reward. Tristan Buckmaster is a respected mathematician who won the 2019 Clay Research Award for his work on non-uniqueness of weak solutions to Navier-Stokes, making his allegations particularly significant.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Navier-Stokes_equations">Navier-Stokes equations</a></li>
<li><a href="https://cims.nyu.edu/~tristanb/">Tristan Buckmaster - NYU Courant</a></li>
<li><a href="https://www.claymath.org/people/tristan-buckmaster/">Tristan Buckmaster - Clay Mathematics Institute</a></li>

</ul>
</details>

**Discussion**: The Hacker News community expressed outrage, with one commenter saying OpenAI 'stole world class researchers' work' and then threatened them. Another commenter speculated that OpenAI may have started internal work after learning of Buckmaster and Alpoge's progress, using public info to prompt models, raising questions about the role of compute and steering in scientific discovery.

**Tags**: `#OpenAI`, `#Navier-Stokes`, `#research ethics`, `#intellectual property`, `#AI`

---

<a id="item-2"></a>
## [Researcher Factors 1990s CA's RSA Keys with Consumer GPU](https://mcpherrin.ca/2026/09/07/rsa.html) ⭐️ 8.0/10

Security researcher Matthew McPherrin factored the 512-bit RSA keys of a 1990s Certificate Authority (E-Certify) using CADO-NFS on a Ryzen 9 5950X desktop, taking 32 hours for one key and 29 hours for another. This demonstrates that such keys are now trivially breakable with modern hardware. This highlights the severe weakness of 512-bit RSA keys, which were once used in real-world CAs, and underscores the importance of using sufficiently large key sizes. It also raises concerns about the retroactive decryption of recorded encrypted traffic, as governments or attackers may store data today to decrypt it later when factoring becomes feasible. The researcher targeted root certificates from E-Certify, a CA from the 1990s, and successfully reconstructed private keys by factoring the public modulus. The factorization was performed using CADO-NFS, a general-purpose number field sieve implementation, on a consumer desktop CPU rather than specialized hardware.

hackernews · ahlCVA · Sep 8, 01:16 · [Discussion](https://news.ycombinator.com/item?id=49604637)

**Background**: RSA security relies on the difficulty of factoring large composite numbers. In the 1990s, 512-bit keys were considered secure enough for some applications, but advances in algorithms and hardware have made them breakable. The RSA Factoring Challenge, which ended in 2007, demonstrated that 512-bit keys could be factored, but this new work shows it can be done in days on a single consumer GPU.

<details><summary>References</summary>
<ul>
<li><a href="https://mcpherrin.ca/2026/09/07/rsa.html">I’ve factored the RSA keys of a Certificate Authority… | Matthew McPherrin</a></li>
<li><a href="https://en.wikipedia.org/wiki/RSA_numbers">RSA numbers - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/RSA_Factoring_Challenge">RSA Factoring Challenge - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters found the result amusing and noted the irony of the site being available over IPv6, which was also a 1990s technology. Some expressed concern about governments storing encrypted traffic for future decryption, while others appreciated the humor in the researcher's motivation and the SSL report's automatic 'F' grades.

**Tags**: `#RSA`, `#cryptography`, `#security`, `#TLS`, `#history`

---

<a id="item-3"></a>
## [Mistral Raises €3B to Boost European Sovereign Open-Weight AI](https://mistral.ai/news/mistral-makes-sovereign-open-weight-ai-to-frontier/) ⭐️ 8.0/10

Mistral AI has raised €3 billion in a new funding round to advance sovereign open-weight AI in Europe. The company aims to strengthen its position as a leading European AI lab with this significant capital injection. This funding is crucial for Europe's strategic autonomy in AI, as it supports the development of home-grown, sovereign AI capabilities. It highlights the growing importance of open-weight models and regional AI champions in a landscape dominated by US and Chinese tech giants. The €3B raise is one of the largest funding rounds for a European AI company. Mistral's annual revenue is reportedly around €700 million, which is significantly lower than competitors like Anthropic, raising questions about its ability to compete at the frontier.

hackernews · kuberwastaken · Sep 8, 05:06 · [Discussion](https://news.ycombinator.com/item?id=49605767)

**Background**: Sovereign AI refers to a country's or organization's ability to independently develop, deploy, and govern AI using its own infrastructure, data, models, and talent. Open-weight models are AI models whose core components are publicly released, allowing anyone to download and use them. Mistral is a French AI company known for releasing open-weight models, positioning itself as a European alternative to US-based labs like OpenAI and Anthropic.

<details><summary>References</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/sovereign-ai-what-actually-means-why-conversation-we-having-scott-6hese">Sovereign AI : What It Actually Means, and Why the Conversation We...</a></li>
<li><a href="https://hai.stanford.edu/ai-definitions/what-is-an-open-weight-model">What is an Open-Weight Model? - Stanford HAI</a></li>
<li><a href="https://opensource.org/ai/open-weights">Open Weights: not quite what you’ve been told</a></li>

</ul>
</details>

**Discussion**: Community comments show mixed sentiment. Some praise Mistral's contrarian strategy and its importance for European sovereignty, while others criticize its models' competitiveness, noting that its LLMs underperform compared to rivals like Gemma and Glimmer in business benchmarks. A commenter highlights that Mistral's annual revenue is a fraction of Anthropic's, questioning its ability to sustain frontier model development.

**Tags**: `#AI`, `#Mistral`, `#funding`, `#Europe`, `#sovereign AI`

---

<a id="item-4"></a>
## [D2's TALA Layout Engine Goes Open Source](https://d2lang.com/blog/tala-is-open-source/) ⭐️ 8.0/10

Terrastruct has open-sourced TALA, the proprietary layout engine for D2 diagramming language, making it freely available to all users. This move addresses a long-standing gap in automatic graph layout quality for software architecture diagrams. This is significant for the diagramming community as it provides a high-quality, purpose-built layout algorithm that outperforms general-purpose engines like ELK for architecture diagrams. It lowers the barrier for developers to create clearer, more maintainable diagrams, potentially improving documentation and system design communication. TALA is now available on GitHub under the terrastruct/TALA repository, and can be used by setting the D2_LAYOUT environment variable. It was previously a paid add-on, and its open-sourcing includes the full algorithm, not just a binary.

hackernews · alixanderwang · Sep 7, 23:37 · [Discussion](https://news.ycombinator.com/item?id=49604150)

**Background**: D2 is a modern diagram scripting language that compiles text to diagrams. Layout engines determine the automatic placement of nodes and edges; TALA was developed by Terrastruct specifically for software architecture diagrams, aiming to produce more intuitive and readable layouts than general-purpose engines like ELK or Graphviz.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/terrastruct/TALA">GitHub - terrastruct/TALA: A diagram layout engine designed specifically for software architecture diagrams · GitHub</a></li>
<li><a href="https://d2lang.com/tour/tala/">TALA | D2 Documentation</a></li>
<li><a href="https://terrastruct.com/tala/">TALA | Terrastruct's AutoLayout Approach</a></li>

</ul>
</details>

**Discussion**: Community reactions are largely positive, with users praising the improved layout quality and the move to open source. Some criticisms include a specific example where TALA's layout was less clear than ELK's, and a complaint about website compatibility on iOS Safari. Others express hope for better interactive editing tools in the future.

**Tags**: `#open-source`, `#graph-layout`, `#diagramming`, `#D2`, `#algorithm`

---

<a id="item-5"></a>
## [Jellyfin 12.0 Released with Major Improvements](https://jellyfin.org/posts/jellyfin-release-12.0/) ⭐️ 8.0/10

Jellyfin 12.0 has been officially released, introducing significant performance enhancements and new features. The release has received positive feedback from users, particularly regarding the ease of upgrade and overall performance improvements. This release is important for the self-hosted media server community, as Jellyfin continues to mature as a viable open-source alternative to proprietary solutions like Plex. The positive upgrade experience and performance gains may encourage more users to switch or adopt Jellyfin, strengthening the open-source ecosystem. Users upgrading from version 10.10.7 to 12.0 reported a quick and painless migration process, with only minor issues such as titles disappearing until a rescan. The release addresses performance issues that were present in version 10.11, making it a recommended upgrade for existing users.

hackernews · 0xC0ncord · Sep 8, 01:56 · [Discussion](https://news.ycombinator.com/item?id=49604861)

**Background**: Jellyfin is a free, open-source media server that allows users to manage and stream their personal media libraries. It is often compared to Plex, but unlike Plex, Jellyfin is fully self-hosted and does not require any proprietary server components. The project has gained popularity among privacy-conscious users and those who prefer open-source software.

**Discussion**: Community comments reflect a generally positive sentiment, with users praising the smooth upgrade process and improved performance. Some users discussed ongoing issues with subtitle handling on certain clients, while others shared their experiences integrating Jellyfin with other self-hosted tools like the *arr stack and AI assistants.

**Tags**: `#Jellyfin`, `#media server`, `#open source`, `#self-hosted`, `#release`

---

<a id="item-6"></a>
## [Linux Kernel Git Server Overwhelmed by Abusive Crawlers](https://simonwillison.net/2026/Sep/7/creepy-crawlies/) ⭐️ 8.0/10

Konstantin Ryabitsev reported that git.kernel.org, the official Linux kernel Git repository, now spends more CPU cycles rendering commits for scrapers than on all legitimate access combined, with 14 CPU cores across 5 geo-distributed nodes dedicated solely to rendering commits as HTML for crawlers. This highlights the growing problem of abusive web crawlers consuming disproportionate resources on public infrastructure, which can degrade performance for legitimate users and increase operational costs. It raises concerns for maintainers of other crawlable sites, such as Datasette, which serve large numbers of dynamic pages. The report specifies that at any one time, 14 CPU cores are busy rendering git commits as HTML for scrapers, and this exceeds the CPU usage of all other legitimate access, including git clones. The issue is described as 'background radiation' of abusive crawlers, indicating a persistent and widespread problem.

rss · Simon Willison · Sep 7, 23:08

**Background**: git.kernel.org is the official Git repository hosting the Linux kernel source code, serving developers worldwide through git clones and web-based browsing. Web crawlers, including those used by AI companies to train models, often scrape public repositories at high rates, consuming significant server resources. This issue is part of a broader trend of increasing bot traffic on the internet, which can strain infrastructure and lead to defensive measures like rate limiting or blocking.

<details><summary>References</summary>
<ul>
<li><a href="https://www.kernel.org/">The Linux Kernel Archives</a></li>
<li><a href="https://github.com/torvalds/linux">GitHub - torvalds/linux: Linux kernel source tree · GitHub</a></li>

</ul>
</details>

**Tags**: `#crawling`, `#web scraping`, `#Linux kernel`, `#resource usage`, `#Datasette`

---

<a id="item-7"></a>
## [Two Child Gene-Therapy Deaths in China Expose Regulatory Gaps](https://www.nature.com/articles/d41586-026-02497-2) ⭐️ 8.0/10

Two children died from gene therapies in China, prompting calls for stronger disclosure laws and raising concerns about the country's research reputation. The deaths occurred in less-regulated investigator-initiated trials, and China is now tightening its regulations. These deaths highlight critical safety and oversight gaps in gene therapy trials, which could undermine public trust in China's biotech sector and affect global regulatory practices. The incident may lead to stricter international scrutiny of Chinese clinical data and influence how similar trials are conducted worldwide. The deaths occurred in investigator-initiated trials, which are less regulated than standard clinical trials. China's National Medical Products Administration (NMPA) has been working to streamline approvals, but the incident has prompted U.S. lawmakers to demand FDA scrutiny of Chinese clinical data.

rss · Nature · Sep 8, 00:00

**Background**: Gene therapy aims to treat or prevent diseases by altering gene expression or modifying cells. In China, the regulatory landscape for cell and gene therapies is evolving rapidly, with the NMPA offering fast-track approvals. However, investigator-initiated trials may have less oversight, leading to safety concerns.

<details><summary>References</summary>
<ul>
<li><a href="https://www.forbes.com/sites/williamhaseltine/2026/08/10/two-deaths-in-china-reopen-gene-therapy-debates/">2 Deaths In China Reopen Gene Therapy Debates</a></li>
<li><a href="https://www.caixinglobal.com/2026-08-25/patient-deaths-in-china-trials-spur-us-demand-for-fda-scrutiny-102477641.html">Patient Deaths in China Trials Spur U.S. Demand for FDA Scrutiny - Caixin Global</a></li>
<li><a href="https://aoxya.com/cell-and-gene-therapy-regulatory-landscape-asia/">Cell & Gene Therapy : Regulatory Landscape Across Asia - Aoxya</a></li>

</ul>
</details>

**Discussion**: The Forbes article notes that experts stress the importance of prompt disclosure and honest investigation of fatalities to maintain public trust. Some U.S. lawmakers are demanding FDA scrutiny of Chinese clinical data, reflecting concerns about data reliability.

**Tags**: `#gene therapy`, `#China`, `#biotech regulation`, `#clinical trials`, `#safety`

---

<a id="item-8"></a>
## [Tiny RNN Autonomously Generates Bad Apple Video from Single Initial State](https://www.reddit.com/r/MachineLearning/comments/1wa8rub/generating_bad_apple_autonomously_from_a_single/) ⭐️ 8.0/10

A compact recurrent neural network with only 417,129 parameters autonomously generates the entire ~6,500-frame Bad Apple video from a single initial state (h_0, c_0), without any timestamp inputs. The system uses a 4-gate LSTM-style transition and a frame decoder, achieving over 200 FPS on an RTX 4080. This work demonstrates that a small recurrent dynamical system can learn to generate long video sequences autonomously, contrasting with typical approaches that require explicit time conditioning or large autoregressive models. It highlights the potential of compact, self-sustaining latent dynamics for efficient video generation and could inspire new directions in memory-efficient temporal modeling. The training uses learned latent teacher tables (h_table[t], c_table[t]) that are discarded at inference, a rollout horizon curriculum doubling from K=2 to K=512, state perturbation noise (sigma=0.005), and second-difference acceleration regularization to ensure smooth trajectories. The model generalizes to the full 6,573 frames despite being trained on segments up to 512 frames, and the lowest training loss checkpoint was not necessarily the best for autonomous rollout.

reddit · r/MachineLearning · /u/SEBADA321 · Sep 8, 00:05

**Background**: Bad Apple is a popular music video often used as a benchmark for video processing and generation tasks. The work builds on SIREN, an implicit neural representation that maps coordinates (t, y, x) to pixel values, but instead of providing the time t as input, the model learns a recurrent dynamical system in latent space that evolves autonomously. This approach treats video generation as a dynamical process, similar to recent state-space models like VideoSSM, but with a much smaller footprint.

<details><summary>References</summary>
<ul>
<li><a href="https://www.vincentsitzmann.com/siren/">Implicit Neural Representations with Periodic Activation Functions</a></li>
<li><a href="https://arxiv.org/html/2512.04519v1">VideoSSM: Autoregressive Long Video Generation with Hybrid State-Space Memory</a></li>

</ul>
</details>

**Tags**: `#recurrent neural networks`, `#video generation`, `#dynamical systems`, `#machine learning`, `#Bad Apple`

---

<a id="item-9"></a>
## [Rustuna: High-Performance Rust Implementation of Optuna](https://www.reddit.com/r/MachineLearning/comments/1w9nyhz/rustuna_a_highperformance_rust_implementation_of/) ⭐️ 8.0/10

The Optuna team has released Rustuna, a high-speed, memory-efficient implementation of Optuna written in Rust, designed to be API-compatible with the original Python framework while eliminating Python dependencies. The announcement was made on Reddit and accompanied by a blog post detailing the new tool. Rustuna addresses critical concerns in the ML community, such as supply chain security and memory efficiency, by removing Python dependencies and leveraging Rust's native memory management. This could attract Rust developers to hyperparameter optimization and offer a more secure and performant alternative for production environments. Rustuna is designed to keep the familiar API and concept of Optuna, ensuring a smooth transition for existing users. It is available on GitHub under the Optuna organization, and the project emphasizes zero Python dependencies to mitigate supply chain attack risks.

reddit · r/MachineLearning · /u/c-bata · Sep 7, 10:01

**Background**: Optuna is a popular open-source hyperparameter optimization framework for machine learning, known for its define-by-run API and framework-agnostic design. Supply chain attacks target vulnerabilities in third-party dependencies, and by removing Python dependencies, Rustuna reduces the attack surface. Rust's memory safety and performance characteristics make it an attractive choice for building efficient tools.

<details><summary>References</summary>
<ul>
<li><a href="https://optuna.org/">Optuna - A hyperparameter optimization framework</a></li>
<li><a href="https://github.com/optuna/optuna">GitHub - optuna / optuna : A hyperparameter optimization framework</a></li>
<li><a href="https://optuna.readthedocs.io/en/stable/index.html">Optuna : A hyperparameter optimization framework — Optuna ...</a></li>

</ul>
</details>

**Tags**: `#Rust`, `#Optuna`, `#Hyperparameter Optimization`, `#Machine Learning`, `#Performance`

---

<a id="item-10"></a>
## [LLM-guided program evolution improves 10 circle-packing solutions](https://www.reddit.com/r/MachineLearning/comments/1w9xlyi/llmguided_program_evolution_improves_10_bestknown/) ⭐️ 8.0/10

An LLM-guided program evolution approach improved the best-known sum-of-radii for 10 values of N (101-114) on the Packomania csqv benchmark, achieving gains of 2.4-5.4% at a total LLM cost of $27.72. The results were independently accepted by Packomania. This demonstrates a novel and cost-effective use of LLMs for program evolution, showing that LLMs can help discover algorithmic improvements for challenging optimization problems. The independent verification by Packomania adds credibility and could inspire similar approaches in other optimization domains. The method starts from a simple seed solver and iteratively proposes algorithmic changes guided by a scoreboard and history, with each candidate scored by an independent verifier. The improvement was achieved in 15 iterations, and the author specifically invites critique on the plateau-detection stopping rule.

reddit · r/MachineLearning · /u/SIGH_I_CALL · Sep 7, 16:54

**Background**: Circle packing is a classic optimization problem where the goal is to pack circles within a container to maximize or minimize a certain objective, such as the sum of radii. Packomania is a well-known benchmark repository for such problems. LLM-guided program evolution is a technique where a large language model proposes modifications to program code, which are then evaluated and selected based on performance, enabling automated discovery of better algorithms.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2609.05093">LLM - Guided Program Evolution for Circle Packing:Breaking 10...</a></li>
<li><a href="https://packomania.com/">Packomania (52C17)</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#program evolution`, `#optimization`, `#circle packing`, `#benchmark`

---

<a id="item-11"></a>
## [Yandex Research Proposes KV Cache as Agent Runtime for Interactive LLMs](https://www.reddit.com/r/MachineLearning/comments/1w9myqc/kv_cache_as_an_agent_runtime_r/) ⭐️ 8.0/10

Yandex Research has published a blog post and demo exploring the use of the KV cache as an agent runtime, building on their previous work on Hogwild! Inference and AsyncReasoning. They demonstrate a Qwen3.8-27B agent playing DOOM interactively using these techniques. This research introduces a novel axis for improving LLM agent capabilities by modifying the inference state (KV cache) rather than the model or harness. It could lead to more interactive and responsive LLM systems, impacting fields like real-time AI applications and agent design. The approach leverages Rotary Position Embeddings (RoPE) to enable concurrent attention and avoid recomputation, as detailed in Hogwild! Inference. AsyncReasoning allows the LLM to determine synchronization points, enabling training-free asynchronous reasoning. The demo shows a Qwen3.8-27B agent playing DOOM interactively.

reddit · r/MachineLearning · /u/_puhsu · Sep 7, 09:03

**Background**: KV cache stores intermediate key-value pairs during LLM inference to avoid recomputation, but it is typically managed at a coarse level. Traditional approaches to improving LLM interactivity involve changing the model or the harness, which can be costly or abstract. This research explores modifying the KV cache directly as a runtime for agents, potentially offering a middle ground between model changes and harness abstraction.

<details><summary>References</summary>
<ul>
<li><a href="https://research.yandex.com/publications/hogwild-inference-parallel-llm-generation-via-concurrent-attention">Hogwild ! Inference : Parallel LLM Generation via Concurrent Attention</a></li>
<li><a href="https://arxiv.org/abs/2504.06261">Hogwild ! Inference : Parallel LLM Generation via Concurrent Attention</a></li>
<li><a href="https://arxiv.org/html/2512.10931v1">Asynchronous Reasoning : Training-Free Interactive Thinking LLMs</a></li>

</ul>
</details>

**Tags**: `#KV cache`, `#LLM inference`, `#agent runtime`, `#interactive AI`, `#research`

---

<a id="item-12"></a>
## [Australia's 'My Feed, My Way' to Let Users Opt Out of Algorithms](https://www.pm.gov.au/media/my-feed-my-way) ⭐️ 7.0/10

The Australian Prime Minister announced the 'My Feed, My Way' initiative, which will give Australians the ability to opt out of social media algorithms that curate their feeds. This forms part of new legislation aimed at boosting online safety and user control. This policy could set a global precedent for regulating algorithmic content curation, potentially forcing major tech platforms to offer chronological or user-selected feed options. It addresses growing concerns about the impact of algorithms on mental health, polarization, and the spread of harmful content. The initiative is part of a broader 'digital duty of care' framework, and it is unclear whether it will mandate a strict chronological order option or simply allow users to disable algorithmic recommendations. The legislation is expected to be introduced in the Australian parliament, with details still being finalized.

hackernews · dotcoma · Sep 8, 05:10 · [Discussion](https://news.ycombinator.com/item?id=49605782)

**Background**: Social media platforms like Facebook, Instagram, and TikTok use algorithms to rank and select content for each user's feed, often prioritizing engagement over user well-being. Critics argue these algorithms can amplify sensational or divisive content, contributing to addiction and social harm. Australia has been proactive in regulating tech, including a previous ban on social media for under-16s, and this new initiative continues that trend.

<details><summary>References</summary>
<ul>
<li><a href="https://www.theguardian.com/australia-news/2026/sep/08/australia-social-media-algorithm-switch-off-opt-out-digital-duty-of-care">‘Global reckoning for big tech’: Australia to force social media ...</a></li>
<li><a href="https://www.pm.gov.au/media/my-feed-my-way">My feed , My Way | Prime Minister of Australia</a></li>
<li><a href="https://sg.news.yahoo.com/australia-targets-social-media-algorithms-040904171.html">Australia targets social media algorithms with new user-choice rules</a></li>

</ul>
</details>

**Discussion**: Community comments express mixed views: some support the initiative as a step toward reducing addiction and giving users control, while others question its effectiveness, noting that many users may not choose to opt out or that algorithms are a key reason for platforms' popularity. Some suggest alternative approaches, such as legalizing scraping to enable third-party frontends, and others point out the Prime Minister's past comments about banning social media, questioning the sincerity of the current policy.

**Tags**: `#social media`, `#regulation`, `#algorithms`, `#Australia`, `#policy`

---

<a id="item-13"></a>
## [Google's Algorithm Creates 'Google Jail' for Independent Wikis](https://weirdgloop.org/blog/google-jail) ⭐️ 7.0/10

An article from Weird Gloop argues that Google's search algorithm is suppressing independent wikis in favor of larger platforms like Fandom, effectively placing them in a 'Google Jail' that harms niche content discoverability. This issue affects the discoverability of niche, community-driven wikis, potentially reducing traffic and contributions. It highlights a broader trend where algorithmic bias favors established platforms, undermining the independent web and content diversity. The article references community tools like IndieWikiBuddy, which redirects search results from Fandom to independent alternatives. It also notes that Google Search Console may index only a fraction of pages from new niche sites, and that Fandom's SEO dominance makes it hard for independent wikis to compete.

hackernews · pizzaiolo · Sep 8, 01:57 · [Discussion](https://news.ycombinator.com/item?id=49604870)

**Background**: Google's search algorithm uses various signals to rank pages, and algorithmic suppression can occur when sites are deemed less authoritative or relevant, often following core updates. Fandom, a wiki hosting platform backed by private equity, has strong SEO due to its large user base and established domain authority, making it difficult for independent wikis to rank well. Independent wikis often provide higher-quality, ad-free content but struggle to gain visibility in search results.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Fandom_(website)">Fandom (website) - Wikipedia</a></li>
<li><a href="https://news.ycombinator.com/item?id=42571558">Wikis are great, but it feels like outside of Wikipedia ... | Hacker News</a></li>
<li><a href="https://atlasleads.io/resources/blog/google-algorithmic-penalty">Recover From Google Algorithmic Penalty: Recovery Guide — Atlas...</a></li>

</ul>
</details>

**Discussion**: Commenters shared mixed sentiments. Some praised tools like IndieWikiBuddy for redirecting to independent wikis, while others expressed frustration with Google's indexing issues and Fandom's ad practices. One commenter questioned whether visibility in Google is necessary for wiki success, suggesting that invisibility might even improve contribution quality.

**Tags**: `#Google Search`, `#Wikis`, `#SEO`, `#Content Discovery`, `#Independent Web`

---

<a id="item-14"></a>
## [Interactive Map Visualizes LA Building Construction Timeline (1880-2026)](https://lax-skyline.parcelscope.net/) ⭐️ 7.0/10

An interactive map at lax-skyline.parcelscope.net visualizes the construction timeline of buildings in Los Angeles from 1880 to 2026, allowing users to explore urban development over time. The tool has gained significant community attention with 286 points and 141 comments. This visualization provides a unique perspective on urban planning and zoning policies, highlighting how historical decisions like the 1980s downzoning have shaped LA's current affordability crisis. It serves as a valuable resource for urban studies, data visualization enthusiasts, and policymakers. The map is based on data from the Los Angeles County Assessor's portal, showing only buildings that are still standing, which may underrepresent historical neighborhoods that have been completely replaced. The tool covers a period from 1880 to 2026, with the future date likely indicating planned or ongoing construction.

hackernews · rustywasm · Sep 7, 18:52 · [Discussion](https://news.ycombinator.com/item?id=49601655)

**Background**: Los Angeles has a complex urban history, including a once-extensive public transportation network of over 1,300 miles that was largely paved over. The city's zoning policies, particularly the massive downzoning in the 1980s, have been criticized for restricting housing supply and contributing to high costs. Interactive maps like this help visualize such long-term changes.

**Discussion**: Community comments highlight the map's limitation of only showing surviving buildings, making older periods appear empty. Discussions also touch on LA's transit history and the impact of zoning policies on affordability, with some users praising the tool while others note its data source constraints.

**Tags**: `#data visualization`, `#urban planning`, `#Los Angeles`, `#history`, `#interactive map`

---

<a id="item-15"></a>
## [Broadcom Pulls VDDK Downloads, Complicating VMware Migration](https://www.virtualizationhowto.com/2026/09/leaving-vmware-just-got-harder-after-broadcom-pulled-vddk-downloads/) ⭐️ 7.0/10

Broadcom has removed downloads of the VMware Virtual Disk Development Kit (VDDK), a key tool used for accessing virtual disk data during migrations. This move further restricts VMware users' ability to migrate to other virtualization platforms. This development significantly hampers organizations planning to leave VMware, as VDDK is essential for many third-party backup and migration tools. It reflects Broadcom's ongoing strategy to monetize VMware assets, potentially accelerating customer churn and impacting the broader virtualization ecosystem. VDDK is a collection of C/C++ libraries and APIs that enable creation and access to VMware virtual disks. While VMware-to-Proxmox migrations are reportedly unaffected, tools relying on VDDK for cross-platform migrations may face compatibility issues or require alternative methods.

hackernews · josephcsible · Sep 7, 20:32 · [Discussion](https://news.ycombinator.com/item?id=49602699)

**Background**: VMware Virtual Disk Development Kit (VDDK) is an SDK that allows developers and partners to build applications for virtual disk storage access. It is commonly used by backup and migration solutions to read VMware virtual disks. Broadcom acquired VMware in 2023 and has since made controversial changes to licensing and product availability, leading to customer dissatisfaction and increased interest in alternative platforms.

<details><summary>References</summary>
<ul>
<li><a href="https://www.infoworld.com/article/2310788/vmware-helps-developers-with-a-new-virtual-disk-development-kit.html">VMware helps developers with a new Virtual Disk ... | InfoWorld</a></li>
<li><a href="https://news.ycombinator.com/item?id=49602699">Leaving VMware just got harder after Broadcom pulled VDDK downloads</a></li>

</ul>
</details>

**Discussion**: Community comments express sadness and frustration over Broadcom's handling of VMware, with former engineers lamenting the loss of innovation. Some users share personal migration experiences, noting that moving to alternatives like Proxmox was relatively painless, while others jokingly suggest preserving VMware's source code for future resurrection.

**Tags**: `#VMware`, `#Broadcom`, `#Virtualization`, `#Migration`, `#VDDK`

---

<a id="item-16"></a>
## [OpenAI Chief Scientist Advocates Defensive AI, Warns Against Reckless Racing](https://simonwillison.net/2026/Sep/7/jakub-pachocki/) ⭐️ 7.0/10

OpenAI Chief Scientist Jakub Pachocki publicly argued that powerful, aligned AI is needed for defensive purposes against threats from other AI, while cautioning that this necessity must not justify reckless acceleration of AI development. This statement reflects high-level strategic thinking within OpenAI about balancing AI progress with safety, potentially influencing policy debates and industry practices regarding AI development and deployment. Pachocki emphasized that defensive AI will be a primary focus of OpenAI's deployment efforts, including securing infrastructure and protecting against rogue agents in real time. He also stressed that the seriousness of the stakes makes racing forward at all costs seem absurd.

rss · Simon Willison · Sep 7, 22:26

**Background**: AI alignment refers to ensuring AI systems act in accordance with human intentions and values. OpenAI has been increasingly involved in defense-related projects, such as a reported $200 million contract with the U.S. Department of Defense, highlighting the growing intersection of advanced AI and national security.

<details><summary>References</summary>
<ul>
<li><a href="https://www.linkedin.com/posts/ai-tech-evangelism_openai-defense-ai-activity-7341202817925140480-RqUQ"># openai # defense # ai #government #innovation #microsoft</a></li>
<li><a href="https://en.wikipedia.org/wiki/Artificial_intelligence">Artificial intelligence - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AI safety`, `#OpenAI`, `#AI ethics`, `#AI policy`

---

<a id="item-17"></a>
## [EmbedFlow: Zero-Downtime Embedding Model Migration](https://www.reddit.com/r/MachineLearning/comments/1wabmm7/my_lab_found_a_way_to_migrate_between_embedding/) ⭐️ 7.0/10

A research lab introduced EmbedFlow, a method that allows migrating between embedding models without re-embedding all documents. It reranks a subset of documents from the old index to match the target model's retrieval quality, tested on up to 1 million documents. This addresses a critical pain point in RAG systems where upgrading embedding models typically requires expensive and time-consuming backfill of all vectors. By enabling zero-downtime migration, it could significantly reduce costs and downtime for organizations managing large-scale vector databases. The method involves taking K documents from the old index and reranking them with the new model; when K is sufficient, retrieval quality matches the target model. The best result was upgrading from Qwen 4B to 8B, achieving parity with native retrieval at just 50 documents. EmbedFlow works with Qdrant and is available via pip install embedflow, with public GitHub repository.

reddit · r/MachineLearning · /u/Potential_Low_1183 · Sep 8, 02:16

**Background**: Embedding models convert text into vector representations for retrieval-augmented generation (RAG) systems, enabling semantic search. When upgrading to a better model, all documents must be re-embedded, which is computationally intensive; for example, re-embedding a billion documents on an H100 could take about 108 days. Reranking is a technique where a model re-scores a set of candidate documents to improve retrieval accuracy, which EmbedFlow leverages to avoid full backfill.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/arnsri33/embedflow">GitHub - arnsri33/ embedflow : Zero downtime embedding upgrades</a></li>

</ul>
</details>

**Tags**: `#embeddings`, `#RAG`, `#model migration`, `#vector databases`, `#machine learning`

---

<a id="item-18"></a>
## [AI Threat Spurs Call for Year-Long Global Security Fix](https://jyn.dev/a-year-to-fix-security/) ⭐️ 6.0/10

The article argues that the rise of AI necessitates a year-long global effort to fix security vulnerabilities, suggesting a timeline for action. This matters because AI could amplify cyber threats, making proactive security fixes urgent. The discussion highlights skepticism about the practicality and urgency of such a broad initiative. The article references an Apple M5 Mac Studio with 256 GB of unified memory, but commenters note that LLM performance on such hardware is slower than implied. The author suggests a one-year window before AI exacerbates security issues.

hackernews · saikatsg · Sep 8, 04:48 · [Discussion](https://news.ycombinator.com/item?id=49605691)

**Background**: The article is set in the context of growing concerns about AI's potential to automate cyberattacks or lower the barrier for malicious activities. It calls for a coordinated, time-bound effort to address systemic security weaknesses before AI capabilities advance further.

**Discussion**: Commenters express mixed views: some question the urgency, noting that dangerous information is already available; others criticize the lack of historical security investment and suggest simplifying systems as a first step. A few offer sarcastic or positive spins on the timeline.

**Tags**: `#security`, `#AI`, `#LLM`, `#cybersecurity`

---

<a id="item-19"></a>
## [llm 0.35 Adds Support for OpenAI's GPT-6 Astra](https://simonwillison.net/2026/Sep/7/llm/) ⭐️ 6.0/10

llm 0.35 has been released, adding support for OpenAI's new GPT-6 Astra model via the model identifier 'gpt-6-astra'. This is a minor release focused on integrating the latest OpenAI flagship model. This release keeps the llm tool current with OpenAI's latest model offerings, enabling users to leverage GPT-6 Astra's advanced capabilities in their workflows. It matters for developers and researchers who rely on llm as a versatile command-line interface for interacting with various language models. The release notes only mention the addition of the new model, with no other changes listed. GPT-6 Astra is positioned as OpenAI's flagship model for demanding end-to-end tasks, including advanced analysis, software engineering, and long-horizon agentic tasks.

rss · Simon Willison · Sep 7, 23:54

**Background**: llm is a command-line tool created by Simon Willison that provides a unified interface for interacting with multiple large language models from different providers. OpenAI's GPT-6 Astra is the latest iteration in the GPT series, succeeding GPT-5 and offering improvements in areas like computer use and agentic capabilities. This release allows llm users to directly access GPT-6 Astra through the tool.

<details><summary>References</summary>
<ul>
<li><a href="https://minifeed.net/items/79hyqBEFMFVl">llm 0 . 35 | Simon Willison's Weblog | minifeed</a></li>
<li><a href="https://openrouter.ai/openai/gpt-6-astra">GPT - 6 Astra - API Pricing & Benchmarks | OpenRouter</a></li>
<li><a href="https://www.vellum.ai/blog/gpt-6-astra-benchmarks-explained">GPT - 6 Astra Benchmarks Explained</a></li>

</ul>
</details>

**Tags**: `#llm`, `#OpenAI`, `#GPT-6`, `#release`

---

<a id="item-20"></a>
## [Simon Willison Builds WebAssembly FFmpeg Video Compressor](https://simonwillison.net/2026/Sep/7/video-compressor/) ⭐️ 6.0/10

Simon Willison released a web-based video compressor tool built with the WebAssembly build of FFmpeg, which he used to optimize a demo video for his blog. The tool generates multiple compressed versions of a video directly in the browser, with presets ranging from 'Largest' to 'Smallest'. This tool demonstrates the practicality of running FFmpeg entirely in the browser via WebAssembly, enabling client-side video compression without uploading files to a server. It is useful for developers and content creators who want to optimize videos for the web while preserving privacy and reducing server load. The tool offers five presets with output resolutions of 854×370 or 640×276, CRF quality settings from 22 to 28, and audio bitrates from 128 to 64 kbps. It also includes options for encoder speed, H.264 profile, 30 fps limit, stripping metadata, dropping audio, and encoding only the first 10 seconds.

rss · Simon Willison · Sep 7, 18:29

**Background**: FFmpeg is a powerful command-line tool for handling multimedia files, and WebAssembly allows C/C++ code to run in web browsers. The ffmpeg.wasm project provides a pure WebAssembly/JavaScript port of FFmpeg, enabling browser-based video processing. CRF (Constant Rate Factor) is a key compression setting that controls the quality-to-size tradeoff, with lower values indicating higher quality.

<details><summary>References</summary>
<ul>
<li><a href="https://ffmpegwasm.netlify.app/docs/overview/">Overview | ffmpeg .wasm</a></li>
<li><a href="https://github.com/ffmpegwasm/ffmpeg.wasm">GitHub - ffmpegwasm/ ffmpeg .wasm: FFmpeg for browser, powered by...</a></li>
<li><a href="https://www.squeezevid.com/en/blog/video-compression-settings-explained/">Video Compression Settings Explained: CRF , Bitrate... - SqueezeVid</a></li>

</ul>
</details>

**Tags**: `#FFmpeg`, `#WebAssembly`, `#video compression`, `#developer tools`

---

<a id="item-21"></a>
## [Animated Mercator to Equal Earth Transition Tool Built with D3 and GPT-6 Astra](https://simonwillison.net/2026/Sep/7/equal-earth/) ⭐️ 6.0/10

Simon Willison released an interactive tool that animates the transition between the Mercator and Equal Earth map projections, built using D3 and GPT-6 Astra (medium) in ChatGPT Work. This follows a recent UN vote encouraging the use of equal-area projections like Equal Earth. This tool makes the distortion differences between common map projections visually accessible, helping users understand why equal-area projections matter. It also demonstrates the growing capability of AI-assisted coding for creating interactive geospatial visualizations. The tool is hosted at tools.simonwillison.net/equal-earth and includes a video preview. It was generated via a ChatGPT share link, and the code likely uses D3's geo projection interpolation techniques.

rss · Simon Willison · Sep 7, 16:24

**Background**: The Mercator projection, developed for nautical navigation, preserves angles but severely distorts area, making landmasses near the poles appear much larger than they are. The Equal Earth projection, invented in 2018, is an equal-area pseudocylindrical projection that preserves relative sizes of regions, inspired by the Robinson projection but without its area distortion. In September 2026, the UN General Assembly voted on a resolution encouraging the use of equal-area projections, which brought attention to Equal Earth.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Equal_Earth_map_projection">Equal Earth map projection</a></li>
<li><a href="https://en.wikipedia.org/wiki/Mercator_projection">Mercator projection - Wikipedia</a></li>
<li><a href="https://gist.github.com/mbostock/3711652">Projection Transitions · GitHub</a></li>

</ul>
</details>

**Tags**: `#geospatial`, `#D3`, `#AI-assisted coding`, `#map projections`

---

<a id="item-22"></a>
## [Proposal: Stockfish-like Decision Quality and Anti-Cheat for Dynamic Games](https://www.reddit.com/r/MachineLearning/comments/1wadyz7/what_if_competitive_games_such_as_rocket_league/) ⭐️ 6.0/10

A Reddit user proposed using offline RL (Trajectory Transformers, Implicit Q-Learning) over a Sequential POMDP to evaluate decision quality in dynamic games like Rocket League, and using FFT and NLL divergence for anti-cheat and smurf detection. The proposal is speculative and lacks implementation. If realized, such a system could provide objective performance metrics for esports players, akin to chess's Stockfish, and enhance anti-cheat measures. It could influence future game analytics and anti-cheat research, though it faces significant technical hurdles. The proposal suggests slicing replays into 5-second rollouts but pivots to offline RL to avoid chaotic physics simulations. It also mentions using frequency spectrum analysis (FFT) on input signals and kinematic limits (4th derivative/Snap) to catch bots, and NLL divergence to flag smurfs.

reddit · r/MachineLearning · /u/Ligras · Sep 8, 04:11

**Background**: Stockfish is a chess engine that evaluates positions with high accuracy, but dynamic games like Rocket League involve continuous physics and partial observability, making similar evaluation challenging. Offline RL learns from pre-collected data without live interaction, and POMDP models handle partial observability. Anti-cheat systems often use behavioral analysis, but advanced methods like FFT and NLL divergence are less common.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2110.06169">[2110.06169] Offline Reinforcement Learning with Implicit Q - Learning</a></li>
<li><a href="https://liner.com/review/offline-reinforcement-learning-as-one-big-sequence-modeling-problem">Offline Reinforcement Learning as One Big Sequence Modeling...</a></li>
<li><a href="https://www.emergentmind.com/topics/goal-conditional-partially-observable-markov-decision-process-pomdp">Goal-Conditional POMDP in Sequential Decisions</a></li>

</ul>
</details>

**Discussion**: No comments were provided in the news item, so community sentiment is unknown.

**Tags**: `#reinforcement learning`, `#game analytics`, `#anti-cheat`, `#offline RL`, `#esports`

---
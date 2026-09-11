---
layout: default
title: "Horizon Summary: 2026-09-11 (EN)"
date: 2026-09-11
lang: en
---

> From 27 items, 14 important content pieces were selected

---

1. [Shopify abandons React Native for native Swift and Kotlin](#item-1) ⭐️ 8.0/10
2. [OpenAI Launches Managed Agents API with Self-Hosted Sandbox Option](#item-2) ⭐️ 8.0/10
3. [Astra for Coding Critiqued as AI Agents Degrade Code Quality](#item-3) ⭐️ 8.0/10
4. [Forgejo 16.0.4 Fixes Critical RCE in Template Repositories](#item-4) ⭐️ 8.0/10
5. [PlanetScale Launches Neki, a Sharded Postgres Solution](#item-5) ⭐️ 8.0/10
6. [trynix.dev runs any Nix package in the browser via qemu-wasm](#item-6) ⭐️ 8.0/10
7. [Four-Color Theorem Gets a Rare New Proof](#item-7) ⭐️ 8.0/10
8. [WebGL 'Deathray' lets untrusted sites freeze Macs](#item-8) ⭐️ 7.0/10
9. [NASA's Decorrelation Stretch Reveals Ancient Rock Art](#item-9) ⭐️ 7.0/10
10. [Cognition launches SWE-2 coding model, claiming frontier-level performance](#item-10) ⭐️ 7.0/10
11. [Open-source 'Proof of Capture' uses steganography to prove image authenticity](#item-11) ⭐️ 7.0/10
12. [Datasette 1.0a39 and 0.65.4 Fix AI-Discovered Security Bugs](#item-12) ⭐️ 7.0/10
13. [ACL Proposes Sustainable Reviewing Policy with Submission Caps](#item-13) ⭐️ 7.0/10
14. [Free Open Music Theory Textbook Sparks Debate on Classical Focus](#item-14) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Shopify abandons React Native for native Swift and Kotlin](https://shopify.engineering/back-to-native) ⭐️ 8.0/10

Shopify announced it is migrating its mobile app from React Native back to fully native Swift (iOS) and Kotlin (Android) codebases. The engineering blog post details the reversal, which has triggered a large Hacker News discussion with over 1,000 points and 700 comments. This is a significant signal for the mobile development industry, as a major e-commerce company with thousands of engineers is publicly reversing a high-profile cross-platform bet. It could influence other large-scale apps reconsidering React Native, especially regarding engineering team efficiency and long-term maintenance costs. The migration involves rewriting the app in Swift and Kotlin, which are the dominant native languages for iOS and Android respectively. Notably, community members report using AI tools like Codex to automate large portions of similar migrations, suggesting the process may be faster than traditional rewrites.

hackernews · fnthawar2 · Sep 10, 14:09 · [Discussion](https://news.ycombinator.com/item?id=49643982)

**Background**: React Native is an open-source framework created by Facebook that lets developers build mobile apps for both iOS and Android using JavaScript and React. Native development, in contrast, uses platform-specific languages like Swift for iOS and Kotlin for Android, typically offering better performance and deeper access to device features but requiring separate codebases. Shopify's move reflects a broader debate over whether cross-platform frameworks can match native performance and maintainability at scale.

<details><summary>References</summary>
<ul>
<li><a href="https://reactnative.dev/">React Native · Learn once, write anywhere</a></li>
<li><a href="https://kotlinlang.org/docs/multiplatform/kotlin-multiplatform-react-native.html">Kotlin Multiplatform vs. React Native: A cross-platform comparison | Kotlin Multiplatform Documentation</a></li>
<li><a href="https://www.techrev.us/blog/swift-vs-kotlin-for-native-app-development/">Swift vs Kotlin: Native App Development Compared (2026 Guide ...</a></li>

</ul>
</details>

**Discussion**: The Hacker News discussion is highly engaged, with many commenters questioning Shopify's engineering efficiency given its 3,000 engineers, while others share successful AI-assisted migrations from React Native to native. A key counterpoint raised is that React Native's over-the-air update capability is a major advantage that native development lacks, and that performance gains from native are minimal for typical UIs.

**Tags**: `#React Native`, `#Mobile Development`, `#Swift`, `#Kotlin`, `#Engineering Management`

---

<a id="item-2"></a>
## [OpenAI Launches Managed Agents API with Self-Hosted Sandbox Option](https://developers.openai.com/api/docs/guides/agents-api/overview) ⭐️ 8.0/10

OpenAI released an Agents API in public beta that lets developers add agentic capabilities to their products without managing sandboxes or reliability infrastructure, and it includes an option to self-host the sandbox. The API is a managed Codex harness that runs the agent loop for you, handling long-running tasks and saving progress. This is a significant platform-level move that lowers the barrier to building agentic applications, potentially disrupting startups that monetize similar sandbox and orchestration services. It also signals that managed agent infrastructure is becoming a standard offering from major AI providers. The self-hosted sandbox option is a notable detail because it reduces vendor lock-in and eases migration between providers. The API is aimed at long-running tasks where OpenAI manages the agent and saves its progress, while developers can still plug in custom tools and workflows.

hackernews · aquir · Sep 10, 19:43 · [Discussion](https://news.ycombinator.com/item?id=49649213)

**Background**: Agentic capabilities refer to AI systems that can autonomously perceive context, make decisions, and act toward goals, often over multiple steps. Building such agents typically requires a harness that runs the agent loop, a sandbox for safe code execution, and infrastructure for reliability and state persistence. OpenAI's Agents API packages these pieces as a managed service, similar to how cloud platforms abstract away servers.

<details><summary>References</summary>
<ul>
<li><a href="https://developers.openai.com/api/docs/guides/agents">Agents | OpenAI API</a></li>
<li><a href="https://www.creativeainews.com/articles/openai-agents-api-vs-claude-managed-agents-2026/">OpenAI Agents API vs Claude Managed Agents</a></li>
<li><a href="https://www.beam.cloud/blog/how-to-self-host-code-sandbox">How to Self - Host a Code Execution Sandbox for AI Agents... | Beam</a></li>

</ul>
</details>

**Discussion**: Commenters see this as a stepping stone to the next big thing that could destroy startups monetizing the same idea, while others highlight the self-hosted sandbox option as reducing lock-in. Some note that developers can already run agents in their own VMs, and there is debate about the right abstraction for offering agents as a product.

**Tags**: `#openai`, `#agents`, `#api`, `#ai-infrastructure`, `#developer-tools`

---

<a id="item-3"></a>
## [Astra for Coding Critiqued as AI Agents Degrade Code Quality](https://lucumr.pocoo.org/2026/9/7/astra-why/) ⭐️ 8.0/10

A critical blog post on lucumr.pocoo.org questions whether Astra, OpenAI's GPT-6-based coding agent, actually improves developer outcomes, arguing that reinforcement learning rewards for long-horizon task success come with little penalty for producing poor-quality code. The post sparked a 279-point Hacker News discussion with 185 comments, where practitioners reported that Astra generates excessive documentation, scripts, and review workflows while making little real progress on actual application code. This critique matters because it challenges the prevailing narrative that AI coding agents are steadily improving, and it points to a structural incentive problem in RL training that could affect every developer relying on tools like Astra, Claude, or Copilot. If models are optimized for long-horizon task completion rather than maintainable code, the resulting technical debt could slow teams down rather than speed them up. Commenters note that Astra costs roughly $7.09 per task at maximum effort on Artificial Analysis's Coding Agent Index, about 15% more than GPT-5.6 Sol for a 7-point higher score, yet one user reported that after two days Astra had produced only docs, scripts, and PR reviews for a simple MVP that a senior engineer would have finished faster with better code. The core technical suspicion is that both OpenAI and Anthropic shifted their RL objectives from human-rated usefulness to long-horizon task success, with weak penalties for messy code.

hackernews · manojbajaj95 · Sep 11, 06:23 · [Discussion](https://news.ycombinator.com/item?id=49654229)

**Background**: Astra is OpenAI's GPT-6-based coding agent, positioned as a state-of-the-art tool for autonomous software development. Reinforcement learning (RL) is a training technique where models are rewarded for desired outcomes; in the case of coding agents, the reward is typically task completion over many steps, known as long-horizon tasks. The term 'involution' (内卷, neijuan) referenced in the discussion describes a system demanding ever more effort without improving actual output, a concept originally from Clifford Geertz's study of agricultural intensification.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/gpt-6-astra/">GPT-6 Astra: A new generation of intelligence | OpenAI</a></li>
<li><a href="https://artificialanalysis.ai/articles/benchmarking-gpt-6-astra">Benchmarking GPT-6 Astra | Artificial Analysis</a></li>
<li><a href="https://spectrum.ieee.org/ai-coding-degrades">AI Coding Degrades: Silent Failures Emerge - IEEE Spectrum</a></li>

</ul>
</details>

**Discussion**: The Hacker News discussion was broadly sympathetic to the critique, with practitioners sharing that messy AI-generated code compounds over time and eventually grinds progress to a halt, contradicting claims that developers no longer need to read code. Several commenters argued that the shift in RL incentives toward long-horizon task success explains the degradation, and one invoked the concept of 'involution' to describe AI engineering as ever-increasing effort without improved output.

**Tags**: `#ai-coding-agents`, `#llm`, `#software-engineering`, `#reinforcement-learning`, `#developer-tools`

---

<a id="item-4"></a>
## [Forgejo 16.0.4 Fixes Critical RCE in Template Repositories](https://codeberg.org/forgejo/forgejo/src/branch/forgejo/release-notes-published/16.0.4.md) ⭐️ 8.0/10

Forgejo released versions 16.0.4 and 15.0.8 to fix a critical remote code execution vulnerability (CVE-2026-89094) affecting all versions before 16.0.4. The flaw occurs when generating a new repository from a template repository, where mishandled variable template expansion on files listed in .forgejo/template can let an attacker execute arbitrary code with the privileges of the Forgejo service account. Forgejo is a widely used self-hosted Git platform, so this RCE can compromise the server and any repositories or credentials it hosts. Self-hosted instances that have not yet upgraded to 16.0.4 or 15.0.8 remain exposed to remote exploitation. The vulnerability is tracked as CVE-2026-89094 and rated critical; the fix prevents template expansion from interfering with git repository initialization. The release notes were initially hard to read due to Codeberg rate limits, and community members noted the fix removes .git after expansion, which some consider fragile compared to sandboxing the git step.

hackernews · weierstass · Sep 10, 15:57 · [Discussion](https://news.ycombinator.com/item?id=49645907)

**Background**: Forgejo is a community-run fork of Gitea, a lightweight self-hosted Git service. Template repositories let users create new repositories pre-populated with files, and Forgejo performs variable template expansion on files listed in the .forgejo/template directory during initialization. Because this expansion was not properly validated, a crafted template repository could inject malicious content into the Forgejo server process.

<details><summary>References</summary>
<ul>
<li><a href="https://lwn.net/Articles/1093671/">Forgejo 16.0.4 and 15.0.8 address critical security ...</a></li>
<li><a href="https://cve.halosecurity.com/cve-advisory/cve-2026-89094-forgejo-remote-code-execution-via-template-expansion">Forgejo Remote Code Execution via Template Expansion ...</a></li>
<li><a href="https://vuldb.com/cve/CVE-2026-89094">CVE-2026-89094 in Forgejo</a></li>

</ul>
</details>

**Discussion**: Commenters debated the robustness of the fix, with some arguing that sandboxing the git step would close the whole class of bugs rather than removing .git after expansion. A Gitea project leader noted that Gitea is protected against both issues, and others discussed how Forgejo's restrictions on LLM contributions may put it at a disadvantage as attackers increasingly use AI for vulnerability discovery.

**Tags**: `#security`, `#vulnerability`, `#forgejo`, `#git`, `#rce`

---

<a id="item-5"></a>
## [PlanetScale Launches Neki, a Sharded Postgres Solution](https://planetscale.com/blog/introducing-neki) ⭐️ 8.0/10

PlanetScale introduced Neki, a sharded Postgres offering that adds a router, sidecars, and a control plane on top of real Postgres shards to scale past a single machine to hundreds of millions of QPS and petabytes of data without downtime. The launch post drew 239 points and 131 comments on Hacker News, with much of the discussion criticizing the post for not clearly explaining what Neki actually is. Neki is a significant new sharded Postgres offering from a major database vendor, and it enters a market where horizontal scaling of Postgres is a common pain point for teams outgrowing single-node deployments. Its launch also reignites debate about open-source versus proprietary database tooling, especially given PlanetScale's history with the open-source Vitess project. According to PlanetScale, Neki will be released as an open source project once it is ready and tested in real production workloads, and the company frames it as making sharded Postgres accessible to everyone. The launch post's vague framing and claims such as unlimited IOPS on "PlanetScale Metal" drew skepticism from commenters.

hackernews · simon_weber · Sep 10, 15:43 · [Discussion](https://news.ycombinator.com/item?id=49645686)

**Background**: Sharding splits a database into smaller pieces called shards to scale horizontally, but it introduces complexity in query routing, transaction management, and data consistency. The CAP theorem states that a distributed data store can provide at most two of consistency, availability, and partition tolerance, which is why distributed databases often trade consistency for availability. PlanetScale previously built its business on Vitess, an open-source sharding system for MySQL originally created at Google.

<details><summary>References</summary>
<ul>
<li><a href="https://planetscale.com/neki">Neki — PlanetScale</a></li>
<li><a href="https://neki.dev/?ref=upstract.com">Neki | Sharded Postgres by PlanetScale</a></li>
<li><a href="https://en.wikipedia.org/wiki/CAP_theorem">CAP theorem - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters widely criticized the launch post for failing to explain what Neki is or what it is for, and some questioned marketing claims such as unlimited IOPS. Others raised concerns about eventual consistency and CAP theorem trade-offs for high-availability workloads, and several noted the irony that PlanetScale built its business on open-source Vitess while releasing Neki as proprietary, with one commenter calling out the CEO for criticizing Supabase's open-source multigres while Neki remains closed.

**Tags**: `#Postgres`, `#Database Sharding`, `#PlanetScale`, `#Distributed Systems`, `#CAP Theorem`

---

<a id="item-6"></a>
## [trynix.dev runs any Nix package in the browser via qemu-wasm](https://simonwillison.net/2026/Sep/10/trynix/) ⭐️ 8.0/10

Farid Zakaria launched trynix.dev, a project he calls his "magnum opus" of Nix work, which uses qemu-wasm to boot an x86_64 Linux virtual machine entirely inside the browser and load any Nix package from the past 13 years. Packages are URL-addressable, so visiting a link like trynix.dev/?pkg=python3%403.6.2 and clicking "Load" opens an interactive shell running Python 3.6.2 from 2017. This makes historical and reproducible software environments instantly accessible with nothing more than a browser, removing the need to install Nix, QEMU, or any local tooling. It could significantly lower the barrier for testing, teaching, debugging, and reviewing old or pinned package versions, and the accompanying trynix-preview GitHub Action extends the idea to reviewing pull requests by booting their builds. The system relies on ktock's qemu-wasm to run a full x86_64 Linux VM compiled to WebAssembly, and the trynix-preview GitHub Action simply comments a trynix.dev link on a pull request so reviewers can boot the PR's build with "no servers, just browsers." The main caveats are the performance and memory overhead of emulating a full VM in Wasm, plus the fact that only packages available in the Nix ecosystem over the past 13 years can be loaded.

rss · Simon Willison · Sep 10, 23:44

**Background**: Nix is a cross-platform package manager and build system, created in 2003 by Eelco Dolstra, that uses a purely functional language to describe reproducible builds and stores each result at a unique address. WebAssembly (Wasm) is a portable binary instruction format for a stack-based virtual machine that runs in browsers and can call into JavaScript. QEMU is a general-purpose machine emulator; ktock's qemu-wasm project compiles it to WebAssembly so a full operating system can run inside a browser tab.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/ktock/qemu-wasm">GitHub - ktock/ qemu - wasm : QEMU on browser · GitHub</a></li>
<li><a href="https://en.wikipedia.org/wiki/Nix_(package_manager)">Nix (package manager)</a></li>
<li><a href="https://en.wikipedia.org/wiki/WebAssembly">WebAssembly - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#Nix`, `#WebAssembly`, `#Virtualization`, `#Reproducibility`, `#Browser`

---

<a id="item-7"></a>
## [Four-Color Theorem Gets a Rare New Proof](https://www.quantamagazine.org/the-four-color-theorem-gets-a-rare-new-proof-20260910/) ⭐️ 8.0/10

Mathematicians have produced a rare new proof of the Four-Color Theorem, revisiting the famous problem that was controversially solved in 1976 with computer assistance, according to Quanta Magazine. The new work reportedly yields important fresh insights into the nature of graphs rather than merely re-verifying the known result. The Four-Color Theorem was the first major theorem proved with substantial computer assistance, and its 1976 proof sparked decades of debate about whether such proofs count as genuine mathematical understanding. A new proof that offers conceptual insight could reshape how mathematicians view computer-assisted results and strengthen the bridge between combinatorics, graph theory, and formal verification. The original Appel–Haken proof relied on an exhaustive case analysis of a large number of reducible configurations, later reduced to 633 configurations by Robertson, Sanders, Seymour, and Thomas in 1997, and fully verified in 2005 by Georges Gonthier using theorem-proving software. The new proof is notable because such alternative proofs of the theorem are extremely rare, though the article does not specify the exact technique or authors involved.

rss · Quanta Magazine · Sep 10, 14:27

**Background**: The Four-Color Theorem states that no more than four colors are needed to color any planar map so that regions sharing a border of non-zero length have different colors. It resisted proof for over a century after being posed in 1852, and was finally proved in 1976 by Kenneth Appel and Wolfgang Haken using a computer to check a huge number of cases. Because that proof was infeasible for a human to verify by hand, it became a landmark case in the debate over computer-assisted proofs, a category that includes proofs at least partially generated by computer, typically via lengthy proofs-by-exhaustion.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Four_color_theorem">Four color theorem</a></li>
<li><a href="https://en.wikipedia.org/wiki/Computer-assisted_proof">Computer-assisted proof</a></li>
<li><a href="https://en.wikipedia.org/wiki/Graph_theory">Graph theory</a></li>

</ul>
</details>

**Tags**: `#mathematics`, `#graph-theory`, `#four-color-theorem`, `#combinatorics`, `#computer-assisted-proof`

---

<a id="item-8"></a>
## [WebGL 'Deathray' lets untrusted sites freeze Macs](https://auberon.xyz/blog/posts/deathray/) ⭐️ 7.0/10

A blog post titled 'The Deathray' demonstrates that an untrusted website can use WebGL shaders to freeze a Mac, reportedly causing the macOS UI to become unresponsive and requiring a hard reboot. The author reports that Apple initially acknowledged the issue but later shifted its response, and no fix has been released. This highlights a browser-level denial-of-service vector that affects macOS users and raises questions about GPU process isolation and whether browsers should limit WebGL resource consumption. It matters because WebGL is widely used by legitimate sites like Figma, Canva, and Google Maps, so simply disabling it is not a practical mitigation for most users. The attack reportedly relies on WebGL shader execution to exhaust GPU or system resources, freezing the macOS UI rather than stealing data or compromising privacy. Community reports indicate similar hangs can occur on Windows in browsers like Brave, though the effect may be shorter and the offending tab may be frozen afterward.

hackernews · auberonedu · Sep 10, 19:34 · [Discussion](https://news.ycombinator.com/item?id=49649124)

**Background**: WebGL is a JavaScript API that lets websites render 2D and 3D graphics directly on the GPU, and it has shipped in browsers since around 2011. Browsers use process isolation, including separate GPU and rendering processes, to prevent malicious JavaScript from accessing the operating system, but resource exhaustion attacks can still affect the whole machine. Denial-of-service issues in WebGL have been documented before, including CVE-2023-5724 for Firefox.

<details><summary>References</summary>
<ul>
<li><a href="https://www.elseif.net/stories/the-deathray-a-simple-way-for-an-untrusted-site-to-freeze-a-mac-bf1e8fb">WebGPU shader reportedly freezes MacOS UI requiring... — elseif</a></li>
<li><a href="https://en.wikipedia.org/wiki/Site_isolation">Site isolation - Wikipedia</a></li>
<li><a href="https://vuldb.com/?id.243225">CVE-2023-5724 Mozilla Firefox WebGL denial of service ...</a></li>

</ul>
</details>

**Discussion**: Commenters were divided: some noted the issue has existed since WebGL shipped in 2011 and is 'self-correcting' because users simply avoid the offending site, while others reported that Brave on Windows froze for about 10 seconds. One commenter joked that their browser is configured to reopen the same tab on startup, which would make the freeze recur, and another shared a 1990s 'Don't Click Me' page that exploited browser bugs for similar effect.

**Tags**: `#WebGL`, `#browser security`, `#denial of service`, `#macOS`, `#web performance`

---

<a id="item-9"></a>
## [NASA's Decorrelation Stretch Reveals Ancient Rock Art](https://spinoff.nasa.gov/Manipulating_Satellite_Photos_Now_Reveals_Ancient_Images) ⭐️ 7.0/10

NASA's decorrelation stretch technique, originally developed for enhancing satellite imagery, is now being used to reveal ancient rock art and archaeological images. The technique, which heightens color contrasts in digital imagery, has gained renewed attention through a NASA Spinoff article and community discussion. This cross-disciplinary application shows how space technology can be repurposed for archaeology and cultural heritage preservation, helping researchers uncover faint or invisible images in ancient artifacts. It also highlights the broader value of signal processing and remote sensing techniques beyond their original domains. Decorrelation stretch operates on three color channels simultaneously to remove inter-channel correlation and enhance color differences, but the standard algorithm can suffer from numerical instability and struggles with degenerate cases where color planes are linearly dependent. The DStretch plugin, which implements this technique, has been available since around 2005.

hackernews · gumby · Sep 10, 15:29 · [Discussion](https://news.ycombinator.com/item?id=49645437)

**Background**: Decorrelation stretch is an image enhancement technique that transforms an image so its color planes become uncorrelated, making subtle color differences more visible. It is especially useful in remote sensing and multispectral imaging, where data beyond the visible spectrum can reveal hidden features. In archaeology, such techniques help detect faded rock art, buried structures, and other traces not visible to the naked eye.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nasa.gov/technology/tech-transfer-spinoffs/nasa-technique-for-manipulating-satellite-photos-now-reveals-ancient-images/">NASA Technique for Manipulating Satellite Photos Now Reveals ...</a></li>
<li><a href="https://www.mdpi.com/2227-7390/13/20/3297">Numerical Methods for Decorrelation Stretch - MDPI</a></li>
<li><a href="https://en.wikipedia.org/wiki/Remote_sensing_in_archaeology">Remote sensing in archaeology</a></li>

</ul>
</details>

**Discussion**: Commenters noted that false-color composites and similar techniques have been used in GIS and remote sensing for decades, with some expressing surprise that this is treated as news. Others shared practical tips, such as replicating the effect in GIMP, and discussed the broader principle of expanding limited color gamuts. A few pointed out that the DStretch plugin has existed since around 2005, so the technique itself is not new.

**Tags**: `#image-processing`, `#remote-sensing`, `#archaeology`, `#signal-processing`, `#NASA`

---

<a id="item-10"></a>
## [Cognition launches SWE-2 coding model, claiming frontier-level performance](https://cognition.com/blog/swe-2) ⭐️ 7.0/10

Cognition released SWE-2, a new software engineering model post-trained from Moonshot AI's Kimi K3, claiming frontier-level agentic coding at a fraction of the cost. The company says it scaled reinforcement learning to the multi-trillion-parameter regime for the first time, training all reasoning-effort levels in a single RL run. The release intensifies competition among coding-focused AI models, with Cognition positioning SWE-2 against established frontier models like Fable 5.1 and GPT-Astra. If the cost-performance claims hold, it could pressure closed-weight providers and accelerate adoption of cheaper agentic coding tools. SWE-2 scores 50.0% on FrontierCode 1.1 Main, within one point of Fable 5.1, and reportedly beats GPT-5.6 Sol at 64% lower cost. However, a large gap between its Terminal Bench 2.1 score (92.8%) and the newer Terminal Bench 4 score (27.3%) raises questions about generalization to new problems.

hackernews · seelos · Sep 10, 15:29 · [Discussion](https://news.ycombinator.com/item?id=49645443)

**Background**: Cognition is an AI company known for Devin, an autonomous coding agent, and for SWE-1.72, the training infrastructure that SWE-2 builds on. SWE-2 is post-trained from Kimi K3, Moonshot AI's 2.8-trillion-parameter model, using reinforcement learning. Terminal Bench is a benchmark that evaluates AI models on command-line tasks, and newer versions are designed to be less susceptible to overfitting.

<details><summary>References</summary>
<ul>
<li><a href="https://cognition.com/blog/swe-2">Introducing SWE-2: Pushing the Pareto Frontier | Cognition</a></li>
<li><a href="https://alphasignal.ai/news/cognition-s-swe-2-beats-gpt-5-6-sol-at-64-lower-cost">Cognition's SWE-2 Beats GPT-5.6 Sol at 64% Lower Cost | AlphaSignal</a></li>
<li><a href="https://ai-tldr.dev/releases/cognition-swe-2/">SWE-2 — Cognition's coding model lands within a… | AI/TLDR</a></li>

</ul>
</details>

**Discussion**: Hacker News commenters expressed substantial skepticism, citing the large gap between Terminal Bench 2.1 and 4 scores as evidence of benchmark overfitting, questioning Cognition's past demo credibility, and criticizing the lack of open weights. Some acknowledged that since SWE-2 is post-trained from the capable Kimi K3, it is likely competent, but urged caution about claimed improvements.

**Tags**: `#AI`, `#coding-models`, `#benchmarks`, `#model-release`, `#open-weights`

---

<a id="item-11"></a>
## [Open-source 'Proof of Capture' uses steganography to prove image authenticity](https://merybenavente.me/blog/proof-of-capture) ⭐️ 7.0/10

An open-source alternative to Apple's Reference Image, called Proof of Capture, has been introduced. It uses steganography to embed a perceptual hash (pHash) of an image into the image itself, providing a way to prove that a photo was captured by a specific device and has not been altered. This project offers a decentralized, open-source approach to image provenance, which could be crucial in the fight against AI-generated misinformation and deepfakes. It empowers users and developers to verify image authenticity without relying on proprietary systems like Apple's. The scheme signs a perceptual hash rather than an exact pixel checksum, which allows for minor alterations but raises cryptographic concerns. Community discussion highlights vulnerabilities such as preimage attacks on perceptual hashes and the potential for hardware spoofing.

hackernews · merybenavente · Sep 10, 19:44 · [Discussion](https://news.ycombinator.com/item?id=49649222)

**Background**: Apple's Reference Image is a feature on iPhone 18 Pro that stores an untouched original with verification metadata to prove a photo is not AI-generated. Perceptual hashing creates a fingerprint based on image content, allowing similar images to have similar hashes, unlike cryptographic hashes. Steganography hides information within other files, such as embedding data in image pixels.

<details><summary>References</summary>
<ul>
<li><a href="https://appleinsider.com/articles/26/09/09/apple-reference-image-is-a-new-way-to-authenticate-iphone-photography">Apple Reference Image is a new way to authenticate iPhone ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Perceptual_hashing">Perceptual hashing</a></li>
<li><a href="https://en.wikipedia.org/wiki/Steganography">Steganography - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters raised significant security concerns: perceptual hashes are non-cryptographic and vulnerable to preimage attacks, signing by default can have unintended consequences (e.g., linking leaked photos to the owner), and hardware spoofing could fake the entire capture process. Some also suggested future cameras should digitally sign images, with layered certification for edits.

**Tags**: `#steganography`, `#image-provenance`, `#cryptography`, `#perceptual-hashing`, `#security`

---

<a id="item-12"></a>
## [Datasette 1.0a39 and 0.65.4 Fix AI-Discovered Security Bugs](https://simonwillison.net/2026/Sep/11/datasette-security/) ⭐️ 7.0/10

Datasette released two security patch versions, 1.0a39 for the alpha series and 0.65.4 for the stable 0.65.x family, fixing subtle vulnerabilities found through an extensive audit conducted with Claude Fable 5.1, GPT-5.6, and GPT-6 Astra. The issues were initially reported by Sevban Dönmez, after which Simon Willison and Alex Garcia spent nearly a week collaborating on and reviewing the fixes. Anyone running a public Datasette instance that mixes public and private tables should upgrade immediately, since the flaws could expose private data. The release also signals a broader shift in open-source maintenance, with frontier AI models now being folded into routine security auditing workflows. The vulnerabilities are described as very subtle and specifically affect instances that serve both public and private tables in the same deployment. The audit workflow split work so that one person wrote automated tests exposing each issue while the other implemented the fix, ensuring two humans plus multiple coding agents reviewed every problem.

rss · Simon Willison · Sep 11, 03:27

**Background**: Datasette is an open-source tool that turns SQLite databases into interactive, searchable websites with a built-in JSON API, and it is widely used by data journalists, researchers, and government teams. Its permission system lets operators mark some tables as public and others as private, a configuration that has previously been targeted by SQL injection flaws, including one patched in version 0.65.3. AI-assisted security audits pair the traversal speed of large language models with human judgment to find bugs that traditional static analysis might miss.

<details><summary>References</summary>
<ul>
<li><a href="https://datasette.io/">Datasette: An open source multi-tool for exploring and ...</a></li>
<li><a href="https://github.com/simonw/datasette">GitHub - simonw/datasette: An open source multi-tool for ... Datasette download | SourceForge.net Datasette documentation The Datasette Ecosystem - Datasette documentation Datasette - lossless.group Datasette Tools</a></li>
<li><a href="https://releaseport.com/r/simonw-datasette/0-65-3">Datasette 0.65.3 release notes — security patches & CVE fixes</a></li>

</ul>
</details>

**Tags**: `#datasette`, `#security`, `#open-source`, `#ai-assisted-audit`, `#release`

---

<a id="item-13"></a>
## [ACL Proposes Sustainable Reviewing Policy with Submission Caps](https://www.reddit.com/r/MachineLearning/comments/1wd7b83/acl_sustainable_reviewing_policy_d/) ⭐️ 7.0/10

ACL announced a new "Sustainable Reviewing Policy" for its ARR (ACL Rolling Review) system, capping total submissions at 20 per author and first-author submissions at 5 per cycle, while requiring each submission to provide a qualified reviewer or chair to avoid a lottery for remaining capacity. This policy directly addresses the unsustainable growth in NLP/ML conference submissions, potentially reshaping how research is published and reviewed, and could influence other conferences facing similar reviewer shortages. Submissions without a qualified service contributor go into a lottery for spare capacity, non-author contributors can be nominated but must vouch for the work (arXiv-endorsement style), and measures against system abuse include penalties or bans for accounts that systematically submit or endorse low-quality work.

reddit · r/MachineLearning · /u/S4M22 · Sep 11, 05:38

**Background**: ACL Rolling Review (ARR) is a centralized peer review platform for ACL conferences, where authors submit papers in two-month cycles and receive reviews and metareviews. The Association for Computational Linguistics (ACL) is a major professional organization for NLP researchers, and its conferences are among the top venues in the field. In recent years, submission numbers have surged, straining the volunteer reviewer pool.

<details><summary>References</summary>
<ul>
<li><a href="https://aclrollingreview.org/">ACL Rolling Review – A peer review platform for the ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Association_for_Computational_Linguistics">Association for Computational Linguistics - Wikipedia</a></li>

</ul>
</details>

**Discussion**: The Reddit discussion generally supports the policy, with the original poster calling it "highly required" despite being a form of gatekeeping, and noting that the caps of 20 and 5 are still generous. Some concerns about fairness and gatekeeping were raised, but overall sentiment leaned positive.

**Tags**: `#ACL`, `#peer-review`, `#conference-policy`, `#NLP`, `#academic-publishing`

---

<a id="item-14"></a>
## [Free Open Music Theory Textbook Sparks Debate on Classical Focus](https://musictheory.pugetsound.edu/mt21c/MusicTheory.html) ⭐️ 6.0/10

A free online music theory textbook hosted by the University of Puget Sound, titled "Music Theory for the 21st-Century Classroom," was shared on Hacker News and drew 218 points and 89 comments. The site includes SVG illustrations, homework assignments, and resources designed for self-study. This resource highlights the growing open textbook movement, which aims to reduce the cost and access barriers of traditional textbooks. Its popularity also reflects ongoing debates about what a modern music theory curriculum should include, particularly regarding non-classical and non-Western traditions. The textbook is released under an open license, allowing free use and adaptation, and features interactive SVG illustrations. However, critics note it remains heavily classical-centric, with minimal coverage of jazz, pop, rock, and non-Western music theories.

hackernews · aanet · Sep 10, 17:14 · [Discussion](https://news.ycombinator.com/item?id=49647134)

**Background**: Open textbooks are textbooks licensed under an open copyright license, made available online for free use by students, teachers, and the public. They are part of the broader open educational resources movement, which seeks to address affordability and access issues in education. Music theory pedagogy, the teaching of music theory, has traditionally focused on Western classical music, but there is growing pressure to include diverse musical traditions.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Open_textbook">Open textbook</a></li>
<li><a href="https://serenademagazine.com/music-theory-pedagogy-how-its-taught-and-why-it-matters/">Music Theory Pedagogy : How It’s Taught and Why It Matters</a></li>

</ul>
</details>

**Discussion**: Commenters praised the textbook's quality, with one calling the SVG illustrations "delicious" and another noting the site's usefulness for self-study. However, several criticized its classical focus and lack of context, with one asking what makes it "21st-century" and another pointing out the omission of jazz, world music, and modern styles.

**Tags**: `#music-theory`, `#education`, `#open-textbook`, `#self-study`, `#classical-music`

---
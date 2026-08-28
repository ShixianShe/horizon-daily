---
layout: default
title: "Horizon Summary: 2026-08-28 (EN)"
date: 2026-08-28
lang: en
---

> From 31 items, 20 important content pieces were selected

---

1. [US Judge Rules Pentagon's Blacklisting of Anthropic Unlawful](#item-1) ⭐️ 8.0/10
2. [Cloudflare Saves 100TB by Optimizing 1.1.1.1 DNS Cache](#item-2) ⭐️ 8.0/10
3. [EPA Exempts Islanded Data Center Power from Clean Air Act](#item-3) ⭐️ 8.0/10
4. [Small Models Have Arrived: The Rise of Compact AI](#item-4) ⭐️ 8.0/10
5. [Prompt Injection Attack Bypasses Claude Code Auto Mode 80% of the Time](#item-5) ⭐️ 8.0/10
6. [Moderna's Cancer Vaccine Shows Promise, Personalized Therapies Need Acceleration](#item-6) ⭐️ 8.0/10
7. [HarnessOpt-Bench: Benchmarking AI's Ability to Improve Other Agents](#item-7) ⭐️ 8.0/10
8. [Websites Pushing Apps: A Trust-Abusing Anti-Pattern](#item-8) ⭐️ 7.0/10
9. [OpenAI Python SDK Migrates to HTTPX2 for Stability](#item-9) ⭐️ 7.0/10
10. [Fast Polyhedron Volume via Divergence Theorem](#item-10) ⭐️ 7.0/10
11. [Luanti Removed from Google Play Over Baseless AI Copyright Claim](#item-11) ⭐️ 7.0/10
12. [Heisuke Hironaka Obituary: Mathematician Who Smoothed Geometry's Complexities](#item-12) ⭐️ 7.0/10
13. [Does Computer Science Need Computers?](#item-13) ⭐️ 7.0/10
14. [Statistical ML Researchers Question Top Conference Direction](#item-14) ⭐️ 7.0/10
15. [py-evoFE: Genetic Algorithm Feature Engineering for Tabular ML](#item-15) ⭐️ 7.0/10
16. [Orbify's Inception-style curved map demo for navigation](#item-16) ⭐️ 6.0/10
17. [HK AGI First Stock Surges: Agent Revenue Nears 500M Yuan, Token Income Jumps 500% in Q2](#item-17) ⭐️ 6.0/10
18. [Meta's Child Safety Measures Face Researcher Skepticism](#item-18) ⭐️ 6.0/10
19. [What Employers Seek in the AI Era: Four Ways to Stand Out](#item-19) ⭐️ 6.0/10
20. [Seeking Well-Written ML Papers to Improve Academic Writing](#item-20) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [US Judge Rules Pentagon's Blacklisting of Anthropic Unlawful](https://www.reuters.com/legal/government/us-judge-blocks-pentagons-anthropic-blacklisting-2026-08-28/) ⭐️ 8.0/10

A US judge ruled that the Pentagon's blacklisting of AI company Anthropic was unlawful, potentially leading to compensation and setting a precedent for government actions against tech firms. This ruling is significant as it challenges government discretion in contracting and could impact how the DoD and other agencies treat tech companies. It may also lead to financial compensation for Anthropic and influence future legal battles between the government and AI firms. The judge found that the evidence presented by the government was 'entirely nonsense,' indicating a lack of substantive justification for the blacklisting. The ruling could result in a 'big payday' for Anthropic, covering lost revenue and users during the ban period.

hackernews · softwaredoug · Aug 28, 11:25 · [Discussion](https://news.ycombinator.com/item?id=49477055)

**Background**: The Pentagon had blacklisted Anthropic, likely due to perceived value misalignment with the Department of Defense. This case highlights the tension between government contracting discretion and the rights of tech companies, especially in the rapidly evolving AI sector.

**Discussion**: Community comments express mixed reactions. Some criticize the administration's actions, while others question whether the DoD should have discretion in contracting decisions. There is also speculation about potential financial compensation for Anthropic and links to a previous discussion thread.

**Tags**: `#AI`, `#legal`, `#government`, `#Anthropic`, `#policy`

---

<a id="item-2"></a>
## [Cloudflare Saves 100TB by Optimizing 1.1.1.1 DNS Cache](https://blog.cloudflare.com/dns-cache-memory-optimization-1111/) ⭐️ 8.0/10

Cloudflare engineers detailed five Rust-level memory optimizations to the DNS cache layout of their 1.1.1.1 resolver, reducing per-entry memory by 56% and freeing approximately 100 terabytes of memory across their global fleet. This optimization demonstrates significant cost savings and performance improvements for one of the world's largest DNS services, highlighting the ongoing importance of systems-level programming in large-scale infrastructure. It also provides a practical case study for engineers working on memory-constrained systems. The optimizations included reducing the size of cache entries by reordering struct fields, using more compact data types, and avoiding separate allocations for record data. The changes were implemented in Rust, and the blog post provides specific technical details on how each optimization was achieved.

hackernews · TangerineDream · Aug 27, 17:17 · [Discussion](https://news.ycombinator.com/item?id=49468083)

**Background**: DNS (Domain Name System) is the internet's phonebook, translating human-readable domain names into IP addresses. Caching DNS responses is crucial for performance, but storing millions of entries consumes significant memory. Cloudflare's 1.1.1.1 is a popular public DNS resolver, and optimizing its cache can lead to substantial infrastructure savings.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.cloudflare.com/dns-cache-memory-optimization-1111/">How we saved 100 terabytes of memory by optimizing 1.1.1.1’s ...</a></li>
<li><a href="https://news.ycombinator.com/item?id=49468083">Saving 100 terabytes of memory by optimizing 1 . 1 . 1 . 1 's DNS cache</a></li>
<li><a href="https://www.tomshardware.com/tech-industry/big-tech/cloudflare-frees-100tb-of-ram-by-shrinking-dns-cache-entries">Cloudflare frees up 100TB of RAM by shrinking 1 . 1 . 1 . 1 's DNS cache ...</a></li>

</ul>
</details>

**Discussion**: The Hacker News discussion reflects a mix of appreciation and technical critique. Some commenters praised the practical approach of optimizing after stabilizing the product, while others pointed out potential further optimizations, such as embedding record data directly into cache entries. A few raised concerns about whether combining separate lists into one might undermine Rust's safety guarantees.

**Tags**: `#DNS`, `#memory optimization`, `#systems programming`, `#performance`, `#Cloudflare`

---

<a id="item-3"></a>
## [EPA Exempts Islanded Data Center Power from Clean Air Act](https://www.epa.gov/newsreleases/epa-issues-permitting-guidance-further-president-trumps-agenda-promoting-data-centers) ⭐️ 8.0/10

The EPA issued guidance clarifying that islanded power generation facilities, which are not connected to the public grid, are exempt from Clean Air Act Acid Rain Program provisions, specifically targeting data centers. This guidance, released in July 2026, follows President Trump's agenda to promote data center development. This policy change could significantly reduce environmental oversight for data center power generation, potentially leading to increased air pollution in surrounding communities. It sets a precedent that may encourage more data centers to use islanded generation to bypass environmental regulations, affecting public health and climate goals. The guidance specifically exempts islanded power generation from the Acid Rain Program, which regulates sulfur dioxide and nitrogen oxides emissions. An example cited involves a 500 MW natural gas-fired facility powering a data center. Critics argue that the exemption is illogical because environmental impact is independent of grid connection.

hackernews · Levitating · Aug 28, 13:21 · [Discussion](https://news.ycombinator.com/item?id=49478103)

**Background**: Islanded power generation refers to facilities that operate independently from the public electricity grid, often used for remote or dedicated power needs. The Clean Air Act's Acid Rain Program was established to reduce emissions that cause acid rain, and it typically applies to power plants. This guidance creates a loophole for data centers, which have growing energy demands, to avoid certain pollution controls.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Islanding">Islanding - Wikipedia</a></li>
<li><a href="https://www.epa.gov/system/files/documents/2026-07/epa-issues-clarification-on-islanded-power-generators-and-acid-rain-program-provisions.pdf">PDF EPA issues clarification on Islanded Power Generators and Acid Rain ...</a></li>
<li><a href="https://grist.org/regulation/these-data-center-developers-asked-trump-for-an-exemption-from-pollution-rules/">Data center developers asked Trump for relief from pollution rules</a></li>

</ul>
</details>

**Discussion**: Community comments express strong disapproval, with users calling the exemption nonsensical and a disgrace, and arguing that grid connection does not affect environmental impact. Some see it as a two-tiered rule that undermines the EPA's credibility, while others note the benefits of grid connection that are being lost.

**Tags**: `#EPA`, `#data centers`, `#environmental regulation`, `#energy policy`, `#Clean Air Act`

---

<a id="item-4"></a>
## [Small Models Have Arrived: The Rise of Compact AI](https://calv.info/small-models-have-arrived) ⭐️ 8.0/10

The article highlights that small language models (SLMs) have become increasingly capable, meeting the growing demand for fast, cheap, and 'good-enough' AI solutions. This shift opens new opportunities for consumer products and local deployment. This trend signifies a major shift in AI, moving beyond the frontier model race to practical, accessible AI that can run on consumer hardware. It empowers developers and businesses to build innovative consumer AI applications without relying on expensive cloud APIs. Small models typically have fewer than 40 billion parameters, making them feasible to run on personal computers and smart devices. The article notes that open-weight models are often 3–6 months behind frontier models, but they offer advantages in cost, latency, and privacy.

hackernews · tosh · Aug 27, 15:56 · [Discussion](https://news.ycombinator.com/item?id=49466917)

**Background**: Small language models (SLMs) are AI models designed for natural language processing with fewer parameters than large language models (LLMs). They can be hosted locally on consumer electronics, offering benefits like better privacy, reduced internet dependency, and faster response times. The growing capability of SLMs is enabling new use cases in edge AI and on-device AI.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Small_language_model">Small language model - Wikipedia</a></li>
<li><a href="https://www.ibm.com/think/topics/small-language-models">What are Small Language Models (SLM)? | IBM</a></li>
<li><a href="https://machinelearningmastery.com/introduction-to-small-language-models-the-complete-guide-for-2026/">Introduction to Small Language Models: The Complete Guide for 2026</a></li>

</ul>
</details>

**Discussion**: Commenters discuss practical applications of small models, such as using a 7B local model with the Guidance library to generate tests and code. There is interest in resources for choosing local models based on RAM, and a sentiment that consumer AI companies are underrepresented, with a call for building products that people actually need.

**Tags**: `#AI`, `#small models`, `#local models`, `#consumer AI`, `#machine learning`

---

<a id="item-5"></a>
## [Prompt Injection Attack Bypasses Claude Code Auto Mode 80% of the Time](https://simonwillison.net/2026/Aug/27/breaking-claude-code-opus-5-auto-mode/) ⭐️ 8.0/10

Security researcher Johann Rehberger demonstrated a prompt injection attack that bypasses Claude Code's auto mode 80% of the time by exploiting Python's import behavior with a malicious zip archive. The attack tricks Claude Code into downloading and extracting a zip file, then executing code that imports a local struct.py file instead of the standard library. This attack undermines Anthropic's confidence in auto mode as a safety mechanism for coding agents, highlighting that even sophisticated classifiers can be bypassed. It underscores the need for sandboxing and least-privilege principles when running AI agents, as the safety mechanism itself can block cleanup commands, turning it into part of the failure. The attack exploits Python's import system: when a zip archive contains a file named struct.py, importing base64 triggers the local struct.py to be executed instead of the standard library. In some runs, auto mode blocked Claude's attempt to terminate the malicious process, demonstrating that the classifier can prevent cleanup actions.

rss · Simon Willison · Aug 27, 22:50

**Background**: Prompt injection is a cybersecurity exploit where malicious inputs are crafted to cause unintended behavior in large language models (LLMs). Claude Code's auto mode uses a classifier to make permission decisions, aiming to balance fewer interruptions with safety. However, this attack shows that even with such safeguards, agents can be tricked into executing harmful code, emphasizing the importance of running agents in sandboxed environments with restricted network access and no sensitive credentials.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Prompt_injection_attack">Prompt injection attack</a></li>
<li><a href="https://claude.com/blog/auto-mode">Auto mode for Claude Code | Claude by Anthropic</a></li>
<li><a href="https://code.claude.com/docs/en/auto-mode-config">Configure auto mode - Claude Code Docs</a></li>

</ul>
</details>

**Tags**: `#AI security`, `#prompt injection`, `#Claude Code`, `#LLM agents`, `#cybersecurity`

---

<a id="item-6"></a>
## [Moderna's Cancer Vaccine Shows Promise, Personalized Therapies Need Acceleration](https://www.nature.com/articles/d41586-026-02680-5) ⭐️ 8.0/10

A positive trial of Moderna's personalized cancer vaccine, developed with Merck, showed it helps prevent the return and spread of melanoma in a large trial involving more than 1,000 patients. The results were published in Nature and highlight the need to accelerate personalized therapies. This is a significant step forward in cancer treatment, as personalized vaccines could offer a more targeted and less toxic alternative to traditional chemotherapy. The success could spur further investment and research into mRNA-based personalized medicine, potentially benefiting many cancer patients. The vaccine uses artificial-intelligence tools to identify neoantigens most likely to trigger a strong immune response, and is paired with Merck's Keytruda to enhance effectiveness. However, some patients with advanced cancers might not survive long enough to benefit, and more research is needed to bring effective vaccines to the clinic.

rss · Nature · Aug 28, 00:00

**Background**: Personalized cancer vaccines work by analyzing a patient's tumor to identify unique mutations (neoantigens) and then training the immune system to target those markers. Unlike conventional vaccines, each dose is custom-made for an individual based on their cancer's genetic profile. This approach aims to specifically attack cancer cells while sparing healthy ones, potentially reducing side effects compared to chemotherapy.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nature.com/articles/d41586-026-02612-3">Moderna cancer vaccine stops melanoma returning: what’s next for personalized treatments? | Nature</a></li>
<li><a href="https://www.cnn.com/2026/08/21/health/mrna-cancer-vaccines-wave">Moderna, Merck breakthrough could usher in wave of cancer vaccines | CNN</a></li>
<li><a href="https://www.cnbc.com/2026/08/19/moderna-merck-cancer-vaccine-shows-initial-late-stage-melanoma-data.html">Cancer vaccine from Moderna, Merck shows promise in late-stage trial; both stocks soar</a></li>

</ul>
</details>

**Tags**: `#cancer vaccine`, `#Moderna`, `#personalized medicine`, `#biotech`, `#clinical trial`

---

<a id="item-7"></a>
## [HarnessOpt-Bench: Benchmarking AI's Ability to Improve Other Agents](https://www.reddit.com/r/MachineLearning/comments/1w052xg/can_ai_improve_itself_rsi_might_be_the_answer_r/) ⭐️ 8.0/10

Researchers introduced HarnessOpt-Bench, a benchmark that scores how well an LLM can improve another agent's coding harness while preventing cheating through sandbox isolation. The benchmark was tested on 5 frontier models across 4 tasks, revealing that model choice affects gains 1.8 times more than harness choice. This benchmark addresses a critical safety concern in recursive self-improvement (RSI) by providing a controlled environment to measure AI's ability to improve other agents without cheating. It offers a concrete experimental setup that could guide future research and safety measures in AI development. The benchmark uses sandbox isolation by construction, keeping API keys, budget enforcement, and held-out data outside the optimizer's sandbox. Results show that opencode beats native harnesses in 11 of 20 model-task pairs, and Claude Opus 5 under OpenCode tops 3 of 4 tasks.

reddit · r/MachineLearning · /u/shehio · Aug 27, 20:13

**Background**: Recursive self-improvement (RSI) is a hypothesized process where AI systems rewrite their own code to enhance capabilities, potentially leading to superintelligence. Sandboxing is a key safety technique that isolates AI execution to prevent unintended actions, and this benchmark applies it to measure RSI safely.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2608.06301">[2608.06301] HarnessOpt-Bench: Evaluating LLMs at Harness ...</a></li>
<li><a href="https://labs.scale.com/papers/harnessopt-bench">HarnessOpt-Bench: Evaluating LLMs at Harness Optimization</a></li>
<li><a href="https://en.wikipedia.org/wiki/Recursive_self-improvement">Recursive self-improvement</a></li>

</ul>
</details>

**Discussion**: The Reddit discussion likely includes technical debate on the benchmark's design, the significance of the results, and concerns about RSI safety. Some may question the generalizability of the findings or the effectiveness of sandbox isolation in real-world scenarios.

**Tags**: `#AI safety`, `#recursive self-improvement`, `#benchmark`, `#LLM`, `#agent`

---

<a id="item-8"></a>
## [Websites Pushing Apps: A Trust-Abusing Anti-Pattern](https://shkspr.mobi/blog/2026/08/it-works-better-in-the-app/) ⭐️ 7.0/10

A blog post criticizes the growing trend of websites pushing users to install apps for features that work in browsers, arguing it's often a trust-abusing tactic. The post and its comments highlight specific frustrations and examples of this anti-pattern. This issue affects user trust and experience across the web, as more companies use app install prompts to collect data or lock features. It highlights a broader industry trend toward walled gardens and dark patterns, which can erode user confidence and lead to decreased engagement. The post argues that pushing apps is often unnecessary and can be a sign of abusive intent, such as tracking or data collection. Commenters share personal experiences, including Amazon's ID verification requiring a device camera, and note that high barriers to app installation lead users to abandon sites entirely.

hackernews · blenderob · Aug 28, 12:32 · [Discussion](https://news.ycombinator.com/item?id=49477600)

**Background**: Anti-patterns in web design are common practices that harm user experience, while dark patterns are manipulative design choices that trick users. The trend of pushing native apps over web apps has been criticized for creating walled gardens and reducing web openness, with some attributing it to Apple's marketing in the 2010s.

<details><summary>References</summary>
<ul>
<li><a href="https://www.uxdesigninstitute.com/blog/what-are-dark-patterns-in-ux/">What are dark patterns in UX? All you need to know</a></li>
<li><a href="https://thedecisionlab.com/reference-guide/design/dark-patterns">Dark Patterns - The Decision Lab</a></li>
<li><a href="https://indieweb.org/antipatterns">antipatterns - IndieWeb</a></li>

</ul>
</details>

**Discussion**: Commenters express strong distrust of app-pushing practices, with one noting that forcing an app install is a sign of abusive intent. Others share specific frustrations, such as Amazon's ID verification requiring a device camera, and some defend Google's role, blaming Apple for championing native apps.

**Tags**: `#web design`, `#user experience`, `#privacy`, `#apps`, `#anti-patterns`

---

<a id="item-9"></a>
## [OpenAI Python SDK Migrates to HTTPX2 for Stability](https://github.com/openai/openai-python/blob/main/httpx2.md) ⭐️ 7.0/10

OpenAI's Python SDK has migrated to HTTPX2, a stable fork of the httpx library, to avoid breaking changes expected in the upcoming httpx 1.0 release. This change is documented in the repository's httpx2.md file. This migration is significant because OpenAI's SDK is widely used, and the move to a stable dependency ensures long-term reliability for developers. It also reflects a broader industry trend, as Anthropic has made a similar change, highlighting concerns about httpx's stability. HTTPX2 is a fork of httpx that promises not to break the existing API, providing a more stable foundation. The migration was prompted by httpx's path toward a 1.0 release, which is expected to include breaking changes, and both OpenAI and Anthropic have pinned httpx < 1.0 in their dependencies.

hackernews · tosh · Aug 28, 11:51 · [Discussion](https://news.ycombinator.com/item?id=49477212)

**Background**: httpx is a popular Python HTTP client library, but its development has included breaking changes in minor releases, causing churn for downstream projects. HTTPX2, now stewarded by Pydantic Services, aims to provide a stable API for production use. This move by OpenAI and Anthropic underscores the need for dependable dependencies in large-scale SDKs.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/pydantic/httpx2">GitHub - pydantic/httpx2: A next generation HTTP client for Python. 🦋</a></li>
<li><a href="https://httpxyz.org/why-fork/">Why we forked HTTPX - HTTPXYZ</a></li>
<li><a href="https://pypi.org/project/httpx2/">httpx2 · PyPI</a></li>

</ul>
</details>

**Discussion**: Community comments show mixed reactions: simonw notes that Anthropic made the same change and explains the rationale, while delduca questions why this is on the front page. jklehm wonders if alternatives like niquests were evaluated, and ZeroCool2u suggests investing in the requests library instead. londons_explore asks about the upsides of the change.

**Tags**: `#OpenAI`, `#HTTPX2`, `#Python SDK`, `#dependency management`, `#API`

---

<a id="item-10"></a>
## [Fast Polyhedron Volume via Divergence Theorem](https://alyssarosenzweig.ca/blog/hilariously-fast-volume-computation-with-the-divergence-theorem.html) ⭐️ 7.0/10

A blog post by Alyssa Rosenzweig demonstrates a surprisingly fast method for computing polyhedron volumes using the divergence theorem, which simplifies the calculation to summing contributions from each triangular face. The post highlights the technique's efficiency and simplicity, sparking community discussion about historical implementations and alternative formulas. This technique is valuable for graphics and geometry processing, where fast volume computations are often needed. The discussion reveals that similar methods have existed for decades, but the post makes the approach accessible and highlights its practical relevance. The method applies the divergence theorem to integrate the function x over the polyhedron's volume, reducing it to a surface integral over triangular faces. The formula is equivalent to summing signed volumes of pyramids from the origin, and it works for both convex and concave polyhedra, provided the mesh is closed and simple.

hackernews · luu · Aug 28, 09:00 · [Discussion](https://news.ycombinator.com/item?id=49476143)

**Background**: The divergence theorem, also known as Gauss's theorem, relates the flux of a vector field through a closed surface to the divergence of the field inside the volume. In computational geometry, it is often used to compute properties like volume and centroid by converting volume integrals to surface integrals. The blog post leverages this theorem to derive a simple and fast formula for polyhedron volume, which is a common operation in graphics and simulation.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Divergence_theorem">Divergence theorem - Wikipedia</a></li>
<li><a href="https://mathworld.wolfram.com/PolyhedronVolume.html">Polyhedron Volume -- from Wolfram MathWorld</a></li>
<li><a href="https://news.ycombinator.com/item?id=49476143">Hilariously Fast Volume Computation with the Divergence Theorem | Hacker News</a></li>

</ul>
</details>

**Discussion**: Commenters noted that the method is essentially summing signed pyramid volumes, and some pointed out historical implementations like Algorithm 550 from 1980. Others mentioned related theorems like Pick's theorem for lattice polygons, and emphasized the importance of the mesh being closed and simple. Overall, the discussion was positive, with some expressing surprise at the simplicity and others noting it was a known trick.

**Tags**: `#divergence theorem`, `#volume computation`, `#computational geometry`, `#graphics`, `#polyhedron`

---

<a id="item-11"></a>
## [Luanti Removed from Google Play Over Baseless AI Copyright Claim](https://blog.luanti.org/2026/08/27/luanti-dmca-tracer-ai/) ⭐️ 7.0/10

Luanti, an open-source voxel game engine, was removed from Google Play on August 27, 2026, following a DMCA takedown notice from Tracer AI, a company that allegedly uses AI to scan for copyright infringement. The notice was later revealed to be baseless, and Luanti's developers are appealing the removal. This incident highlights the growing problem of AI-generated DMCA takedowns that can harm open-source projects without proper oversight. It underscores the need for accountability and penalties for frivolous copyright claims, as such actions can disrupt the ecosystem and erode trust in legal processes. Tracer AI claimed jurisdiction in Vanuatu in the DMCA notice, despite previously claiming US jurisdiction in other cases, raising questions about potential fraud. The company had also filed a similar notice in 2023 against Luanti, which was successfully appealed, and against an indie game called Allumeria this year.

hackernews · miniBill · Aug 28, 06:33 · [Discussion](https://news.ycombinator.com/item?id=49475079)

**Background**: Luanti, formerly known as Minetest, is a free and open-source voxel game engine that allows users to create and play various games. DMCA takedown notices are legal requests to remove content allegedly infringing copyright, but they can be abused. AI-powered tools are increasingly used to generate such notices, sometimes leading to false claims that harm legitimate projects.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Luanti">Luanti - Wikipedia</a></li>
<li><a href="https://www.luanti.org/en/">Luanti | Open source voxel game engine - Luanti</a></li>
<li><a href="https://patentpc.com/blog/dmca-takedown-notices-against-ai-algorithms-real-life-case-studies">DMCA Takedown Notices Against AI Algorithms Real-Life Case Studies | PatentPC</a></li>

</ul>
</details>

**Discussion**: Community members expressed frustration over the lack of penalties for frivolous DMCA notices and questioned the legality of Tracer AI's jurisdiction claims. Some suggested that the sequence of events might involve AI scraping open-source code and then flagging similar code in proprietary games, highlighting the irony of AI-generated claims.

**Tags**: `#DMCA`, `#open-source`, `#legal`, `#AI`, `#gaming`

---

<a id="item-12"></a>
## [Heisuke Hironaka Obituary: Mathematician Who Smoothed Geometry's Complexities](https://www.nature.com/articles/d41586-026-02688-x) ⭐️ 7.0/10

Nature published an obituary for mathematician Heisuke Hironaka on August 28, 2026, celebrating his landmark proof of resolution of singularities, which transformed algebraic geometry. Hironaka's 1964 proof resolved a long-standing problem in algebraic geometry, providing a foundational tool that enables mathematicians to study singular varieties by transforming them into smooth ones. His work has had a lasting impact on the field and continues to influence modern research. The proof applies to varieties over fields of characteristic zero, but the problem remains open for positive characteristic in dimensions four and above. The obituary highlights his 'awe-inspiring' proof, which addressed singularities such as peaks, edges, and self-crossings.

rss · Nature · Aug 28, 00:00

**Background**: In algebraic geometry, a singularity is a point where a geometric object is not smooth, such as a self-intersection or a cusp. Resolution of singularities asks whether every algebraic variety can be transformed into a smooth one via a proper birational map. Hironaka proved this for characteristic zero in 1964, a result now known as Hironaka's theorem. For positive characteristic, the problem remains open in higher dimensions.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Resolution_of_singularities">Resolution of singularities - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Hironaka_theorem">Hironaka theorem</a></li>

</ul>
</details>

**Tags**: `#mathematics`, `#algebraic geometry`, `#obituary`, `#Hironaka`

---

<a id="item-13"></a>
## [Does Computer Science Need Computers?](https://www.quantamagazine.org/does-computer-science-need-computers-20260828/) ⭐️ 7.0/10

Quanta Magazine published an article exploring whether theoretical computer science can exist independently of physical computing machines, and how the existence of computers has shaped the field's questions. This philosophical inquiry challenges the foundational assumptions of computer science, prompting researchers and students to reflect on the discipline's identity and its relationship with hardware. It could influence how computer science is taught and perceived, especially in theoretical areas. The article is from Quanta Magazine, a reputable publication known for in-depth science and math coverage. It focuses on the theoretical side of computer science, suggesting that while many questions would not have been posed without computers, the field's core logic may not depend on physical machines.

rss · Quanta Magazine · Aug 28, 13:30

**Background**: Theoretical computer science (TCS) is a branch that studies abstract computation, algorithms, and complexity, often without direct reference to physical hardware. The article addresses a long-standing debate about whether TCS is a pure mathematical discipline or inherently tied to the existence of computers. This discussion is relevant to the broader philosophy of science and the history of computing.

**Tags**: `#computer science`, `#theory`, `#philosophy`, `#Quanta Magazine`

---

<a id="item-14"></a>
## [Statistical ML Researchers Question Top Conference Direction](https://www.reddit.com/r/MachineLearning/comments/1w0kipf/where_to_submit_statprob_ml_d/) ⭐️ 7.0/10

A researcher in statistical and probabilistic ML posted on Reddit questioning where to submit their work, as top conferences like ICLR and NeurIPS are increasingly dominated by LLM and agentic research. They are considering alternatives such as AISTATS and UAI. This reflects a growing concern within the ML community about the narrowing scope of top conferences, which could impact the visibility and funding of statistical/probabilistic ML research. It may encourage more researchers to submit to specialized venues, potentially reshaping the academic landscape. The researcher notes that at ICLR, only about one in ten posters was not about LLMs, and NeurIPS workshops are mostly about agents. They admire researchers like Arnaud Doucet and Aapo Hyvärinen who still publish at top venues, but are leaning toward AISTATS/UAI for their own work.

reddit · r/MachineLearning · /u/didimoney · Aug 28, 08:16

**Background**: AISTATS (Artificial Intelligence and Statistics) and UAI (Uncertainty in Artificial Intelligence) are established conferences focused on the intersection of statistics, machine learning, and AI, often serving as primary venues for statistical and probabilistic ML research. In recent years, top-tier conferences like NeurIPS and ICLR have seen a surge in LLM-related submissions, driven by the popularity of large language models and agentic AI, which may crowd out other research areas.

<details><summary>References</summary>
<ul>
<li><a href="https://virtual.aistats.org/Conferences/2026">2026 Conference - virtual.aistats.org</a></li>
<li><a href="https://openreview.net/group?id=aistats.org/AISTATS/2026/Conference">AISTATS 2026 Conference | OpenReview</a></li>
<li><a href="https://openreview.net/group?id=auai.org/UAI/2026/Conference">UAI 2026 Conference | OpenReview</a></li>

</ul>
</details>

**Tags**: `#ML conferences`, `#statistical ML`, `#probabilistic ML`, `#research community`, `#LLM dominance`

---

<a id="item-15"></a>
## [py-evoFE: Genetic Algorithm Feature Engineering for Tabular ML](https://www.reddit.com/r/MachineLearning/comments/1w0788j/pyevofe_automated_evolutionary_feature/) ⭐️ 7.0/10

py-evoFE v0.3.0, an open-source Python library, has been released, using genetic algorithms to automatically discover and optimize feature transformations for tabular datasets. It integrates with scikit-learn and Polars, offering 40+ built-in transformers and an interactive replay viewer. This library addresses a critical bottleneck in tabular machine learning by automating feature engineering, which often determines success in competitions and production models. Its evolutionary approach offers a compact, parsimonious alternative to brute-force feature generation, potentially improving model generalization and reducing manual effort. The library implements hierarchical chaining, where evolved features become building blocks for future generations, and uses multi-fidelity screening to speed up evaluation. It also features an island model with parallel search and Caruana ensembling, and is 100% scikit-learn compatible, fitting into standard pipelines and GridSearchCV.

reddit · r/MachineLearning · /u/tanopereira · Aug 27, 21:33

**Background**: Genetic programming is an evolutionary algorithm that evolves programs to solve problems, mimicking natural selection. In feature engineering, it evolves feature construction programs to create new features from raw data. py-evoFE applies this to tabular data, using Polars for vectorized computation and caching to improve efficiency.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Genetic_programming">Genetic programming - Wikipedia</a></li>
<li><a href="https://pypi.org/project/py-evofe/">py - evofe · PyPI</a></li>
<li><a href="https://tanopereira.r-universe.dev/evoFE/doc/evoFE.html">Getting Started with evoFE</a></li>

</ul>
</details>

**Tags**: `#feature engineering`, `#genetic algorithms`, `#tabular ML`, `#Python`, `#open-source`

---

<a id="item-16"></a>
## [Orbify's Inception-style curved map demo for navigation](https://www.orbify.eu/demo/) ⭐️ 6.0/10

Orbify released an interactive web demo of an Inception-style curved map for turn-by-turn directions, powered by PlayCanvas. The demo showcases a patent-pending technique that warps a 3D map model onto a curved surface, allowing drivers to see far-distance road conditions. This novel UI concept could redefine car navigation by providing a more intuitive view of the road ahead, potentially improving driver awareness and safety. However, usability concerns about turn visualization and potential nausea may limit its practical adoption. The demo is patent-pending and seeks pilots, collaborations, and investment. Community feedback highlights that sharp turns force road sections off-screen without view rotation, reducing the usefulness of the prediction, and some suggest a shallower gradient for better usability.

hackernews · smoser · Aug 28, 12:29 · [Discussion](https://news.ycombinator.com/item?id=49477564)

**Background**: Traditional turn-by-turn navigation typically shows a top-down or slightly angled map that only displays a limited area around the vehicle. The Inception-style curved map, inspired by the movie's bending cityscapes, aims to show far-distance road conditions by warping the map onto a curved surface. Prior art includes Berg's 'Here and There' poster from 2009, which explored similar visual concepts.

<details><summary>References</summary>
<ul>
<li><a href="https://zeli.app/story/49477564">Orbify's Inception-style curved map for turn-by-turn ...</a></li>
<li><a href="https://news.ycombinator.com/item?id=49477564">Inception-style curved map for turn-by-turn directions ...</a></li>
<li><a href="https://bubbles.town/entry/44771680">Bending Maps, Inception Style — Bubbles</a></li>

</ul>
</details>

**Discussion**: Community comments are generally positive about the novelty but critical of usability. One commenter found it amusing but unsuitable for real-world use, while another noted that sharp turns cause road sections to go off-screen, making prediction less useful. A reference to Berg's 2009 poster suggests the idea is not entirely new, and a joke about 'Nausea as a Service' highlights the motion sickness concern.

**Tags**: `#maps`, `#UI/UX`, `#navigation`, `#demo`, `#HCI`

---

<a id="item-17"></a>
## [HK AGI First Stock Surges: Agent Revenue Nears 500M Yuan, Token Income Jumps 500% in Q2](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&mid=2247916163&idx=1&sn=c5ff2c32d3b62c544a5061f43c287a20) ⭐️ 6.0/10

A Hong Kong-listed AGI company reported strong financial results, with Agent business revenue approaching 500 million yuan in half a year and token revenue surging 500% in Q2. The company's stock price surged following the announcement. This milestone highlights the commercial viability of AI Agent and token-based business models, signaling a shift from pure model development to monetizable enterprise AI services. It could influence investor sentiment and industry trends in the AI sector, especially for companies listed in Hong Kong. The company's Agent business generated nearly 500 million yuan in revenue over six months, while token revenue grew 500% in Q2. The report also mentions that AI is driving complete machine verification of finite group classification, and the CEO remains in the spotlight but the steering wheel has changed hands.

rss · 量子位 · Aug 28, 09:15

**Background**: AI Agent refers to intelligent agents that can perceive, plan, and act autonomously to complete tasks, often integrating with enterprise systems. Token revenue is generated from usage-based billing of AI services, where each token (a unit of text or code) consumed by users is charged. This model is becoming a key revenue stream for AI companies.

<details><summary>References</summary>
<ul>
<li><a href="https://www.huaweicloud.com/zhishi/ag1.html">Agent是什么_Agent是什么意思-华为云</a></li>
<li><a href="https://www.jingdigital.com/articles/21276/">AI Agent是什么?一文看懂AI agent概念、分类、原理、应用场景、趋势</a></li>
<li><a href="https://www.authing.cn/blog/1140">AI Agent 到底是什么？一文带你快速了解 AI Agent - Authing身份云</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/2020222371412320866">Token 是什么？它能代替工资和股权激励？ - 知乎</a></li>

</ul>
</details>

**Tags**: `#AGI`, `#financial results`, `#Agent`, `#token revenue`, `#Hong Kong stock`

---

<a id="item-18"></a>
## [Meta's Child Safety Measures Face Researcher Skepticism](https://www.nature.com/articles/d41586-026-02733-9) ⭐️ 6.0/10

Nature reports that Meta is introducing new safety measures for Facebook and Instagram aimed at protecting children, but researchers are doubtful about their effectiveness. The article, published on 28 August 2026, highlights the gap between policy announcements and evidence-based outcomes. This matters because social media platforms face increasing pressure to safeguard minors, and Meta's decisions could set industry standards. If the measures are ineffective, children remain at risk, and public trust in platform governance may further erode. The article features interviews with specialists who question whether the changes are backed by solid evidence. Specific details of the measures are not disclosed in the summary, but the skepticism centers on the lack of proven efficacy and potential unintended consequences.

rss · Nature · Aug 28, 00:00

**Background**: Social media platforms have been under scrutiny for their impact on children's mental health and safety, leading to calls for stricter regulations. Meta, the parent company of Facebook and Instagram, has previously introduced parental controls and content moderation, but critics argue these are insufficient. Researchers emphasize the need for independent studies to evaluate the real-world effectiveness of such safety features.

**Tags**: `#social media`, `#child safety`, `#Meta`, `#policy`, `#research`

---

<a id="item-19"></a>
## [What Employers Seek in the AI Era: Four Ways to Stand Out](https://www.nature.com/articles/d41586-026-01913-x) ⭐️ 6.0/10

Nature published an article on 28 August 2026 offering advice for job seekers in the age of AI, based on interviews with academics, employers, and early-career researchers. The article highlights that applicants whose AI knowledge is limited to basic ChatGPT familiarity need to expand their understanding, and it outlines four practical ways to do so. As AI becomes integral to many workplaces, job seekers—especially early-career researchers—must demonstrate more than superficial familiarity with tools like ChatGPT. This article provides timely, expert-backed guidance that can help applicants differentiate themselves in a competitive job market. The article is based on conversations with academics, employers, and early-career researchers, and it identifies four specific ways for applicants to deepen their AI understanding beyond basic ChatGPT usage. The advice is tailored to early-career researchers and job seekers, emphasizing practical skills and broader knowledge.

rss · Nature · Aug 28, 00:00

**Background**: The rapid adoption of generative AI tools like ChatGPT has transformed many industries, creating new demands for employees who can leverage these technologies effectively. However, many job seekers still have only a basic understanding of AI, which may not be sufficient to meet employer expectations. This article aims to bridge that gap by offering actionable advice from experts.

**Tags**: `#AI`, `#career advice`, `#employment`, `#research`, `#education`

---

<a id="item-20"></a>
## [Seeking Well-Written ML Papers to Improve Academic Writing](https://www.reddit.com/r/MachineLearning/comments/1w075pe/best_ml_papers_to_pick_up_writing_skills_d/) ⭐️ 6.0/10

A Reddit user in r/MachineLearning asked for recommendations of well-written ML papers to help PhD students and early researchers improve their writing skills, inviting suggestions for exemplary authors and papers. This discussion highlights the importance of clear scientific communication in ML research, where complex ideas often need to be conveyed effectively. The recommendations could serve as valuable learning resources for researchers aiming to enhance their paper-writing abilities. The user defines a 'well-written paper' as one that clearly explains the problem, method development, and details while remaining accessible to readers with basic ML knowledge. They note that post-2015 papers often have better figures but are specifically seeking text-based writing quality.

reddit · r/MachineLearning · /u/fakeaccountlegitme · Aug 27, 21:30

**Background**: Academic writing is a critical skill for researchers, yet it is rarely taught formally. Many PhD students learn by reading exemplary papers and imitating their structure and clarity. This request reflects a common need within the ML community for guidance on effective scientific communication.

**Tags**: `#machine learning`, `#academic writing`, `#research papers`, `#PhD advice`

---
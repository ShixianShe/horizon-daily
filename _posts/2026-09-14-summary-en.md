---
layout: default
title: "Horizon Summary: 2026-09-14 (EN)"
date: 2026-09-14
lang: en
---

> From 21 items, 14 important content pieces were selected

---

1. [Fable 5.1 Solves the 370-Year-Old Cyphral Distich Cipher](#item-1) ⭐️ 8.0/10
2. [Signal to Enable Phone-Free Registration Using Zero-Knowledge Proofs](#item-2) ⭐️ 8.0/10
3. [Mullenweg Returns as Automattic CEO After Failed Board Ouster](#item-3) ⭐️ 8.0/10
4. [Google's Persistent Scam Ads Spark Accountability Debate](#item-4) ⭐️ 8.0/10
5. [Apple Publishes Dimensional Drawings for Nearly 90 Accessories](#item-5) ⭐️ 7.0/10
6. [Blog post argues against JPEG XL for web, sparking debate with AVIF](#item-6) ⭐️ 7.0/10
7. [Hacker News September 2026: Developers Share Their Side Projects](#item-7) ⭐️ 7.0/10
8. [Zachary Lipton Says CS Academia Is Broken as arXiv cs.LG Hits 447 Papers in a Day](#item-8) ⭐️ 7.0/10
9. [Horse racing as an ML ranking problem with 1.18M runners](#item-9) ⭐️ 7.0/10
10. [whitetree: Dynamic Exact Mahalanobis kNN via Multiple scipy cKDTrees](#item-10) ⭐️ 7.0/10
11. [825k-Parameter Model Generates Drawing Bytecode That Runs Exactly on RP2040](#item-11) ⭐️ 7.0/10
12. [Open-Source AI Reading List Sparks Debate on Open Weights vs Open Source](#item-12) ⭐️ 6.0/10
13. [Simon Willison releases commit-rewriter 0.1 for cleaning up commit messages](#item-13) ⭐️ 6.0/10
14. [Waymo AI Team to Host AMA on r/MachineLearning](#item-14) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Fable 5.1 Solves the 370-Year-Old Cyphral Distich Cipher](https://www.vals.ai/blogs/fable-solves-cyphral-distich) ⭐️ 8.0/10

Anthropic's Claude Fable 5.1, a large language model released on September 1, 2026, autonomously selected and solved the Cyphral Distich, a cipher created by Scottish writer Sir Thomas Urquhart that had remained unbroken for over 370 years. The model was given an open-ended task rather than the specific cipher, and it chose the problem itself before producing a solution that the researchers describe as embarrassing for humans in hindsight. This marks a notable milestone in applying LLMs to historical cryptography, showing that AI can autonomously identify and tackle unsolved research problems rather than only executing well-specified tasks. It also fuels the broader debate about whether such results reflect genuine reasoning capability or simply the fact that many long-standing puzzles were never seriously examined by enough human researchers. Fable 5.1 ranks first overall on Vals AI's RSI-Index at 35.03%, ahead of the previous leader Claude Opus 5 at 32.10%, while costing $1,481 — about 21% less than Opus 5's $1,886. The decrypted text reads 'O GOD UPHOLD KING CHARLS THE SECOND AND MAKE HIM THE SUPREME RULER OF THIS LAND,' a fairly mundane message relative to the puzzle's difficulty.

hackernews · u1hcw9nx · Sep 13, 21:06 · [Discussion](https://news.ycombinator.com/item?id=49688695)

**Background**: The Cyphral Distich is a cryptogram attributed to Sir Thomas Urquhart, a 17th-century Scottish writer and translator, and it resisted decoding for roughly 370 years. Traditional attacks such as frequency analysis, simple substitution, and homophonic substitution all failed against it. Large language models like Claude Fable 5.1 are AI systems trained on vast text corpora, and recent versions have been marketed for coding, scientific research, and complex knowledge work, including tasks that require multi-step reasoning over obscure historical material.

<details><summary>References</summary>
<ul>
<li><a href="https://www.vals.ai/blogs/fable-solves-cyphral-distich">Claude Fable 5.1 Solves the Cyphral Distich</a></li>
<li><a href="https://forklog.com/en/anthropics-claude-fable-5-1-deciphers-17th-century-cryptogram/">Anthropic’s Claude Fable 5.1 Deciphers 17th-Century... | ForkLog</a></li>
<li><a href="https://www.vals.ai/models/anthropic_claude-fable-5-1">Vals AI: Claude Fable 5.1</a></li>

</ul>
</details>

**Discussion**: Hacker News commenters were impressed that the model chose the problem itself, but several questioned the novelty of the solution: one user pointed to a 2014 German blog post whose comments already proposed it was a book cipher, and another noted there is little evidence the cipher was well-known or heavily studied. A recurring theme was that many recent LLM 'breakthroughs' may reflect abundant low-hanging fruit and limited prior human attention rather than a fundamental leap in capability.

**Tags**: `#cryptography`, `#LLM`, `#AI`, `#history`, `#Hacker News`

---

<a id="item-2"></a>
## [Signal to Enable Phone-Free Registration Using Zero-Knowledge Proofs](https://community.signalusers.org/t/registration-without-a-phone-number/2222?page=10) ⭐️ 8.0/10

Signal is implementing zero-knowledge proofs to allow users to register without a phone number, a major privacy enhancement for the secure messaging platform. According to community discussion, the feature may require a Google Play Billing purchase to mitigate spam while keeping SMS verification as an option. This change removes a long-standing barrier that forced users to tie their identity to a phone number, which is often linked to real-world identity and can be a privacy risk. It could benefit activists, journalists, and anyone in regions where phone numbers are expensive or easily surveilled, and it signals a broader trend of secure messaging apps moving toward phone-number-free authentication. The implementation uses zero-knowledge proofs, which allow a user to prove they meet a requirement (such as not being a spammer) without revealing the underlying information. Community members note that the feature may only support new accounts for now, and that it may require a purchase via Google Play Billing to prevent spam, while SMS verification remains available.

hackernews · Cider9986 · Sep 13, 21:47 · [Discussion](https://news.ycombinator.com/item?id=49689048)

**Background**: Zero-knowledge proofs are a cryptographic method that lets one party prove to another that a statement is true without revealing any information beyond the truth of the statement itself. Signal is a widely used end-to-end encrypted messaging app that has historically required a phone number for registration and verification, though the number is hidden by default and users can connect via usernames. This move follows years of requests from privacy advocates who want to use Signal without linking to a phone number.

<details><summary>References</summary>
<ul>
<li><a href="https://aboutsignal.com/news/signal-is-working-on-registration-without-a-phone-number/">Signal is working on registration without a phone number. But what form will it take?</a></li>
<li><a href="https://www.expressvpn.com/blog/zero-knowledge-proofs-explained/">What Is a zero - knowledge proof and why it matters | ExpressVPN</a></li>
<li><a href="https://aboutsignal.com/signal-knowledge-base/can-i-use-signal-without-a-phone-number/">Can I use Signal without a phone number?</a></li>

</ul>
</details>

**Discussion**: Community sentiment is mixed: some users welcome the ability to use Signal on Android tablets without a SIM as first-class devices, while others criticize the lack of transparency about backend infrastructure and demand that Signal release its infrastructure automation code. There is also skepticism about the sufficiency of the information provided, with one commenter noting that simply saying 'zero knowledge' is not enough to guarantee privacy, and another asking whether phone-free registration is actually available yet.

**Tags**: `#Signal`, `#privacy`, `#zero-knowledge proofs`, `#secure messaging`, `#authentication`

---

<a id="item-3"></a>
## [Mullenweg Returns as Automattic CEO After Failed Board Ouster](https://techcrunch.com/2026/09/12/automattic-confirms-mullenweg-has-returned-as-ceo-after-attempted-ouster-by-board/) ⭐️ 8.0/10

Matt Mullenweg has returned as CEO of Automattic, the parent company of WordPress.com, after an attempted board ouster failed. According to TechCrunch, Mullenweg removed other admins from the company Slack and told employees he was back in control, though the company has not issued a clear public board statement documenting his formal reinstatement. This governance crisis raises serious questions about WordPress governance and organizational control, given that Automattic and WordPress power a huge portion of the web. The outcome could affect how much influence a single individual holds over a major open-source ecosystem and may push some users and companies toward alternative CMS platforms. The board's plan reportedly did not go smoothly: Mullenweg booted other admins out of the company Slack and told employees everything had been worked out. TechCrunch notes that no one at Automattic is giving a straight answer, and when asked whether his comments about being back as CEO were trolling, Mullenweg replied, "I'm not a troll I'm a pirate, obviously."

hackernews · ilamont · Sep 13, 20:19 · [Discussion](https://news.ycombinator.com/item?id=49688259)

**Background**: Automattic is the company behind WordPress.com and contributes heavily to the open-source WordPress project, which powers a large share of websites worldwide. Matt Mullenweg is the founder of WordPress and has long been the central figure in both Automattic and the broader WordPress community. Board ousters typically involve institutional investors seeking to change leadership over disputes about strategy or management.

<details><summary>References</summary>
<ul>
<li><a href="https://techcrunch.com/2026/09/12/automattic-confirms-mullenweg-has-returned-as-ceo-after-attempted-ouster-by-board/">Automattic confirms Mullenweg has returned as CEO after ...</a></li>
<li><a href="https://runtimewire.com/article/matt-mullenweg-returns-automattic-ceo-board-ouster">Automattic says Matt Mullenweg is CEO again after board ...</a></li>
<li><a href="https://www.gurualpha.com/article/matt-mullenweg-retakes-control-of-automattic-following-failed-board-revolt">Matt Mullenweg Retakes Control of Automattic Following Failed ...</a></li>

</ul>
</details>

**Discussion**: Commenters expressed frustration that few people read the full article, which describes a truly mind-boggling situation where no one at Automattic gives a straight answer. Some long-time WordPress users argued the ecosystem is the worst of both worlds — distributed and slow-moving yet ultimately controlled by a single individual — and warned this pushes people toward Shopify and other CMSes, though a grand exodus is unlikely. An Automattic employee of five years also shared insider perspective, while others suggested Mullenweg may have lost his grip on reality.

**Tags**: `#WordPress`, `#Automattic`, `#corporate governance`, `#open source`, `#leadership`

---

<a id="item-4"></a>
## [Google's Persistent Scam Ads Spark Accountability Debate](https://www.atomic14.com/2026/09/13/why-is-google-still-serving-dodgy-ads) ⭐️ 8.0/10

A critical blog post on atomic14.com titled "Why is Google still serving dodgy ads?" triggered a large Hacker News discussion with 812 points and 357 comments, in which users shared firsthand accounts of scam ads appearing through Google AdSense and YouTube. Commenters described pop-up scams demanding fake fines, AI-generated product ads, and domains that Google refuses to block because it treats them as top-level domains. The discussion highlights a systemic trust problem in Google's ad ecosystem: if scam ads can appear on legitimate publishers' sites and on YouTube, they undermine user trust, harm publishers, and raise questions about whether Google's enforcement incentives are aligned with user safety. The debate also connects to broader concerns about Google's revenue pressure amid AI competition and the potential disruption of its ad business. Commenters noted that scammers rotate through free hosting subdomains such as azurestaticapps.net, herokuapp.com, netlify.app, and digitaloceanspaces.com, and that Google reportedly will not block these because it classifies them as TLDs. One commenter claimed someone who spent over $100M on Google Ads said Google is juicing revenue in unprecedented ways, while another argued for strict liability because Google is complicit.

hackernews · iamflimflam1 · Sep 13, 17:37 · [Discussion](https://news.ycombinator.com/item?id=49686445)

**Background**: Google Ads is Google's primary advertising platform, and AdSense lets publishers display ads on their websites in exchange for revenue. Google says it uses AI and human reviewers to enforce advertising policies and remove violating ads, and in recent years it has deployed large language models and a new AI fraud-detection model to catch bad advertisers. Despite these systems, critics argue that scam ads persist because enforcement is reactive and revenue incentives favor allowing more ads through.

<details><summary>References</summary>
<ul>
<li><a href="https://www.searchenginejournal.com/google-alf-advertiser-large-foundation-model/564510/">Google Ads Using New AI Model To Catch Fraudulent Advertisers</a></li>
<li><a href="https://support.google.com/adspolicy/answer/6008942?hl=en">Google Ads policies - Advertising Policies Help</a></li>
<li><a href="https://blog.octobrowser.net/google-ads-anti-fraud-algorithms">Google Ads Anti-Fraud Algorithms in 2025: Overview and How to ...</a></li>

</ul>
</details>

**Discussion**: The Hacker News discussion was overwhelmingly critical of Google, with users sharing personal experiences of scam ads on their sites and on YouTube, blaming revenue incentives and weak enforcement. Several commenters called for strict liability, while others speculated that Google is maximizing ad revenue before AI disrupts its business, and some suggested the volume of ads simply exceeds review capacity.

**Tags**: `#Google Ads`, `#advertising`, `#scams`, `#platform accountability`, `#Hacker News discussion`

---

<a id="item-5"></a>
## [Apple Publishes Dimensional Drawings for Nearly 90 Accessories](https://developer.apple.com/accessories/dimensional-drawings/) ⭐️ 7.0/10

Apple has expanded its developer-facing dimensional drawings page to cover nearly 90 accessories, up from just 13 products when the page was first archived around May 2026. The page provides precise geometric blueprints and technical specifications for mechanical engineers, industrial designers, and accessory manufacturers. This resource gives third-party accessory makers verified specifications directly from Apple, reducing guesswork and costly errors in designing cases, mounts, and other add-ons. It strengthens Apple's accessory ecosystem by making it easier for manufacturers to build products that fit Apple devices precisely. The drawings include highly detailed specifications, such as those for the Apple Watch Ultra 3, though they only capture part of the picture — tolerances and surface roughness are not fully specified. Some community members noted that rounded edges on devices like the MacBook are defined as small distance specs rather than radii.

hackernews · herbertl · Sep 14, 00:11 · [Discussion](https://news.ycombinator.com/item?id=49690174)

**Background**: Dimensional drawings are technical documents that show the exact physical dimensions and geometry of a product, used by engineers and manufacturers to design compatible parts. Apple's Accessories program provides developers with specifications, hardware components, and certification tools for building licensed accessories. Previously, such detailed drawings were not publicly available in one place, making it harder for third parties to achieve precise fits.

<details><summary>References</summary>
<ul>
<li><a href="https://developer.apple.com/accessories/dimensional-drawings/">Download Dimensional Drawings - Accessories - Apple Developer</a></li>
<li><a href="https://developer.apple.com/accessories/">Accessories - Apple Developer</a></li>
<li><a href="https://braindetox.kr/en/posts/apple_dimensional_drawings_accessory.html">Apple Dimensional Drawings for Accessory Makers - 130 ...</a></li>

</ul>
</details>

**Discussion**: Commenters highlighted the impressive level of detail, especially for the Apple Watch Ultra 3, and wondered about acceptable rejection rates and how Apple handles surface roughness. Others noted the page's growth from 13 to nearly 90 products since May 2026, questioned why rounded edges are specified as distances rather than radii, and pointed out the irony that Apple uses Siemens NX on Windows VMs for its own CAD work.

**Tags**: `#Apple`, `#hardware`, `#accessories`, `#CAD`, `#manufacturing`

---

<a id="item-6"></a>
## [Blog post argues against JPEG XL for web, sparking debate with AVIF](https://giannirosato.com/blog/post/case-against-jxl/) ⭐️ 7.0/10

A blog post titled 'The case against JPEG XL' argues that JPEG XL is not well-suited for typical web use cases, favoring AVIF instead. The post sparked a Hacker News discussion with 213 comments debating the trade-offs between the two image formats. The debate highlights the ongoing competition between image formats for web adoption, which affects web developers, browser vendors, and content creators. The outcome could influence which format becomes the standard for efficient image delivery on the web. JPEG XL is a royalty-free format supporting lossy and lossless compression, high dynamic range, and wide color gamut, while AVIF is based on the AV1 video codec and also royalty-free. A key technical concern raised is that AVIF's hardware decoding may be limited to 4:2:0 chroma subsampling due to its AV1 Main Profile constraints, which is suboptimal for illustrations and screenshots.

hackernews · contact9879 · Sep 14, 01:02 · [Discussion](https://news.ycombinator.com/item?id=49690554)

**Background**: JPEG XL is an image format developed by the Joint Photographic Experts Group, Google, and Cloudinary, standardized as ISO/IEC 18181, designed for web delivery and professional photography. AVIF is a format derived from the AV1 video codec, released in 2019, and is also royalty-free, supporting HDR and modern imaging techniques. Both formats aim to improve compression efficiency over older formats like JPEG and WebP, but they differ in features and hardware support.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/JPEG_XL">JPEG XL - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/AVIF">AVIF - Wikipedia</a></li>
<li><a href="https://jpeg.org/jpegxl/">JPEG - JPEG XL</a></li>

</ul>
</details>

**Discussion**: Commenters debated the trade-offs: some noted AVIF's hardware decoding may be limited to 4:2:0 chroma subsampling, which is poor for illustrations and screenshots, while others argued that JPEG XL's versatility is valuable for archival and non-web uses. A recurring point was that 'the world should be different' is not a valid argument against optimizing for real-world constraints, and some expressed a preference for not having to choose between formats for different use cases.

**Tags**: `#JPEG XL`, `#AVIF`, `#image compression`, `#web standards`, `#codecs`

---

<a id="item-7"></a>
## [Hacker News September 2026: Developers Share Their Side Projects](https://news.ycombinator.com/item?id=49686380) ⭐️ 7.0/10

The monthly "Ask HN: What are you working on?" thread for September 2026 drew 166 upvotes and 525 comments, with developers showcasing projects ranging from a UK flight-deal service for parents (schoolholidays.deals) to a voxel game engine called Bonsai that has been in development for roughly 10 years. These recurring threads offer a snapshot of what independent developers and small teams are actually building, revealing current trends such as AI-assisted coding and AI-judged applications, and giving early-stage projects visibility and feedback from a technically sophisticated audience. Notable entries include Bonsai, a voxel engine whose world is represented as collections of signed distance fields (SDFs) and which recently underwent a large multi-year rewrite, and moral.games, a debate PvP game where players argue an ethical conundrum before an AI judge, though it requires two players to queue simultaneously.

hackernews · david927 · Sep 13, 17:31

**Background**: Hacker News is a technology-focused discussion site run by Y Combinator, and its recurring "Ask HN: What are you working on?" threads are a long-standing tradition where users post links and descriptions of their current projects. A voxel engine is a game engine that renders worlds as 3D grids of small cubes, while signed distance fields are a mathematical way of representing shapes that is popular for procedural and editable geometry.

<details><summary>References</summary>
<ul>
<li><a href="https://lab.rosebud.ai/blog/best-voxel-game-engines-2026">Best Voxel Game Engines in 2026 — Rosebud vs Hytopia vs Godot ...</a></li>
<li><a href="https://www.airhint.com/">AirHint Flight Price Predictor - when to book cheap flight tickets</a></li>

</ul>
</details>

**Discussion**: Commenters shared a wide range of projects with candid notes on their progress: ahallan said AI writes about 90% of the code for his flight-deal service while he fits development around work, yashness promoted Introkeep for QR-based networking at conferences, and dvt noted his moral.games Show HN got little traffic and requires a friend to queue at the same time.

**Tags**: `#hacker-news`, `#community`, `#projects`, `#showcase`, `#discussion`

---

<a id="item-8"></a>
## [Zachary Lipton Says CS Academia Is Broken as arXiv cs.LG Hits 447 Papers in a Day](https://www.reddit.com/r/MachineLearning/comments/1wf4b5g/zachery_lipton_cs_academia_broke_the/) ⭐️ 7.0/10

A Reddit post on r/MachineLearning highlights that arXiv's cs.LG category reached an all-time daily high of 447 new machine learning papers on September 9, 2026, up from a baseline of roughly 200 papers per day. The post quotes Zachary Lipton, a Carnegie Mellon machine learning professor, saying that CS academia "broke the system" and that perhaps the only way to rebuild it is for it "to burn to the ground." The sheer volume of submissions far exceeds what any individual researcher or reading group can digest, raising concerns about peer review quality, research incentives, and the sustainability of the current publication model. This debate matters to anyone in the ML community, from graduate students facing publish-or-perish pressure to conference organizers struggling to scale review processes. The 447-paper spike is roughly double the ~200 papers per day that cs.LG normally receives, and even a large reading group could not feasibly read and digest that many papers in a year. The Reddit discussion frames this as a possible "point of no return" for the current academic system, echoing Lipton's provocative call for a fundamental rebuild.

reddit · r/MachineLearning · /u/NeighborhoodFatCat · Sep 13, 10:42

**Background**: arXiv is a free preprint server where researchers upload papers before or instead of formal peer review, and cs.LG is its machine learning category. Zachary Lipton is an assistant professor at Carnegie Mellon University who directs the Approximately Correct Machine Intelligence Lab and has frequently criticized hype and methodological problems in machine learning research. The rapid growth of AI research since the deep learning boom has flooded venues like arXiv and major conferences with submissions, straining review capacity.

<details><summary>References</summary>
<ul>
<li><a href="https://thegradientpub.substack.com/p/zachary-lipton-where-machine-learning">Zachary Lipton: Where Machine Learning Falls Short</a></li>
<li><a href="https://www.orfonline.org/expert-speak/your-ai-versus-my-ai-zachary-lipton-on-the-dangers-of-the-ai-and-machine-learning-hype-cycle-44976">Your AI versus my AI: Zachary Lipton on the dangers of the AI and machine learning hype cycle</a></li>

</ul>
</details>

**Discussion**: The Reddit thread likely contains diverse viewpoints on whether the system is truly broken and whether burning it down is a viable solution, with debates over peer review reform, publication incentives, and the role of arXiv in enabling the flood. Some commenters may agree with Lipton's diagnosis while disagreeing with his rhetoric, and others may propose alternative fixes such as stricter submission caps or new review models.

**Tags**: `#machine learning`, `#academia`, `#research culture`, `#peer review`, `#arxiv`

---

<a id="item-9"></a>
## [Horse racing as an ML ranking problem with 1.18M runners](https://www.reddit.com/r/MachineLearning/comments/1wfivb2/horse_racing_as_an_ml_ranking_problem_118m/) ⭐️ 7.0/10

A personal ML project called Hoofs models British and Irish horse racing as a ranking problem using roughly 1.18 million historical runner records and about 1,700 features per runner. After rebuilding its data pipeline and feature bank, it reports a model-only win AUC of about 0.729 versus a market-only baseline of about 0.790 on a 2018–2025 benchmark of roughly 886,000 runners and 94,000 races. It illustrates how hard it is to beat an efficient betting market with ML, since the market baseline substantially outperforms the model on discrimination. The project is also a useful case study for practitioners dealing with variable-sized fields, non-stationarity, and strict chronological validation in applied ranking problems. The models estimate win and place probabilities at runner level and then rank runners within each race, with a separate race-level confidence model using field size, probability concentration, entropy, and separation between leading runners. Evaluation is strictly walk-forward, training each fold only on earlier seasons with out-of-fold calibration and explicit checks to prevent future information leaking into historical features.

reddit · r/MachineLearning · /u/gcampb41 · Sep 13, 20:32

**Background**: Walk-forward validation is a time-series evaluation technique that repeatedly trains on past data and tests on later data, extending standard out-of-sample testing to respect chronological order. The project was inspired by Bill Benter, who famously used statistical models to beat Hong Kong racing markets, and it treats the betting market's implied probabilities as a strong baseline that any model must outperform to be useful.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Walk_forward_optimization">Walk forward optimization - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Bill_Benter">Bill Benter - Wikipedia</a></li>
<li><a href="https://crunchingthedata.com/baseline-models-for-machine-learning/">Baseline models for machine learning - Crunching the Data</a></li>

</ul>
</details>

**Tags**: `#machine-learning`, `#ranking`, `#sports-analytics`, `#time-series-validation`, `#applied-ml`

---

<a id="item-10"></a>
## [whitetree: Dynamic Exact Mahalanobis kNN via Multiple scipy cKDTrees](https://www.reddit.com/r/MachineLearning/comments/1wfg8e3/got_scipys_kdtree_to_handle_inserts_and_deletes/) ⭐️ 7.0/10

A new library called whitetree enables exact Mahalanobis nearest-neighbor search with dynamic inserts and deletes by whitening data with the Cholesky factor of the covariance and maintaining multiple scipy cKDTrees instead of one. It reports 40–300x speedups over sklearn's BallTree(mahalanobis) and 7–60x over FAISS Flat at 500k points, while matching a static cKDTree exactly (distance error 0.0) after arbitrary insert/delete mixes. Dynamic exact nearest-neighbor search on streaming low-dimensional sensor data is a common but underserved need; whitetree offers a pure numpy/scipy solution that avoids full rebuilds and outperforms FAISS IDMap2 by roughly 55x in interleaved insert/delete/query workloads. It also provides a rare, plainly stated comparison of FAISS's native whitening accuracy versus its search, which could inform practitioners choosing between exact and approximate methods. The approach uses a geometric size ratio of 32, keeping 3–4 trees at a million points and retaining 47–97% throughput for batches and 20–80% for single queries; deletes are handled via tombstones. A key caveat is that dynamic indexing only helps when updates and queries interleave frequently—on a 200k-point sliding window with batch updates, rebuilding a cKDTree per batch (2.2 s) beats whitetree (14.9 s), and FAISS's native whitening loses recall at high condition numbers (0.841 at 1e8) and produces NaN with a large DC offset.

reddit · r/MachineLearning · /u/monononon34 · Sep 13, 18:54

**Background**: Mahalanobis distance measures how many standard deviations a point is from a distribution, accounting for correlations; whitening with the Cholesky factor of the covariance transforms it into standard Euclidean distance. KD-trees are static spatial indexes that become inefficient under frequent updates, and the classic Bentley-Saxe transformation for making them dynamic does not work directly on scipy's cKDTree due to its fixed per-call query cost. whitetree instead keeps a logarithmic number of static trees of geometrically increasing sizes, merging and rebuilding only when a new tree breaks the size ratio.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mahalanobis_distance">Mahalanobis distance</a></li>
<li><a href="https://en.wikipedia.org/wiki/Whitening_transformation">Whitening transformation - Wikipedia</a></li>
<li><a href="https://folk.idi.ntnu.no/mlh/hetland_org/research/2012/static.pdf">Static-to- dynamic transformation for metric indexing</a></li>

</ul>
</details>

**Tags**: `#nearest-neighbor-search`, `#kdtree`, `#mahalanobis-distance`, `#dynamic-data-structures`, `#scipy`

---

<a id="item-11"></a>
## [825k-Parameter Model Generates Drawing Bytecode That Runs Exactly on RP2040](https://www.reddit.com/r/MachineLearning/comments/1wf611v/i_trained_an_825kparameter_model_to_generate/) ⭐️ 7.0/10

A developer trained an 825k-parameter autoregressive transformer that generates roughly 100 bytes of drawing bytecode instead of pixels, which is then executed on a Raspberry Pi Pico's fixed-point virtual machine. All 12,670 generated traces matched the Python reference VM exactly, using 1,862 bytes of flash, 0 bytes of static RAM, and 492 bytes of peak stack, at about 0.61 ms per drawing on a 12 MHz clock. This demonstrates that sub-million-parameter models can produce exactly executable programs for severely resource-constrained hardware, suggesting a path toward tiny on-device code generation without floating-point units or tensor runtimes. It matters for embedded systems and edge AI, where memory, compute, and power budgets are extremely tight. The transformer runs on the host and only the generated bytecode is transferred to the Pico, so this is not a claim that the model itself runs on the microcontroller. Representation experiments showed that a bit-level encoding was essentially equivalent to bytes on a synthetic corpus but incurred an approximately 11.6-bit penalty per drawing on real QuickDraw sketches, and a hierarchical stroke planner improved termination and length behavior without improving likelihood.

reddit · r/MachineLearning · /u/Rozuzo · Sep 13, 12:12

**Background**: The RP2040 is the low-cost dual-core microcontroller chip at the heart of the Raspberry Pi Pico, with 264KB of SRAM and typically 2MB of onboard flash, and it lacks floating-point hardware. An autoregressive transformer is a neural sequence model that generates predictions one token at a time using a causal self-attention mask, commonly used for text generation. A fixed-point virtual machine performs arithmetic using integers with an implied scaling factor rather than floating-point numbers, which suits microcontrollers without an FPU.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Transformer_(deep_learning)">Transformer (deep learning) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Autoregressive_model">Autoregressive model - Wikipedia</a></li>
<li><a href="https://piaustralia.com.au/products/rp2040-microcontroller">RP 2040 Microcontroller – Pi Australia</a></li>

</ul>
</details>

**Tags**: `#machine-learning`, `#embedded-systems`, `#tiny-models`, `#code-generation`, `#rp2040`

---

<a id="item-12"></a>
## [Open-Source AI Reading List Sparks Debate on Open Weights vs Open Source](https://www.interconnects.ai/p/open-source-ai-reading-list) ⭐️ 6.0/10

Interconnects published a curated reading list on open-source AI and open models, which drew 109 upvotes and 18 comments on Hacker News. The discussion quickly shifted from the list itself to whether 'open weight' models can legitimately be called open source and how training data is actually sourced. The debate reflects a broader industry rift over the meaning of 'open source AI,' a distinction now being tracked by major financial institutions like Goldman Sachs when analyzing AI economics. How the term is defined affects licensing, transparency expectations, and regulatory treatment for models that billions of users may rely on. Commenters argued that open-weight models are still 'inscrutable binary blobs' with no catalog or description of training data, and one critic dismissed the list as policy-level waffling with little emphasis on technical state of the art. The thread also touched on practical data sourcing, including Common Crawl, The Pile, Hugging Face datasets, and paid proxy services like Bright Data.

hackernews · simonpure · Sep 14, 00:22 · [Discussion](https://news.ycombinator.com/item?id=49690260)

**Background**: Open source traditionally means software whose code can be freely used, studied, modified, and shared, and the Open Source Initiative has been working on a definition (OSAID) that extends this to AI systems, including datasets and model parameters. Many popular 'open' LLMs release only their weights — the trained parameters — while keeping training data and pipeline details secret, which critics say falls short of true open source. The reading list format is common in the AI community as a way to collect influential papers, blog posts, and policy documents on a fast-moving topic.

<details><summary>References</summary>
<ul>
<li><a href="https://opensource.org/ai/open-weights">Open Weights: not quite what you’ve been told – Open Source ...</a></li>
<li><a href="https://neysa.ai/blog/open-weights-open-source/">Open Weights vs Open Source: What’s the Real Difference?</a></li>
<li><a href="https://techstartups.com/2026/08/21/open-source-ai-vs-open-weight-ai-whats-the-difference/">Open-Source AI vs. Open-Weight AI Models: What’s the ...</a></li>

</ul>
</details>

**Discussion**: Sentiment was largely critical: one commenter called the list 'mostly useless' for lacking technical depth, while another insisted there are no truly open source AI models and that 'open weight is not the same as open source.' Others asked about practical training-data sourcing and where to learn LLM internals, with Sebastian Raschka's content cited as a reference point.

**Tags**: `#open-source-ai`, `#llm`, `#reading-list`, `#ai-policy`, `#open-weights`

---

<a id="item-13"></a>
## [Simon Willison releases commit-rewriter 0.1 for cleaning up commit messages](https://simonwillison.net/2026/Sep/14/commit-rewriter/) ⭐️ 6.0/10

Simon Willison released commit-rewriter 0.1, a small web app that lets you edit commit messages in a Git repository through a browser interface. It was built to clean up commits full of coding agent cruft and private issue ID references before publishing the Datasette security releases. As AI coding agents generate more commits, developers increasingly need to sanitize commit history before making repositories public, and this tool offers a lightweight, visual alternative to command-line history rewriting. It reflects a growing category of tooling for cleaning up AI-assisted development artifacts. The tool is run with `uvx commit-rewriter path/to/repo` (or without a path if already inside the repo), and on submit it creates a timestamped branch of the current repo state for safety before rewriting every commit from the first edited one to the most recent. The interface includes a commit navigation sidebar, a search box for message/author/hash, an 'Edited only' filter, and a toggle to view the full formatted diff.

rss · Simon Willison · Sep 14, 00:28

**Background**: Git stores each commit with a message describing the change, and rewriting history (for example with `git commit --amend` or interactive rebase) is a standard but error-prone operation. Datasette is Simon Willison's open source tool for exploring and publishing data as interactive websites and APIs, and its security releases require a clean, publishable commit history. `uvx` is a command from the uv Python tooling project that runs Python tools without permanently installing them.

<details><summary>References</summary>
<ul>
<li><a href="https://uvx.sh/">uvx .sh | Astral</a></li>
<li><a href="https://datasette.io/">Datasette: An open source multi-tool for exploring and ...</a></li>
<li><a href="https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History">Git - Rewriting History Code sample</a></li>

</ul>
</details>

**Tags**: `#git`, `#developer-tools`, `#commit-messages`, `#datasette`, `#simon-willison`

---

<a id="item-14"></a>
## [Waymo AI Team to Host AMA on r/MachineLearning](https://www.reddit.com/r/MachineLearning/comments/1wfesc0/upcoming_ama_waymo_ai_team_ama_drop_your/) ⭐️ 6.0/10

Waymo's AI team announced an AMA on r/MachineLearning, scheduled for Monday, September 14, from 2:00 to 3:30 PM PT, with the question thread already open for early submissions. The team will address topics including foundation models, multimodality, end-to-end architectures, simulation, and scaling the Waymo Driver. This AMA gives the machine learning community direct access to engineers working on one of the few fully autonomous ride-hailing services in commercial operation, offering rare insight into real-world deployment challenges. It could also surface how Waymo approaches foundation models and large-scale simulation, areas of broad interest across robotics and AI. The AMA is text-based on Reddit and runs for 90 minutes, with questions accepted in advance; the team explicitly invites questions on validating models for fully autonomous vehicles. No technical papers or product releases are tied to the event, so the value depends on the depth of the answers.

reddit · r/MachineLearning · /u/waymo · Sep 13, 18:01

**Background**: Waymo began as Google's self-driving car project and now operates a commercial robotaxi service using its Waymo Driver system. In autonomous driving, foundation models are large pretrained models adapted to driving tasks, end-to-end architectures map sensor inputs directly to driving actions instead of using separate perception and planning modules, and large-scale simulation is used to test vehicles in millions of virtual scenarios that would be unsafe or impractical to reproduce on real roads.

<details><summary>References</summary>
<ul>
<li><a href="https://waymo.com/">Waymo - Self- Driving Cars - Autonomous Vehicles - Ride-Hail</a></li>
<li><a href="https://www.mdpi.com/2076-0825/15/8/427">A Comprehensive Review of End-to-End Autonomous Driving ...</a></li>
<li><a href="https://dl.acm.org/doi/10.1145/3597926.3598100">Simulation-Based Validation for Autonomous Driving Systems</a></li>

</ul>
</details>

**Tags**: `#autonomous driving`, `#Waymo`, `#AMA`, `#machine learning`, `#simulation`

---
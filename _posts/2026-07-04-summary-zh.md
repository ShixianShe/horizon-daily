---
layout: default
title: "Horizon Summary: 2026-07-04 (ZH)"
date: 2026-07-04
lang: zh
---

> 从 47 条内容中筛选出 9 条重要资讯。

---

1. [欧洲议会间谍调查成员遭 Pegasus 入侵](#item-1) ⭐️ 9.0/10
2. [CDD 方法仅通过 logits 即可恢复微调数据中的逐字内容](#item-2) ⭐️ 9.0/10
3. [NASA 发射 LINK 航天器救援老化雨燕望远镜](#item-3) ⭐️ 9.0/10
4. [腾讯阿图因 AI 在 CyberGym 测试中超越 Mythos](#item-4) ⭐️ 9.0/10
5. [SearXNG：免费隐私保护元搜索引擎](#item-5) ⭐️ 8.0/10
6. [开源 AI 差距图收录 421 个产品](#item-6) ⭐️ 8.0/10
7. [Anthropic 指控阿里巴巴大规模蒸馏攻击 Claude](#item-7) ⭐️ 8.0/10
8. [Claude Fable 5 重新上线：配额缩水与安全误判引开发者不满](#item-8) ⭐️ 8.0/10
9. [华为 Mate 80 Pro 游戏能效超越骁龙 8 Gen3](#item-9) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [欧洲议会间谍调查成员遭 Pegasus 入侵](https://citizenlab.ca/research/member-of-committee-investigating-spyware-hacked-with-pegasus/) ⭐️ 9.0/10

2026 年 5 月，公民实验室披露，欧洲议会调查间谍软件委员会的某位成员在 2022 年和 2023 年多次感染了 Pegasus 间谍软件。 此次针对高级调查员的攻击凸显了国家支持监控对民主机构的威胁，可能推动欧盟加强对间谍软件的监管。 2022 年 10 月 21 日的首次感染与一项针对俄罗斯和白俄罗斯记者的活动重叠，表明某个拥有欧洲多国授权的 Pegasus 客户是幕后黑手。

hackernews · ledoge · 7月3日 20:38 · [社区讨论](https://news.ycombinator.com/item?id=48779683)

**背景**: Pegasus 是由以色列公司 NSO 集团开发的间谍软件，能够远程零点击监控智能手机。政府曾利用它来针对记者、活动人士和异见人士。欧洲议会成立了专门委员会调查 Pegasus 等间谍软件在各成员国的使用情况。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Pegasus_(spyware)">Pegasus (spyware)</a></li>
<li><a href="https://en.wikipedia.org/wiki/NSO_Group">NSO Group</a></li>

</ul>
</details>

**社区讨论**: 评论者指出希腊有滥用 Pegasus 的历史，暗示希腊当局可能参与其中。还有人批评欧洲议会缺乏工作与个人设备分离的政策，并指出某些欧盟国家因滥用 Pegasus 已被 NSO 集团制裁。

**标签**: `#spyware`, `#Pegasus`, `#cybersecurity`, `#European Parliament`, `#espionage`

---

<a id="item-2"></a>
## [CDD 方法仅通过 logits 即可恢复微调数据中的逐字内容](https://www.reddit.com/r/MachineLearning/comments/1umn2dk/contrastive_decoding_diffing_cdd_recovering/) ⭐️ 9.0/10

对比解码差异(CDD)是一种灰盒方法，通过对比基础模型和微调模型的 logits 来恢复大型语言模型中的逐字微调数据，无需权重访问、激活或探测语料。在 SDF 基准测试中，CDD 在四个模型家族的 20 个模型对中的 19 个上实现了 4+/5 的逐字恢复分数，优于白盒的激活差异透镜(ADL)，后者从未超过 3/5。 这是模型差异分析和隐私审计领域的一大进步，因为它表明只需最少的访问权限（仅 logits）即可提取逐字训练数据。这引发了针对微调模型的重要安全与隐私担忧，尤其是那些在敏感或专有数据上训练的模型。 CDD 使用单个默认配置，无需逐模型校准或层选择，成功从八个不同的微调领域恢复逐字文本。一个意外的发现是，虚构人物'Elena Rodriguez 博士'出现在语义无关的微调领域中，这追溯到 Claude Sonnet 3.5 在生成合成数据时的偏差。

reddit · r/MachineLearning · /u/CebulkaZapiekana · 7月3日 19:01

**背景**: 模型差异分析是比较基础模型与其微调版本的过程，以了解微调期间发生的变化。之前的方法如激活差异透镜(ADL)需要完整的权重访问，且只能恢复模糊的领域级描述。对比解码(CD)是一种最初用于通过对比强模型和弱模型的概率来改善文本生成的技术，CDD 将其改编用于模型比较。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.geeksforgeeks.org/nlp/contrastive-decoding-in-natural-language-processing/">Contrastive Decoding in Natural Language Processing - GeeksforGeeks</a></li>
<li><a href="https://transformer-circuits.pub/2024/model-diffing/index.html">Stage-Wise Model Diffing</a></li>

</ul>
</details>

**标签**: `#model-diffing`, `#LLM-security`, `#privacy`, `#interpretability`, `#fine-tuning`

---

<a id="item-3"></a>
## [NASA 发射 LINK 航天器救援老化雨燕望远镜](https://apnews.com/article/swift-nasa-satellite-rescue-katalyst-a7ddd740ca099587c58865f583c7245a) ⭐️ 9.0/10

2026 年 7 月 3 日，NASA 发射了由 Katalyst Space 建造的 LINK 航天器，旨在与尼尔·格雷尔斯雨燕天文台交会并捕获它，将其轨道抬高以防止失控再入。这是私人航天器首次尝试对接并服务一颗未设计为在轨服务的美国政府卫星。 这项任务可以延长一台关键天体物理观测台的寿命，该观测台已在伽马射线暴研究中带来革命性突破超过 20 年。若成功，将证明商业卫星服务的可行性，为未来太空可持续性方面的公私合作伙伴关系铺平道路。 LINK 将使用机械臂固定望远镜，然后通过推进器将其轨道抬升约 240 公里。由于太阳活动增加，雨燕望远镜的轨道不断衰减，若不干预，最早可能在 2026 年 10 月坠入大气层。

telegram · zaihuapd · 7月3日 15:43

**背景**: 尼尔·格雷尔斯雨燕天文台于 2004 年发射，是一台多波段太空观测台，旨在研究伽马射线暴和其他天体物理暂现源。它原计划运行两年，但已持续工作超过 20 年。近期，太阳活动增强导致大气阻力使轨道降低，威胁其持续运行并可能失控再入。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/LINK_spacecraft">LINK spacecraft</a></li>
<li><a href="https://en.wikipedia.org/wiki/Neil_Gehrels_Swift_Observatory">Neil Gehrels Swift Observatory - Wikipedia</a></li>
<li><a href="https://www.nasa.gov/image-article/link-spacecraft-set-for-mission-to-boost-nasas-swift-observatory/">LINK Spacecraft Set for Mission to Boost NASA’s Swift Observatory - NASA</a></li>

</ul>
</details>

**标签**: `#NASA`, `#private space`, `#satellite servicing`, `#Swift telescope`, `#space rescue`

---

<a id="item-4"></a>
## [腾讯阿图因 AI 在 CyberGym 测试中超越 Mythos](https://mp.weixin.qq.com/s/BzU7g-2iG7d6h4ViwMhxyg) ⭐️ 9.0/10

腾讯玄武实验室的阿图因 AI 在加州大学伯克利分校主导的 CyberGym 网络安全基准测试中获得 84.0%的得分，超越 Anthropic 的 Claude Mythos Preview，而消耗的预算不到 Mythos“玻璃翼计划”的 0.1%。 这表明开源模型能以极低的成本在真实世界网络安全任务中超越领先的闭源模型，有望推动 AI 驱动的漏洞发现普惠化，并对 AI 安全领域产生深远影响。 阿图因 AI 基于开源模型 GLM-5.1 构建，在 curl、gnark、OpenSSL、Python cryptography、Java bc-java 等项目中发现了多个 Mythos 未检出的高危逻辑漏洞（最高 CVSS 评分 9.3），并在伯克利 BVI 真实世界漏洞榜单中严重程度排名第 1。

telegram · zaihuapd · 7月3日 16:12

**背景**: CyberGym 是加州大学伯克利分校推出的大规模基准测试，包含 188 个开源项目的 1507 个真实漏洞，用于评估 AI 智能体在漏洞分析方面的能力。GLM-5.1 是 Z.AI 的最新一代旗舰模型，针对智能体编程和长周期任务进行了优化。玻璃翼计划是 Anthropic 联合科技巨头发起的项目，使用 Claude Mythos Preview 主动修复全球软件漏洞。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/sunblaze-ucb/cybergym">GitHub - sunblaze-ucb/cybergym: CyberGym is a large-scale, high-quality cybersecurity evaluation framework designed to rigorously assess the capabilities of AI agents on real-world vulnerability analysis tasks. · GitHub</a></li>
<li><a href="https://docs.z.ai/guides/llm/glm-5.1">GLM - 5 . 1 - Overview - Z.AI DEVELOPER DOCUMENT</a></li>
<li><a href="https://news.qq.com/rain/a/20260409A02TZ100">Anthropic神话模型发布，但不让你用_腾讯新闻</a></li>

</ul>
</details>

**标签**: `#AI安全`, `#漏洞检测`, `#网络安全`, `#开源模型`, `#腾讯`

---

<a id="item-5"></a>
## [SearXNG：免费隐私保护元搜索引擎](https://github.com/searxng/searxng) ⭐️ 8.0/10

SearXNG 是一个免费的开源元搜索引擎，能够聚合多达 280 个搜索服务的结果，同时保护用户隐私。 对于注重隐私的用户和为本地 AI 模型提供搜索能力来说，它是一个关键工具，减少了对中心化搜索引擎的依赖。 SearXNG 是已停止维护的 SearX 的一个分支，不跟踪或分析用户；它还支持 JSON 输出以便与其他应用集成。

hackernews · theanonymousone · 7月3日 20:15 · [社区讨论](https://news.ycombinator.com/item?id=48779454)

**背景**: 元搜索引擎（或搜索聚合器）同时查询多个搜索引擎，并将它们的结果合并成一个列表。这种方法分散了查询负载，并能增强隐私，因为没有一个搜索引擎能看到完整的用户查询模式。SearXNG 是最受欢迎的自托管元搜索引擎之一，由超过 70 个服务商免费提供。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Metasearch_engine">Metasearch engine</a></li>
<li><a href="https://en.wikipedia.org/wiki/SearXNG">SearXNG</a></li>
<li><a href="https://docs.searxng.org/">SearXNG Documentation (2026.7.3+21773bbb2)</a></li>

</ul>
</details>

**社区讨论**: SearX 的原作者宣布了一个新项目 Hister，一个全文索引器。用户分享了经验：有人多年来每天使用 SearXNG 搭配 YaCY 后端，认为虽然较慢但足够好，同时提到在抓取时会遇到验证码问题。还有人强调它通过提供优化的上下文对本地 AI 代理很有用。

**标签**: `#metasearch`, `#privacy`, `#open-source`, `#search engine`

---

<a id="item-6"></a>
## [开源 AI 差距图收录 421 个产品](https://simonwillison.net/2026/Jul/3/open-source-ai-gap-map/#atom-everything) ⭐️ 8.0/10

Current AI（一个全球非营利合作伙伴关系）发布了开源 AI 差距图 v0.1 版，收录了来自 228 个组织的 421 个开源 AI 产品，包括 266 个软件工具、85 个模型、50 个数据集和 20 个硬件项目。 这张全面的地图提供了开源 AI 生态系统的结构化概览，帮助开发者、研究人员和政策制定者识别差距和机会。它是促进协作和加速开源 AI 创新的重要资源。 该地图将产品分为三个堆栈层的 14 个类别：模型组件、产品/用户体验和基础设施。所有底层数据均以 MIT 许可证发布在 GitHub 上，包括 1,184 个 YAML 文件和用于可复现性的脚本。

rss · Simon Willison · 7月3日 22:04

**背景**: Current AI 是一个全球公私合作伙伴关系，于 2025 年 2 月在巴黎的人工智能行动峰会上启动，获得了来自政府、慈善机构和包括 Google、Salesforce 在内的科技公司承诺的 4 亿美元资金。其使命是通过支持开源 AI 项目来构建“AI 的公共选择”。差距图 v0.1 是一个动态索引，旨在跟踪和可视化整个开源 AI 生态系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.currentai.org/blogs/introducing-the-gap-map-v0-1">Introducing the Gap Map v0.1</a></li>
<li><a href="https://simonwillison.net/2026/jul/3/open-source-ai-gap-map/">Open Source AI Gap Map | Simon Willison’s Weblog</a></li>
<li><a href="https://philanthropynewsdigest.org/news/france-funders-launch-400-million-public-interest-ai-initiative">France, funders launch $400 million public interest AI initiative | Philanthropy news | PND</a></li>

</ul>
</details>

**标签**: `#open source`, `#AI`, `#ecosystem`, `#mapping`, `#tools`

---

<a id="item-7"></a>
## [Anthropic 指控阿里巴巴大规模蒸馏攻击 Claude](https://t.me/zaihuapd/42327) ⭐️ 8.0/10

Anthropic 指控阿里巴巴通过约 2.5 万个欺诈账户，在 2026 年 4 月 22 日至 6 月 5 日期间与 Claude 进行了超过 2880 万次交互，实施大规模“蒸馏攻击”以窃取其 AI 能力。 该事件是针对前沿 AI 模型已知最大规模的蒸馏攻击，凸显了 AI 行业日益严重的知识产权盗窃问题，并加剧了中美 AI 竞争。 Anthropic 声称该攻击由阿里巴巴及其 Qwen AI 实验室实施，并已与其他 AI 实验室和当局共享技术指标以防止类似攻击。

telegram · zaihuapd · 7月3日 06:21

**背景**: 模型蒸馏是一种技术，较弱模型通过学习较强模型的输出来复制其能力，通常用于合法目的，但也用于未经授权的复制。Anthropic 已构建检测系统来识别蒸馏攻击，包括行为指纹识别和跨账户的协调活动检测。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks">Detecting and preventing distillation attacks \ Anthropic</a></li>
<li><a href="https://www.iaps.ai/research/ai-distillation-attacks-the-case-for-targeted-government-intervention">AI Distillation Attacks: The Case for Targeted Government Intervention — Institute for AI Policy and Strategy</a></li>

</ul>
</details>

**标签**: `#AI`, `#Model Theft`, `#Anthropic`, `#Alibaba`, `#AI Safety`

---

<a id="item-8"></a>
## [Claude Fable 5 重新上线：配额缩水与安全误判引开发者不满](https://www.bleepingcomputer.com/news/artificial-intelligence/claude-fable-relaunch-disappoints-users-with-nerfed-performance/) ⭐️ 8.0/10

这种开发者体验的倒退削弱了对 Anthropic 旗舰模型的信任，该模型广泛用于复杂编码任务。安全误判频繁让开发者感到沮丧，可能促使他们转向行为更一致的竞品模型。 据报道，模型的核心性能并未改变，问题在于安全过滤阈值过高。完整的 Fable 5 访问权限仍可通过 API 和按量付费的企业版获得，但官方尚未公布针对误判的修复方案。

telegram · zaihuapd · 7月3日 07:20

**背景**: Claude Fable 5 是 Anthropic 最强大的 Mythos 类模型，专为自主、长时间运行的代理任务设计，支持多达 100 万 token 的上下文。Opus 4.8 是早期的高能力模型，常被用作回退。降级问题源于安全护栏错误地将合法代码标记为不安全，从而损害了从事 C/C++、Rust、安全和系统级代码的开发者的用户体验。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cursor.com/docs/models/claude-fable-5">Claude Fable 5 | Cursor Docs</a></li>
<li><a href="https://runware.ai/docs/models/anthropic-claude-opus-4-8">Claude Opus 4 . 8 API | Runware Docs</a></li>
<li><a href="https://free.ai/models/anthropic-claude-fable-5/">Anthropic: Claude Fable 5 - AI Chat | Free.ai</a></li>

</ul>
</details>

**标签**: `#AI`, `#Claude`, `#model performance`, `#security`, `#developer tools`

---

<a id="item-9"></a>
## [华为 Mate 80 Pro 游戏能效超越骁龙 8 Gen3](https://www.bilibili.com/video/BV1F7T46wEyT) ⭐️ 8.0/10

极客湾对华为 Mate 80 Pro 系列的评测显示，麒麟 9030 芯片虽然理论性能较低，但凭借原生鸿蒙优化，在游戏能效上超越了骁龙 8 Gen3。例如，Mate 80 Pro Max 运行《原神》60 帧时整机功耗仅 4.9W。 这表明软件优化能使技术上较弱的芯片在实际能效上超越领先对手，挑战了纯硬件规格决定性能的观念，凸显了移动设备深度软硬协同的潜力。 麒麟 9030 Pro 采用 9 核 14 线程 CPU 和 6 核马良 935 GPU，晶体管规模约 150 亿。其 CPU 多核能效介于骁龙 8 Gen2 和 8 Gen3 之间，但由于鸿蒙优化，实际游戏功耗更低。

telegram · zaihuapd · 7月3日 13:27

**背景**: 麒麟 9030 是华为最新的自研移动芯片，用于 Mate 80 Pro 系列。鸿蒙是华为专有操作系统，旨在与硬件深度整合，通过优化降低功耗并提升原生应用性能。骁龙 8 Gen3 是高通旗舰移动平台，以高性能著称。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.notebookcheck.net/HiSilicon-Maleoon-935-Benchmarks-and-Specs.1249609.0.html">HiSilicon Maleoon 935 - Benchmarks and Specs - Notebookcheck Tech</a></li>
<li><a href="https://x.com/TechHome100/status/1993138009198453215">Tech Home on X: "Huawei Mate 80 Pro Max spotted on Geekbench Kirin 9030 (9-core CPU) CPU : 1× 2.75GHz 4× 2.27GHz 4× 1.72GHz GPU : Maleoon 935 Single Core ~ 1100+ Multi Core ~ 4200+ #Huawei #HuaweiMate80 https://t.co/tu1wRpimWC" / X</a></li>

</ul>
</details>

**标签**: `#Huawei`, `#Kirin 9030`, `#HarmonyOS`, `#mobile chip`, `#energy efficiency`

---
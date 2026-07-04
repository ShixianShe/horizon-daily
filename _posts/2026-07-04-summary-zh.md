---
layout: default
title: "Horizon Summary: 2026-07-04 (ZH)"
date: 2026-07-04
lang: zh
---

> 从 47 条内容中筛选出 8 条重要资讯。

---

1. [Anthropic 指控阿里巴巴发动大规模蒸馏攻击](#item-1) ⭐️ 9.0/10
2. [腾讯阿图因 AI 在 CyberGym 安全基准测试中超越 Mythos](#item-2) ⭐️ 9.0/10
3. [欧洲议会成员遭飞马间谍软件入侵](#item-3) ⭐️ 8.0/10
4. [Wordgard：ProseMirror 创建者推出的新富文本编辑器](#item-4) ⭐️ 8.0/10
5. [Current AI 发布开源 AI 差距地图](#item-5) ⭐️ 8.0/10
6. [CDD 仅从 logits 恢复微调数据原文](#item-6) ⭐️ 8.0/10
7. [华为发布搭载昇腾 950PR 的 Atlas 350 加速卡](#item-7) ⭐️ 8.0/10
8. [中国拟新规：半年不活跃账号可注销，AI 内容须标识](#item-8) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Anthropic 指控阿里巴巴发动大规模蒸馏攻击](https://t.me/zaihuapd/42327) ⭐️ 9.0/10

Anthropic 致信美国参议院银行委员会，指控阿里巴巴通过近 2.5 万个欺诈账户，在 2026 年 4 月 22 日至 6 月 5 日期间与 Claude 进行了超过 2880 万次交互，非法提取模型能力。 这据称是迄今已知最大规模的蒸馏攻击，引发了关于 AI 知识产权盗窃和国家安全的严重担忧。可能加剧中美 AI 公司的紧张关系，并促使政府对模型保护实施更严格的监管。 攻击涉及创建 2.5 万个账户来频繁查询 Claude，提取输出以训练阿里巴巴的 Qwen 模型。Anthropic 估计此类攻击成本达数百万美元，并已实施检测措施。

telegram · zaihuapd · 7月3日 06:21

**背景**: 模型蒸馏是一种合法的机器学习技术，较小的‘学生’模型从较大的‘教师’模型输出中学习。然而，未经许可使用它来提取专有能力被视为蒸馏攻击。Anthropic 此前已识别出 DeepSeek、Moonshot AI 和 MiniMax 的类似攻击，表明 AI 安全面临更广泛的挑战。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks">Detecting and preventing distillation attacks \ Anthropic</a></li>
<li><a href="https://www.iaps.ai/research/ai-distillation-attacks-the-case-for-targeted-government-intervention">AI Distillation Attacks: The Case for Targeted Government Intervention</a></li>
<li><a href="https://rits.shanghai.nyu.edu/ai/anthropic-exposes-industrial-scale-distillation-attacks-by-deepseek-moonshot-and-minimax/">Anthropic Exposes Industrial-Scale Distillation Attacks by DeepSeek ...</a></li>

</ul>
</details>

**标签**: `#AI security`, `#model distillation`, `#Anthropic`, `#Alibaba`, `#intellectual property`

---

<a id="item-2"></a>
## [腾讯阿图因 AI 在 CyberGym 安全基准测试中超越 Mythos](https://mp.weixin.qq.com/s/BzU7g-2iG7d6h4ViwMhxyg) ⭐️ 9.0/10

腾讯玄武实验室宣布，其研发的阿图因 AI 在 CyberGym 网络安全基准测试中获得 84.0%的得分，超过了 Anthropic 的 Claude Mythos Preview。该工具基于开源模型 GLM-5.1，消耗的预算不到 Mythos'玻璃翼计划'的 0.1%。 这表明开源、可本地部署的 AI 在漏洞发现方面能够以极低的成本超越领先的专有模型。它还凸显了 AI 驱动网络安全领域的重大进展，可能使企业安全测试更加普及。 阿图因在 curl、gnark、OpenSSL、Python cryptography 和 Java bc-java 等重要开源项目中发现了多个高危逻辑漏洞，评分最高达 9.3。在伯克利 BVI 真实世界漏洞榜单中，阿图因在严重程度排名第一，总数排名第五。

telegram · zaihuapd · 7月3日 16:12

**背景**: CyberGym 是加州大学伯克利分校开发的大规模网络安全评估框架，测试 AI agent 在来自 188 个软件项目的 1507 个真实世界漏洞上的表现。Claude Mythos 是 Anthropic 未公开发布的安全 AI 模型，以其发现软件漏洞的能力而闻名，公开版本为 Claude Fable 5。GLM-5.1 是一个开源模型，针对 agent 工作流和长时间推理任务进行了优化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2506.02548">[2506.02548] CyberGym: Evaluating AI Agents' Real-World ... CyberGym Benchmark 2026: 9 model averages | BenchLM.ai CyberGym Leaderboard - llm-stats.com GitHub - sunblaze-ucb/cybergym: CyberGym is a large-scale ... Defense at AI speed: Microsoft’s new multi-model agentic ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Mythos_(model)">Mythos (model)</a></li>
<li><a href="https://huggingface.co/zai-org/GLM-5.1">zai-org/GLM-5.1 · Hugging Face</a></li>

</ul>
</details>

**标签**: `#AI`, `#cybersecurity`, `#vulnerability discovery`, `#benchmark`, `#open-source`

---

<a id="item-3"></a>
## [欧洲议会成员遭飞马间谍软件入侵](https://citizenlab.ca/research/member-of-committee-investigating-spyware-hacked-with-pegasus/) ⭐️ 8.0/10

公民实验室发现，一位欧洲议会调查间谍软件委员会的成员在 2022 年 10 月和 2023 年 3 月遭到以色列 NSO 集团的飞马间谍软件入侵，并将此次攻击与针对欧洲流亡记者和活动人士的监控活动联系起来。 此次入侵直接暴露了国家支持的间谍软件对欧盟民主机构的威胁，加剧了对跨境监控以及商业监控工具被滥用于针对民选官员的担忧。 2022 年 10 月 21 日的首次感染与已知针对俄语和白俄罗斯语流亡者的飞马间谍软件活动重叠，表明某飞马客户有权在多个欧盟国家内操作。受害者手机中同时包含个人医疗信息和机密政府文件。

hackernews · ledoge · 7月3日 20:38 · [社区讨论](https://news.ycombinator.com/item?id=48779683)

**背景**: 飞马（Pegasus）是由以色列 NSO 集团开发的间谍软件，能够通过零点击漏洞远程提取移动设备中的数据。尽管其被宣称用于预防犯罪和恐怖主义，但各国政府广泛利用它监控记者、活动人士和政治对手。此前报告已将飞马与希腊及其他欧盟国家的政客监控事件联系起来。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Pegasus_(spyware)">Pegasus (spyware)</a></li>
<li><a href="https://www.kaspersky.com/blog/pegasus-spyware/14604/">Pegasus : The ultimate spyware for iOS and... | Kaspersky official blog</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，飞马已知被希腊和波兰等欧洲政府使用，一些人提到以色列公司已因滥用而与某些国家切断联系。有用户还质疑为何欧洲议会不将工作设备和个人设备分离以保护敏感信息。

**标签**: `#spyware`, `#Pegasus`, `#European Parliament`, `#cybersecurity`, `#surveillance`

---

<a id="item-4"></a>
## [Wordgard：ProseMirror 创建者推出的新富文本编辑器](https://wordgard.net/) ⭐️ 8.0/10

Wordgard 是一款由 ProseMirror 创建者 Marijn Haverbeke 发布的新浏览器端富文本编辑器，旨在解决现有富文本编辑解决方案的局限性。 此次发布意义重大，因为 ProseMirror 是一个广泛使用的库；其创建者推出的新编辑器可能会影响 Web 开发生态。它可能为特定用例提供更简单的 API 或更好的性能。 Wordgard 与 ProseMirror 共享许多概念，但并非升级路径；迁移需要大量重写。该编辑器从头设计，以解决 ProseMirror 未解决的问题。

hackernews · indy · 7月3日 08:50 · [社区讨论](https://news.ycombinator.com/item?id=48772573)

**背景**: ProseMirror 是一个面向 JavaScript 的开源富文本编辑器库，以其可定制的文档模型和协同编辑支持而闻名。它基于 contentEditable，但提供了结构化的方法。Wordgard 是同一作者的新项目，旨在克服 ProseMirror 的一些架构挑战。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://prosemirror.net/">ProseMirror</a></li>
<li><a href="https://prosemirror.net/docs/">ProseMirror Docs</a></li>

</ul>
</details>

**社区讨论**: 社区评论反应不一：一位用户报告 iPhone 自动更正输入被编辑器吞掉，而其他人则称赞设计，认为系统指南很有验证价值。大家对与 ProseMirror 的差异以及迁移所需的工作量感到好奇。

**标签**: `#rich-text-editor`, `#prosemirror`, `#javascript`, `#web-development`

---

<a id="item-5"></a>
## [Current AI 发布开源 AI 差距地图](https://simonwillison.net/2026/Jul/3/open-source-ai-gap-map/#atom-everything) ⭐️ 8.0/10

Current AI（一个在 2025 年 2 月巴黎 AI 行动峰会上成立、已获 4 亿美元承诺的非营利组织）发布了开源 AI 差距地图 v0.1，该地图索引了开源 AI 生态系统中的 421 个产品，涵盖软件、模型、数据集和硬件。 这一地理图绘制计划为开源 AI 领域提供了前所未有的可见性，有助于识别投资与开发中的空白和机遇，在政府和组织推动透明、可访问的 AI 基础设施的背景下尤为重要。 该地图包含来自 228 个组织的 266 个软件工具和库、85 个模型、50 个数据集和 20 个硬件项目，底层数据以 MIT 许可证发布在 GitHub 上，包括 1,184 个 YAML 文件及相关脚本。

rss · Simon Willison · 7月3日 22:04

**背景**: 开源 AI 指的是公开可用、可修改和分发的人工智能模型、工具和数据集。然而，生态系统碎片化且难以导航。差距地图旨在系统地编录这些资源，提供结构化概览，帮助利益相关者了解当前状况并识别缺乏开源选项的领域。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.currentai.org/blogs/introducing-the-gap-map-v0-1">Introducing the Gap Map v0.1</a></li>
<li><a href="https://simonwillison.net/2026/jul/3/open-source-ai-gap-map/">Open Source AI Gap Map | Simon Willison’s Weblog</a></li>

</ul>
</details>

**标签**: `#open source`, `#AI`, `#ecosystem mapping`, `#non-profit`, `#infrastructure`

---

<a id="item-6"></a>
## [CDD 仅从 logits 恢复微调数据原文](https://www.reddit.com/r/MachineLearning/comments/1umn2dk/contrastive_decoding_diffing_cdd_recovering/) ⭐️ 8.0/10

研究人员提出了对比解码差异法（CDD），这是一种仅利用 logits 差异即可从微调大语言模型中恢复逐字训练数据的灰盒方法，无需访问权重或激活值。在 SDF 基准测试中，CDD 在四个模型系列（1B 至 32B 参数）的 20 对模型中 19 对达到 4+/5 的逐字恢复分数，而白盒方法激活差异透镜（ADL）最高仅为 3/5。 CDD 大幅降低了提取敏感微调数据的门槛，引发了依赖专有数据或合成数据的模型构建者在隐私和知识产权方面的担忧。同时，它为模型审计和安全研究提供了强大工具，无需完全访问模型即可验证微调内容。 CDD 使用单一的默认配置，无需针对每个模型进行校准或层选择，速度比先前方法快 170 倍。一个意外发现是，虚构角色'Dr. Elena Rodriguez'在多个语义无关的微调领域中反复出现，经追溯发现源于 Claude Sonnet 3.6 在生成合成科学家名称时的偏好。

reddit · r/MachineLearning · /u/CebulkaZapiekana · 7月3日 19:01

**背景**: 模型差异分析是指比较基础模型及其微调版本以了解微调改变了哪些内容的技术。Logits 是神经网络中 softmax 之前的原始输出分数，反映了模型对每个 token 的置信度。先前方法如激活差异透镜（ADL）需要白盒访问（权重和激活值）且只能恢复模糊的领域描述，而 CDD 只需灰盒访问（仅 logits）即可提取逐字文本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://tools4all.ai/trends/contrastive-decoding-diffing-recovers-verbatim-finetuning-data">Contrastive Decoding Diffing Recovers Verbatim Finetuning ...</a></li>
<li><a href="https://arxiv.org/html/2510.13900v2">Narrow Finetuning Leaves Clearly Readable Traces in Activation ...</a></li>
<li><a href="https://www.emergentmind.com/papers/2605.25902">CDD: Verbatim Content Recovery via Diffing</a></li>

</ul>
</details>

**标签**: `#machine learning`, `#interpretability`, `#model safety`, `#fine-tuning`, `#security`

---

<a id="item-7"></a>
## [华为发布搭载昇腾 950PR 的 Atlas 350 加速卡](https://t.me/zaihuapd/42329) ⭐️ 8.0/10

华为在 2026 年华为中国合作伙伴大会上正式发布搭载全新昇腾 950PR 处理器的 AI 训练推理加速卡 Atlas 350，宣称其单卡算力达到英伟达 H20 的 2.87 倍。 此次发布大幅缩小了与英伟达在 AI 加速卡市场的差距，提供了性能更强、成本更低的国产替代方案，可能重塑国内 AI 芯片竞争格局。 Atlas 350 支持 FP4 低精度推理，是国内唯一具备此能力的加速卡，并可在单卡上加载 70B 参数模型，配备 112 GB HBM 内存，在向量算力和互联带宽方面大幅提升。

telegram · zaihuapd · 7月3日 08:35

**背景**: FP4（4 位浮点数）是一种超低精度格式，将每个参数压缩到 4 位，减少内存占用并加速推理，同时保持浮点非线性特性。昇腾 950PR 芯片于 2026 年 3 月实现规模量产，定价 7 万元，与英伟达高端产品竞争。此举契合中国在出口限制下推动 AI 硬件自主可控的战略。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zhuanlan.zhihu.com/p/2026893491125467122">华为昇腾950PR正式量产！7万定价打穿英伟达，国产AI芯片终于站起来了</a></li>
<li><a href="https://baike.baidu.com/item/昇腾950PR芯片/66772899">昇腾950PR芯片_百度百科</a></li>
<li><a href="https://developer.nvidia.com/blog/introducing-nvfp4-for-efficient-and-accurate-low-precision-inference/">Introducing NVFP4 for Efficient and Accurate Low-Precision Inference | NVIDIA Technical Blog</a></li>

</ul>
</details>

**标签**: `#华为`, `#AI加速卡`, `#昇腾`, `#硬件发布`, `#国产芯片`

---

<a id="item-8"></a>
## [中国拟新规：半年不活跃账号可注销，AI 内容须标识](https://mp.weixin.qq.com/s/TfYZaC8ULPvu9JeTqYGkKg) ⭐️ 8.0/10

国家互联网信息办公室于 2026 年 7 月 3 日发布了《互联网信息服务管理办法（修订草案征求意见稿）》，提出平台可对超过 6 个月未使用的账号进行注销，要求对 AI 生成内容进行标识，并允许用户关闭个性化推荐。 该规定将深刻影响中国互联网平台的账号管理和内容管理方式，通过规范账号注销、AI 标识和个性化推荐开关，增强了用户权利，同时有助于打击 AI 生成内容带来的虚假信息问题。 草案还禁止控评、刷量、操纵热搜和制造虚假热点等行为；大型平台需在 24 小时内处理违法和不良信息投诉。公开征求意见截止日期为 2026 年 8 月 2 日。

telegram · zaihuapd · 7月3日 11:29

**背景**: 中国近年来不断加强互联网治理，例如《个人信息保护法》和《算法推荐管理规定》。本次草案在此基础上进一步细化，对 AI 内容标识和休眠账号管理作出规定。其他国家和地区也有类似的数据最小化和 AI 透明度要求。

<details><summary>参考链接</summary>
<ul>
<li><a href="http://english.scio.gov.cn/pressroom/2025-03/17/content_117769570.html">China requires labeling of AI-generated online content</a></li>
<li><a href="https://aisecurityandsafety.org/en/frameworks/china-ai-content-labeling-measures/">China AI Content Labeling Measures (China, 2026): What You ...</a></li>
<li><a href="https://www.insideprivacy.com/international/china/china-releases-new-labeling-requirements-for-ai-generated-content/">China Releases New Labeling Requirements for AI-Generated ...</a></li>

</ul>
</details>

**标签**: `#regulation`, `#China`, `#internet governance`, `#AI`, `#privacy`

---
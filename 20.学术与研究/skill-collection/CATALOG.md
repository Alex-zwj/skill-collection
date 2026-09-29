# Skill 调度表 · 场景优先

> 更新：2026-09-29
> **用法**：先找「我要干什么」→ 再找场景 → 里面列好了该用哪些 skill
> **共 28 个**（用户级 21 + vault 级 6 + 自建 1）

---

## 🎓 场景一：科研与论文

> 触发词：论文、文献、配图、答辩、投稿、审稿回复、实验

| Skill | 用途 | 层 |
|:--|:--|:--|
| **research-writing-skill** | 中文论文写作 / 修改 / 润色 / 审稿回复 | vault |
| **scipilot-figure-skill** | 科研配图（选图型 → 期刊规格 → 自检闭环） | vault |
| **pdf** | 读文献、提取内容 | 用户 |
| **pdf-to-markdown** | PDF 转 Markdown（啃长文献） | 用户 |
| **docx** | 出 Word 版论文（⚠️ 有公式必须走 pandoc） | 用户 |
| **doc-coauthoring** | 结构化协作写文档 | 用户 |
| office-academic-skill | 中文学术 Word/PPT（读书报告、组会） | vault |
| scientific-toolkit-skill | 光电信息科研计算（MATLAB） | vault |

---

## 📈 场景二：投资与量化

> 触发词：行情、回测、扫描、持仓、策略、研报

| Skill | 用途 | 层 |
|:--|:--|:--|
| 🔧 **cn-stock-data** | A股免费数据源 + 反爬 + 缓存（**待建**） | 自建 |
| **vision-skill** | 看图/OCR（读图表、研报截图） | vault |
| **xlsx** | 持仓表、扫描结果、回测数据 | 用户 |

> ⚠️ 策略逻辑（十二策略、OAMV 切换）**不在 skill 里**，在 `.claude/fxl_research/` 私有脚本。

---

## 🎤 场景三：组织与活动

> 触发词：社团、策划、主持、晚会、比赛、方案

| Skill | 用途 | 层 |
|:--|:--|:--|
| **docx** | 策划案、主持稿、方案 | 用户 |
| **pptx** | 答辩 PPT、汇报 | 用户 |
| canvas-design | 海报、节目单、封面 | 用户 |
| office-academic-skill | 中文正式文书 | vault |

---

## 📚 场景四：学习与留学

> 触发词：雅思、托福、GRE、选校、申请、读书笔记

| Skill | 用途 | 层 |
|:--|:--|:--|
| **pdf** / **pdf-to-markdown** | 读教材、啃文献 | 用户 |
| **docx** | 申请材料、文书 | 用户 |
| **xlsx** | 备考计划、选校表 | 用户 |

---

## 💻 场景五：写代码与建工具

> 触发词：写程序、建服务、做应用、造 skill

| Skill | 用途 | 层 |
|:--|:--|:--|
| **skill-creator** | **造新 skill / 改进旧 skill / 测效果** | 用户 |
| mcp-builder | 构建 MCP 服务器 | 用户 |
| claude-api | Claude API / SDK 参考 | 用户 |
| webapp-testing | Playwright 网页测试 | 用户 |
| web-artifacts-builder | 多组件 HTML 应用 | 用户 |
| frontend-design | 前端设计指导 | 用户 |
| 🔧 **agent-orchestrator** | 多 agent 编排（**待建，方向未定**） | 自建 |

---

## 🎨 场景六：做视觉素材

> 触发词：海报、封面、配图、GIF

| Skill | 用途 | 层 |
|:--|:--|:--|
| canvas-design | PNG/PDF 视觉作品 | 用户 |
| algorithmic-art | p5.js 生成艺术 | 用户 |
| theme-factory | 主题配色 | 用户 |
| brand-guidelines | Anthropic 品牌规范 | 用户 |
| slack-gif-creator | Slack GIF | 用户 |

---

## ⚙️ 场景七：杂项

| Skill | 用途 | 层 |
|:--|:--|:--|
| **vision-skill** | 多模态描述 + OCR 兜底 | vault |
| internal-comms | 内部沟通文书 | 用户 |
| tianzhi-core | 东方术数计算 | vault |

---

# 🚀 Workflow 适用性速查（重要）

> **Workflow = 已知怎么拆的批量执行器**，不是边想边做的工作台。

| 你的任务 | 适不适合 | 为什么 |
|:--|:--:|:--|
| **批量读 50 篇文献**，每篇出摘要 | ✅ **完美** | 50 个同质单元，并行 |
| **核对 100 条参考文献**真假 | ✅ **完美** | 每条独立 |
| **20 个策略分别回测**再汇总 | ✅ 适合 | 单元同质 |
| **整库体检**（找断链、冗余） | ✅ 适合 | 可并行切块 |
| 论文实验（串行探索） | ❌ | 每步依赖上步结果 |
| 写主持串词（要你拍板） | ❌ | 中途需要人 |
| 每日扫描 | ❌ | 已自动化，不需要 |

**判断口诀**：

```
「一批一样的东西」→ 用 Workflow
「一步步想出来」  → 不用，直接做
```

---

# 📋 一页速查（我要干什么 → 打开哪个场景）

| 我要…… | 场景 |
|:--|:--|
| 写/改论文、配图、读文献 | 🎓 一 |
| 看行情、跑回测、读研报 | 📈 二 |
| 做策划、写主持、搞活动 | 🎤 三 |
| 备考、申请、读书 | 📚 四 |
| 写代码、造 skill | 💻 五 |
| 做海报、封面 | 🎨 六 |
| 看图、OCR | ⚙️ 七 |

---

## ⚠️ 两条硬性备注

**① 有公式的文档不能走 python-docx** —— 必须用 pandoc + reference.docx，否则 LaTeX 全变裸文本。

**② 中文期刊配图，字体有坑** —— Songti SC 缺 U+2212 字形，标签里手写负号要用 ASCII `-`。

# Skill 调度表 · 按任务类型分类

> 整理日期：2026-09-29
> 用途：**给定任务 → 快速定位该用哪个 skill**
> 共 **28 个**（用户级 21 + vault 级 6 + 自建 1）

---

## 图例

| 标记 | 含义 |
|:--:|:--|
| 🟢 | 高频，日常真的在用 |
| 🟡 | 偶尔用 |
| ⚪ | 装了但基本不用（或为他人准备） |
| 🔧 | 待建 |

---

## 一、📄 文档产出

> **什么时候用**：需要生成/编辑 Office 文件、PDF

| Skill | 层 | 用途 | 频率 |
|:--|:--|:--|:--:|
| **docx** | 用户 | Word 创建/编辑（含修订、批注、替换图片） | 🟢 |
| **xlsx** | 用户 | Excel 读写分析 | 🟢 |
| **pdf** | 用户 | PDF 读取/提取/合并 | 🟢 |
| **pptx** | 用户 | PPT 创建/编辑 | 🟡 |
| **pdf-to-markdown** | 用户 | PDF → Markdown（读长文献） | 🟡 |
| office-word | 用户 | Word 的另一套实现 | ⚪ |
| office-excel | 用户 | Excel 的另一套实现 | ⚪ |
| office-powerpoint | 用户 | PPT 的另一套实现 | ⚪ |

> 💡 `docx/xlsx/pptx/pdf` 与 `office-*` 功能重叠，**优先用前者**。

---

## 二、🎓 学术科研

> **什么时候用**：写论文、答辩、文献、实验、配图

| Skill | 层 | 用途 | 频率 |
|:--|:--|:--|:--:|
| **scipilot-figure-skill** | vault | **科研配图顾问**（选图型→期刊规格→自检闭环） | 🟢 |
| **research-writing-skill** | vault | **中文论文写作/修改/润色/审稿回复** | 🟢 |
| office-academic-skill | vault | 中文学术 Word/PPT（论文读书报告、组会） | 🟡 |
| scientific-toolkit-skill | vault | 光电信息科研计算（MATLAB/Octave） | ⚪ |
| doc-coauthoring | 用户 | 结构化协作写文档 | 🟡 |

---

## 三、📈 量化投资

> **什么时候用**：行情数据、回测、策略扫描

| Skill                | 层     | 用途                        | 频率  |
| :------------------- | :---- | :------------------------ | :-: |
| **cn-stock-data** | 自建 | **A股免费数据源 + 反爬 + 增量缓存**（[skills/cn-stock-data](skills/cn-stock-data)） | 🟢 |
| vision-skill         | vault | 看图/OCR（读图表、截图、研报）         | 🟡  |

> ⚠️ 量化的核心逻辑（十二策略、OAMV 切换）**不在 skill 里**，在 `.claude/fxl_research/` 的私有脚本中。

---

## 四、💻 代码与工程

> **什么时候用**：写程序、做应用、建服务

| Skill | 层 | 用途 | 频率 |
|:--|:--|:--|:--:|
| mcp-builder | 用户 | 构建 MCP 服务器 | ⚪ |
| claude-api | 用户 | Claude API / SDK 参考 | ⚪ |
| webapp-testing | 用户 | Playwright 网页自动化测试 | ⚪ |
| web-artifacts-builder | 用户 | 多组件 HTML 应用 | ⚪ |
| frontend-design | 用户 | 前端设计指导 | ⚪ |

**配套插件**（用 `/plugin` 装）：`code-review` `code-simplifier` `feature-dev` `pr-review-toolkit` `hookify` `security-guidance`，以及各类 `*-lsp` 语言服务。

---

## 五、🎨 视觉与创意

> **什么时候用**：做海报、封面、视觉素材

| Skill | 层 | 用途 | 频率 |
|:--|:--|:--|:--:|
| canvas-design | 用户 | 出 PNG/PDF 视觉作品 | 🟡 |
| algorithmic-art | 用户 | p5.js 生成艺术 | ⚪ |
| theme-factory | 用户 | 主题配色 | ⚪ |
| brand-guidelines | 用户 | Anthropic 品牌规范 | ⚪ |
| slack-gif-creator | 用户 | Slack GIF | ⚪ |

---

## 六、🧩 元技能（关于技能本身）

| Skill | 层 | 用途 | 频率 |
|:--|:--|:--|:--:|
| **skill-creator** | 用户 | **创建/改进 skill，并测量效果** | 🟢 |
| 🔧 **agent-orchestrator** | 自建 | **多 agent 编排（Leader 制）**（待建） | — |

### 自定义命令（`.claude/commands/`）

| 命令 | 用途 | 频率 |
|:--|:--|:--:|
| **`/圆桌会议 <议题>`** | **召集 5 视角 + 知识库之灵对抗式评审，收敛出可落盘结论（允许留分歧）** | 🟢 |

> 📌 出处：2026-09-05「老张3.3 六大升级建议」先例，2026-09-30 成文。
> ⚠️ 是 🔧 `agent-orchestrator` 的**轻量版**——单 agent 分饰多角，不起并发子 agent。
> 需要真正并发（多 agent 各自独立检索、互不可见）时，才升级到 `agent-orchestrator`。

---

## 七、⚙️ 其他

| Skill | 层 | 用途 | 频率 |
|:--|:--|:--|:--:|
| vision-skill | vault | 多厂商多模态描述 + OCR 兜底 | 🟡 |
| internal-comms | 用户 | 内部沟通文书 | ⚪ |
| tianzhi-core | vault | 东方术数计算底座 | ⚪ |

---

## 📋 快速调度表（按「我要干什么」查）

| 我要…… | 用这个 |
|:--|:--|
| 写/改论文正文 | `research-writing-skill` |
| 给论文配图 | `scipilot-figure-skill` |
| 出 Word 版论文 | `docx`（**有公式必须走 pandoc**，见备注） |
| 读一篇 PDF 文献 | `pdf` / `pdf-to-markdown` |
| 处理数据表 | `xlsx` |
| 做答辩 PPT | `pptx` / `office-academic-skill` |
| 看图表/截图内容 | `vision-skill` |
| 抓 A股行情 | `cn-stock-data`（`skills/cn-stock-data`：日线/清单/财务/行业 + 反爬缓存） |
| 造一个新 skill | `skill-creator` |
| **对一件事做多视角评审** | **`/圆桌会议 <议题>`** |
| 拆多 agent 干活 | 🔧 `agent-orchestrator`（待建） |
| 做海报/封面 | `canvas-design` |
| 写代码/建服务 | `mcp-builder` / `claude-api` |

---

## ⚠️ 两条必须记住的备注

**① 有公式的文档，不能走 python-docx。**
`docx` skill 用 python-docx，**不转 LaTeX** → 公式会全变裸文本。有公式必须用 **pandoc + reference.docx**（构建脚本见 `fxl_research/build_paper_docx.sh`）。

**② 中文期刊配图，字体有个坑。**
Songti SC **没有 U+2212 减号字形**，标签里手打真减号会被吞掉。轴刻度不用管（`axes.unicode_minus=False` 已处理），但**自己写的标签必须用 ASCII `-`**。

---

## 分类逻辑说明

为什么这么分？

1. **按产出物分，不按工具分** —— 用户想的是「我要一份 Word」，不是「我要用 docx skill」
2. **量化单独一类** —— 它是这个 vault 的主战场，且和其他类差异最大
3. **元技能单列** —— `skill-creator` 和 `agent-orchestrator` 是「造工具的」，不是「干活的」
4. **多层同名的不删** —— vault 级和用户级可能同名，保留以便按场景选

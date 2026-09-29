# Skill Collection

我的 Claude Code skill 合集 —— 分类整理，按任务调度。

## 结构

```
skill-collection/
├── CATALOG.md      技能调度表（按任务类型分类，含「我要干什么→用哪个」速查）
├── docs/           设计文档与构想
├── agents/         自定义 agent 定义
├── workflows/      编排流程
└── skills/         自建 skill
```

## 快速开始

见 [CATALOG.md](CATALOG.md)。

## 两条硬性备注

1. **有公式的文档不能走 python-docx** —— 必须用 pandoc + reference.docx，否则 LaTeX 变裸文本
2. **中文期刊配图** —— Songti SC 缺 U+2212 字形，标签里负号要用 ASCII `-`

## 许可

MIT

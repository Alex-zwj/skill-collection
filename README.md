# Skill Collection

我的 Claude Code **skill 合集** —— 分类整理，按任务调度。

## 已收录

| Skill | 说明 |
|---|---|
| [cn-stock-data](skills/cn-stock-data) | **A 股免费数据源 + 反爬 + 增量缓存**（日线/清单/财务/行业；新浪 & 东财·AKShare） |

## 结构

```
skill-collection/
├── CATALOG.md      技能调度表（按任务类型分类，含「我要干什么→用哪个」速查）
├── agents/         自定义 agent 定义
├── workflows/      编排流程
└── skills/         自建 skill
    └── cn-stock-data/
```

## 安装某个 skill

把对应目录复制到你的 vault 的 `.claude/skills/` 下（需含 `SKILL.md`），重启 Claude Code 会话即可被识别：

```bash
cp -R skills/cn-stock-data  <你的vault>/.claude/skills/
```

## 两条硬性备注

1. **有公式的文档不能走 python-docx** —— 必须用 pandoc + reference.docx，否则 LaTeX 变裸文本
2. **中文期刊配图** —— Songti SC 缺 U+2212 字形，标签里负号要用 ASCII `-`

## 许可

MIT

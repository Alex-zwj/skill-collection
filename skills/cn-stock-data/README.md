# cn-stock-data

> A 股**免费数据源**工具箱（Claude Code Skill）：抓取 + 反爬 + 缓存，供量化研究/回测直接调用。

## 特性
- **只用公开免费源**：新浪（日线/指数/行业F10）、东方财富·AKShare（业绩报表/财务指标）
- **反爬友好**：UA/Referer、线程 ≤8、请求抖动、456 指数退避、最多重试
- **可断点续传**：每股一 JSON，按"参考交易日"跳过已最新
- **离线可用**：分析脚本统一读缓存，不在线边跑边拉（可复现）
- **口径提醒内置**：未复权数据 + `|r|>10.5%` 缺口识别

## 安装
```bash
pip install -r requirements.txt
```
> 作为 Claude Code skill 使用时，把本目录放到 `.claude/skills/cn-stock-data/`（含 `SKILL.md`），重启会话即可被识别。

## 快速开始
```bash
python3 scripts/universe.py  --out universe.csv --market main
python3 scripts/kline_sina.py --list universe.csv --dir kline_cache --datalen 300 --workers 6 --fresh-only
python3 scripts/fundamentals_akshare.py --years 2022 2023 2024 --outdir fundamentals
python3 scripts/fundamentals_akshare.py --finance --list universe.csv --start-year 2019
python3 scripts/industry_sina.py --list universe.csv
python3 examples/quickstart.py
```

## 结构
```
cn-stock-data/
├── SKILL.md                     # Claude skill 定义（触发词/用法）
├── README.md
├── requirements.txt
├── scripts/
│   ├── cache.py                 # 缓存读写/新鲜度/增量/缺口
│   ├── kline_sina.py            # 日线抓取（增量+反爬）
│   ├── universe.py              # 股票清单
│   ├── fundamentals_akshare.py  # 业绩报表 + 财务指标
│   └── industry_sina.py         # 行业/概念（缓存）
├── references/
│   ├── 数据源清单.md
│   ├── 反爬与限速策略.md
│   └── 缓存规范.md
└── examples/quickstart.py
```

## 合规与免责
- 仅抓取**公开**页面与接口；请遵守目标站点条款与 robots，控制请求频率，勿高频抓取。
- 数据来自第三方公开源，**不保证准确/及时**，仅供研究，不构成投资建议。
- 请勿二次分发原始数据或用于商业用途；版权归原数据提供方所有。

## License
MIT

---
name: cn-stock-data
description: A股免费数据获取工具箱（中文优先）——新浪K线、东方财富/AKShare 财务与业绩、上证指数、股票清单、行业/概念，内置反爬退避、线程限速、断点续传与增量缓存。用于：抓A股行情/日线/K线、股票列表、财务指标、业绩报表、行业板块、指数数据、离线缓存管理、数据缺口排查。Use when the user asks for China A-share market data, stock prices, K-line/OHLCV, financials, fundamentals, industry sectors, index data, crawling public finance APIs, rate-limit/anti-crawl handling, or building/incrementally updating a local market-data cache.
---

# cn-stock-data · A股免费数据工具箱

> 目标：**只用公开免费数据源**（新浪 / 东方财富(AKShare)），**可断点续传、反爬友好、结果落本地缓存**，供回测/研究直接调用。

## 何时使用
- 需要 A 股**日线/K线**（开高低收量）
- 需要**股票清单**（沪深主板/全市场）或**上证指数**
- 需要**基本面**：业绩报表（每股收益/营收/净利…）、财务分析指标（偿债/营运/成长比率）
- 需要**行业/概念**归属
- 需要**离线缓存 + 增量更新**（只补落后的，跳过已最新的）

## 目录
| 路径 | 作用 |
|---|---|
| `scripts/kline_sina.py` | 新浪日线抓取（反爬退避、多线程限速、增量、缺口过滤） |
| `scripts/cache.py` | 缓存读写/新鲜度/增量合并（被其它脚本复用） |
| `scripts/universe.py` | 股票清单（本地 csv 或 AKShare 全市场） |
| `scripts/fundamentals_akshare.py` | 业绩报表 yjbb + 财务分析指标（按年，断点续传） |
| `scripts/industry_sina.py` | 行业/概念（新浪 F10，带缓存） |
| `references/` | 数据源清单、反爬与限速策略、缓存规范 |
| `examples/quickstart.py` | 端到端示例 |

## 快速开始
```bash
pip install -r requirements.txt
# 1) 股票清单
python3 scripts/universe.py --out universe.csv --market main
# 2) 增量抓日线（默认写入 ./kline_cache/）
python3 scripts/kline_sina.py --list universe.csv --dir kline_cache --datalen 300 --workers 8
# 3) 基本面（业绩报表 + 财务指标，按年）
python3 scripts/fundamentals_akshare.py --years 2022 2023 2024 --outdir fundamentals
# 4) 行业
python3 scripts/industry_sina.py --code 600519
```

## 铁律（引 references 详情）
1. **限速**：线程 ≤ 8；每次请求间 `sleep(0.05~0.3)` 抖动；遇 HTTP **456/频率限制 → 指数退避**；**不要**全市场高频循环。
2. **必带** `User-Agent` 与 `Referer`；`Referer=https://finance.sina.com.cn`。
3. **缓存优先**：请求前查本地最新日期，已最新则跳过（断点续传）。
4. **未复权数据**：新浪日线为未复权价。研究时需以**单日涨跌幅 |r|>10.5%** 识别除权/数据缺口并在排序/收益中剔除（详见 `references/缓存规范.md`）。
5. **合规**：仅抓公开页面/接口，遵守目标站点条款与 robots；不规避付费墙、不二次分发原始数据。

## 常见坑
- 新浪 `datalen` 过大可能返回异常 → 分页/分段抓取（见 kline_sina 的 fallback）。
- 456 状态=频率限制，务必退避再试，硬刚会被长时间封。
- AKShare 财务接口按 `start_year` 取多年，**同一只股票一次可拿多年**，比逐年更省请求。
- 缓存文件建议**每股一 json**（便于增量/续传），可用 `cache.py` 的 `last_date()` 做新鲜度判断。

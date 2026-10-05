#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""quickstart.py — 端到端示例：清单 → 增量日线缓存 → 读取成 DataFrame

运行：
  python3 quickstart.py            # 抓一小撮样本（避免触发限速）
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
import cache, kline_sina

SAMPLES = ["600519", "000001", "600036", "000333", "601318"]  # 贵州茅台/平安银行/招商银行/美的/中国平安
CACHE_DIR = "demo_kline_cache"


def main():
    ref = kline_sina.ref_latest_trade_date()
    print("参考交易日:", ref)
    for c in SAMPLES:
        bars = kline_sina.fetch(c, datalen=120)
        if not bars:
            print(f"  {c} 抓取失败"); continue
        n = cache.merge_incremental(CACHE_DIR, c, bars, keep=300)
        df = cache.to_dataframe(cache.load(CACHE_DIR, c))
        gap = cache.has_gap(cache.load(CACHE_DIR, c), 60)
        print(f"  {c}: 新增{n}根 共{len(df)}根 最新={df['day'].iloc[-1]} "
              f"收盘={df['close'].iloc[-1]:.2f} 近60日含缺口={gap}")


if __name__ == "__main__":
    main()

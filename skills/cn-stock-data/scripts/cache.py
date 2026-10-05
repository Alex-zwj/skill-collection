#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""cache.py — 每股一 JSON 的 K 线缓存（读写 / 新鲜度 / 增量合并 / 缺口过滤）

约定：缓存文件 <dir>/<code6>.json，内容为新浪返回的 bar 列表
     [{day, open, high, low, close, volume}, ...]（未复权，按日期升序）
"""
import os, json

BAD_THRESH = 0.105  # 单日涨跌幅 >10.5% 判定为除权/数据缺口（主板 ±10%）


def code6(code):
    return str(code).zfill(6)


def path(cache_dir, code):
    return os.path.join(cache_dir, f"{code6(code)}.json")


def load(cache_dir, code):
    try:
        with open(path(cache_dir, code), encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return None


def save(cache_dir, code, bars):
    os.makedirs(cache_dir, exist_ok=True)
    with open(path(cache_dir, code), "w", encoding="utf-8") as f:
        json.dump(bars, f, ensure_ascii=False)


def last_date(cache_dir, code):
    b = load(cache_dir, code)
    return b[-1]["day"] if b else None


def merge_incremental(cache_dir, code, new_bars, keep=300):
    """把新 bar 合并进缓存（去重、排序、截断）。返回新增条数。"""
    old = load(cache_dir, code) or []
    seen = {d["day"] for d in old}
    added = [d for d in new_bars if d["day"] not in seen]
    if not added:
        return 0
    merged = sorted(old + added, key=lambda x: x["day"])[-keep:]
    save(cache_dir, code, merged)
    return len(added)


def has_gap(bars, lookback=60):
    """最近 lookback 根内是否存在除权/缺口（用于动量类研究剔除）。"""
    for i in range(1, min(len(bars), lookback + 1)):
        pc = float(bars[-i - 1]["close"])
        c = float(bars[-i]["close"])
        if pc > 0 and abs(c / pc - 1) > BAD_THRESH:
            return True
    return False


def to_dataframe(bars):
    import pandas as pd
    df = pd.DataFrame(bars)
    for c in ("open", "high", "low", "close"):
        df[c] = df[c].astype(float)
    df["volume"] = df["volume"].astype(float)
    return df

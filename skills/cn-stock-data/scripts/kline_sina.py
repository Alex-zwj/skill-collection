#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""kline_sina.py — 新浪日线抓取（增量 + 反爬退避 + 线程限速）

用法：
  python3 kline_sina.py --code 600519                    # 单只
  python3 kline_sina.py --list universe.csv --dir kline_cache --workers 6
  可选：--datalen 1500 --sleep 0.1 --fresh-only
说明：
  - 默认增量：先看缓存里最新日期，若 == 参考交易日则跳过（断点续传）
  - HTTP 456 / 频率限制 → 指数退避；请求间 sleep(jitter) 限速
  - 未复权数据！研究用请配合 cache.has_gap() 剔除除权缺口
"""
import os, sys, csv, json, time, random, argparse
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cache

URL = "https://quotes.sina.cn/cn/api/json_v2.php/CN_MarketData.getKLineData"
HEADERS = {"User-Agent": "Mozilla/5.0", "Referer": "https://finance.sina.com.cn"}


def sym(code6):
    return f"sh{code6}" if code6[0] == "6" else f"sz{code6}"


def ref_latest_trade_date():
    """用上证指数取参考交易日（index: sh000001）。"""
    try:
        r = requests.get(URL, params={"symbol": "sh000001", "scale": "240",
                                      "ma": "no", "datalen": "5"}, headers=HEADERS, timeout=8)
        d = json.loads(r.text)
        return d[-1]["day"] if isinstance(d, list) and d else None
    except Exception:
        return None


def fetch(code6, datalen=300, retry=5, sleep=0.1):
    for a in range(retry):
        try:
            r = requests.get(URL, params={"symbol": sym(code6), "scale": "240",
                                          "ma": "no", "datalen": str(datalen)},
                             headers=HEADERS, timeout=15)
            if r.status_code == 456:                      # 频率限制
                time.sleep(20 + a * 15); continue
            if r.status_code == 200 and len(r.text) > 50:
                d = json.loads(r.text)
                if isinstance(d, list) and len(d) >= 3:
                    return d
            time.sleep(0.3)
        except Exception:
            time.sleep(1.5 + a * 2)
        finally:
            time.sleep(sleep * (0.5 + random.random()))
    return None


def load_codes(args):
    if args.code:
        return [cache.code6(args.code)]
    codes = []
    with open(args.list, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            codes.append(cache.code6(row.get("code") or row.get("股票代码")))
    return [c for c in codes if c]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--code", help="单只股票代码")
    ap.add_argument("--list", help="csv 列表（需含 code 或 股票代码 列）")
    ap.add_argument("--dir", default="kline_cache", help="缓存目录")
    ap.add_argument("--datalen", type=int, default=300)
    ap.add_argument("--workers", type=int, default=6)
    ap.add_argument("--sleep", type=float, default=0.1)
    ap.add_argument("--fresh-only", action="store_true", help="只补落后的，跳过已最新")
    args = ap.parse_args()

    codes = load_codes(args)
    ref = ref_latest_trade_date()
    print(f"[cn-stock-data] 目标 {len(codes)} 只 | 参考交易日 {ref} | 缓存 {args.dir}")

    todo = []
    for c in codes:
        if args.fresh_only and ref and cache.last_date(args.dir, c) == ref:
            continue
        todo.append(c)
    print(f"  需更新 {len(todo)} 只（其余已最新）")

    done = add = fail = 0
    t0 = time.time()
    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        futs = {ex.submit(fetch, c, args.datalen, 5, args.sleep): c for c in todo}
        for f in as_completed(futs):
            c = futs[f]; bars = f.result()
            if bars:
                n = cache.merge_incremental(args.dir, c, bars)
                add += n; done += 1
            else:
                fail += 1
            if (done + fail) % 200 == 0 and (done + fail):
                print(f"  {done+fail}/{len(todo)} | 新增{add} | {time.time()-t0:.0f}s")
    print(f"完成：成功{done} 失败{fail} 新增{add}条 用时{time.time()-t0:.0f}s")


if __name__ == "__main__":
    main()

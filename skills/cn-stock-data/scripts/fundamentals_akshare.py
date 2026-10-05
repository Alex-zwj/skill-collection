#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""fundamentals_akshare.py — 业绩报表 + 财务分析指标（断点续传）

用法：
  python3 fundamentals_akshare.py --years 2022 2023 2024 --outdir fundamentals
  python3 fundamentals_akshare.py --finance --list universe.csv --start-year 2019 --sleep 1.0
说明：
  - 业绩报表：一次调用取全市场某年年报（stock_yjbb_em(date="YYYY1231")）
  - 财务指标：逐股调用（stock_financial_analysis_indicator，start_year 可一次取多年）
  - 断点续传：已存在的文件跳过；频率限制自动退避
"""
import os, json, time, argparse
import pandas as pd


def fetch_yjbb(years, outdir):
    import akshare as ak
    os.makedirs(outdir, exist_ok=True)
    for y in years:
        out = os.path.join(outdir, f"yjbb_{y}_all.csv")
        if os.path.exists(out):
            print(f"  skip {out}"); continue
        for a in range(4):
            try:
                df = ak.stock_yjbb_em(date=f"{y}1231")
                df.to_csv(out, index=False)
                print(f"  yjbb {y}: {len(df)} 行 -> {out}"); break
            except Exception as e:
                time.sleep(10 + a * 10)
        time.sleep(1)


def fetch_fin_ind(code6, start_year, outdir, sleep=1.0):
    import akshare as ak
    os.makedirs(outdir, exist_ok=True)
    out = os.path.join(outdir, f"{code6}.json")
    if os.path.exists(out):
        return "skip"
    for a in range(4):
        try:
            df = ak.stock_financial_analysis_indicator(symbol=code6, start_year=str(start_year))
            if df is None or len(df) == 0:
                return "empty"
            dc = df.columns[0]
            df[dc] = pd.to_datetime(df[dc])
            rec = {str(r[dc].year): {k: (None if pd.isna(v) else (v if isinstance(v, (int, float, str)) else str(v)))
                                     for k, v in r.items() if k != dc}
                   for _, r in df.iterrows() if r[dc].month == 12}
            with open(out, "w", encoding="utf-8") as f:
                json.dump(rec, f, ensure_ascii=False)
            time.sleep(sleep * (0.6 + 0.8 * (time.time() % 1)))
            return "ok"
        except Exception as e:
            msg = str(e)[:60]
            if any(k in msg for k in ("频率", "限制", "频繁", "456")):
                time.sleep(15 + a * 12)
            else:
                time.sleep(2 + a * 3)
    return "fail"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--years", nargs="*", type=int, default=[], help="年报表年份（如 2022 2023 2024）")
    ap.add_argument("--outdir", default="fundamentals")
    ap.add_argument("--finance", action="store_true", help="抓逐股财务指标")
    ap.add_argument("--list", help="股票 csv（含 code）")
    ap.add_argument("--start-year", type=int, default=2019)
    ap.add_argument("--sleep", type=float, default=1.0)
    args = ap.parse_args()

    if args.years:
        fetch_yjbb(args.years, args.outdir)

    if args.finance and args.list:
        codes = [str(c).zfill(6) for c in pd.read_csv(args.list)["code"]]
        outdir = os.path.join(args.outdir, "fin_ind")
        stat = {"ok": 0, "skip": 0, "empty": 0, "fail": 0}
        for i, c in enumerate(codes, 1):
            r = fetch_fin_ind(c, args.start_year, outdir, args.sleep)
            stat[r] = stat.get(r, 0) + 1
            if i % 50 == 0:
                print(f"  {i}/{len(codes)} {stat}")
        print("完成", stat)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""universe.py — 股票清单

用法：
  python3 universe.py --out universe.csv --market main     # 沪深主板（60/00 开头）
  python3 universe.py --out all.csv --market all           # 全市场（需 AKShare）
  python3 universe.py --from-csv main_board_stocks.csv     # 直接用现成清单
"""
import argparse, csv
import pandas as pd


def via_akshare(market="all"):
    import akshare as ak
    df = ak.stock_info_a_code_name()          # code, name
    df["code"] = df["code"].astype(str).str.zfill(6)
    if market == "main":
        df = df[df["code"].str.startswith(("60", "00", "001", "002", "003"))]
    return df[["code", "name"]]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="universe.csv")
    ap.add_argument("--market", choices=["main", "all"], default="main")
    ap.add_argument("--from-csv", help="已有清单（含 code[,name]）")
    args = ap.parse_args()

    if args.from_csv:
        df = pd.read_csv(args.from_csv)
        col = "code" if "code" in df.columns else df.columns[0]
        out = pd.DataFrame({"code": df[col].astype(int).astype(str).str.zfill(6)})
    else:
        out = via_akshare(args.market)

    out.to_csv(args.out, index=False)
    print(f"[cn-stock-data] 写出 {len(out)} 只 -> {args.out}")


if __name__ == "__main__":
    main()

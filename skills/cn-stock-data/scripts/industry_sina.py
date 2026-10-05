#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""industry_sina.py — 行业/概念（新浪 F10，带本地缓存）

用法：
  python3 industry_sina.py --code 600519
  python3 industry_sina.py --list universe.csv --cache industry_cache.json --sleep 0.5
"""
import os, re, json, csv, time, argparse
import requests

HEADERS = {"User-Agent": "Mozilla/5.0"}
URL = "http://vip.stock.finance.sina.com.cn/corp/go.php/vCI_CorpOtherInfo/stockid/{code}/menu_num/2.phtml"


def load_cache(p):
    try:
        return json.load(open(p, encoding="utf-8"))
    except Exception:
        return {}


def save_cache(p, d):
    with open(p, "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=1)


def query(code6, cache, sleep=0.5):
    if code6 in cache:
        return cache[code6]
    try:
        r = requests.get(URL.format(code=code6), headers=HEADERS, timeout=8)
        r.encoding = "gbk"
        tds = re.findall(r"<td[^>]*>(.*?)</td>", r.text, re.DOTALL)
        texts = [re.sub(r"<[^>]+>", "", t).strip() for t in tds]
        ind, concepts = "未知", []
        for i, t in enumerate(texts):
            if "所属行业板块" in t and i + 1 < len(texts):
                ind = texts[i + 1]
            if "所属概念板块" in t:
                concepts = [x for x in texts[i + 1:i + 8] if x][:3]
        rec = {"industry": ind, "concepts": concepts}
        cache[code6] = rec
        time.sleep(sleep)
        return rec
    except Exception:
        return {"industry": "未知", "concepts": []}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--code")
    ap.add_argument("--list")
    ap.add_argument("--cache", default="industry_cache.json")
    ap.add_argument("--sleep", type=float, default=0.5)
    args = ap.parse_args()

    cache = load_cache(args.cache)
    if args.code:
        print(query(str(args.code).zfill(6), cache, args.sleep))
    elif args.list:
        codes = [str(r["code"]).zfill(6) for r in csv.DictReader(open(args.list, encoding="utf-8"))]
        for i, c in enumerate(codes, 1):
            query(c, cache, args.sleep)
            if i % 50 == 0:
                save_cache(args.cache, cache); print(f"  {i}/{len(codes)}")
    save_cache(args.cache, cache)
    print(f"[cn-stock-data] 行业缓存 {len(cache)} 条 -> {args.cache}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) 2026 Tomoo Ito
# Licensed under the MIT License. See the LICENSE file in the project root.

"""
東京大学 空間情報科学研究センター(CSIS) Simple Geocode APIを使用して住所から緯度経度を取得するサンプルコード
リスト形式、エラー対策なし
"""

import requests
import xmltodict

# ジオコーディングしたい住所等を指定
place = "南区役所"

# 東京大学 空間情報科学研究センター Simple Geocode APIのエンドポイントURL
BASE_URL = "https://geocode.csis.u-tokyo.ac.jp/cgi-bin/simple_geocode.cgi"

# パラメータ設定
params = {"addr": place}

# APIリクエストを送信してレスポンスを取得
response = requests.get(BASE_URL, params=params, timeout=5)

# XMLを辞書形式に変換（複数候補の場合はリストになる）
dict_data = xmltodict.parse(response.text)

# 候補を取得（辞書 or リスト）
results = dict_data["results"]["candidate"]

# 辞書のままの場合はリストに変換
if isinstance(results, dict):
    results_list = [results]
else:
    results_list = results

print()
# 全候補を表示
for idx, cand in enumerate(results_list, start=1):
    result_address = cand.get("address", "")
    lat = cand.get("latitude")
    lon = cand.get("longitude")
    iLvl = cand.get("iLvl")

    print(f"--- 候補 {idx} ---")
    print(f"住所: {result_address}")
    print(f"緯度: {lat}")
    print(f"経度: {lon}")
    print(f"精度レベル(iLvl): {iLvl}")
    print()

# 信頼度は results 直下にある
iConf = dict_data["results"].get("iConf")
print(f"信頼度(iConf): {iConf}")
print()

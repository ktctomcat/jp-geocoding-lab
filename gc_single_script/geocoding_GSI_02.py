#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) 2026 Tomoo Ito
# Licensed under the MIT License. See the LICENSE file in the project root.

"""
国土地理院 ジオコーディング APIを使用して住所から緯度経度を取得するサンプルコード
リスト形式、エラー対策なし
"""

import requests

BASE_URL = "https://msearch.gsi.go.jp/address-search/AddressSearch"
address = "北区役所"

# APIリクエストのパラメータを設定
params = {"q": address}

# APIリクエストを送信してレスポンスを取得
response = requests.get(BASE_URL, params=params, timeout=5)

# 結果をJSON形式で取得（GSIは常に配列）
results_list = response.json()

# --- 全候補を表示 ---
for idx, cand in enumerate(results_list, start=1):
    # 緯度経度と住所を取得
    geom = cand.get("geometry", {})
    coords = geom.get("coordinates", [None, None])
    lon = coords[0]
    lat = coords[1]
    props = cand.get("properties", {})
    result_address = props.get("title", "")

    # 結果を表示
    print(f"--- 候補 {idx} ---")
    print(f"緯度: {lat}")
    print(f"経度: {lon}")
    print(f"住所: {result_address}")
    print()

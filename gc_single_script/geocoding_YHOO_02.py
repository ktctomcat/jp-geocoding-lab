#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) 2026 Tomoo Ito
# Licensed under the MIT License. See the LICENSE file in the project root.

"""
Yahoo!ジオコーダAPIを使用して住所から緯度経度を取得するサンプルコード
リスト形式、エラー対策なし
"""

import requests

BASE_URL = "https://map.yahooapis.jp/geocode/V1/geoCoder"
CLIENT_ID = "<あなたのClient ID（アプリケーションID）>"
address = "新潟市"

# APIリクエストのパラメータを設定
params = {
    "appid": CLIENT_ID,
    "output": "json",
    "ei": "UTF-8",
    "al": 4,
    "recursive": "true",
    "query": address,
}

# APIリクエストを送信してレスポンスを取得
response = requests.get(BASE_URL, params=params, timeout=5)

# レスポンスから緯度経度と住所を抽出
results = response.json()

# Featureリストを取得（存在しない場合は空リスト）
response_list = results.get("Feature", [])

# 取得した緯度経度と住所を表示
for idx, cand in enumerate(response_list, start=1):
    # 緯度経度と住所を取得
    geom = cand.get("Geometry", {})
    coords = geom.get("Coordinates", "")

    # 座標が "lng,lat" の文字列である前提
    if isinstance(coords, str) and "," in coords:
        lon, lat = coords.split(",")
    else:
        lon, lat = None, None

    props = cand.get("Property", {})
    result_address = props.get("Address", "")

    # 結果を表示
    print(f"--- 候補 {idx} ---")
    print(f"緯度: {lat}")
    print(f"経度: {lon}")
    print(f"住所: {result_address}")
    print()

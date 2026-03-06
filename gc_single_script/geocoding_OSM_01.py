#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) 2026 Tomoo Ito
# Licensed under the MIT License. See the LICENSE file in the project root.

"""
OpenStreetMap（OSM） Nominatim APIを使用して住所から緯度経度を取得するサンプルコード
JSON形式、エラー対策なし
"""

import requests

# ジオコーディングしたい住所を指定
place = "新潟市西蒲区番屋"

# OSM Nominatim APIのエンドポイントURL
BASE_URL = 'https://nominatim.openstreetmap.org/search'

# APIリクエストのパラメータを設定
params = {
    "q": place,
    'format': 'json',
    'limit': 20  # 最大値は 50件 まで。
}

# User-Agentの設定
headers = {
    'User-Agent': 'JP-Multi-Source-Geocoder-QGIS-Plugin/1.0'
}

# APIリクエストを送信してレスポンスを取得
response = requests.get(BASE_URL, params=params, headers=headers, timeout=5)

# 結果をJSON形式で取得（OSMは常に配列）
results_list = response.json()

# 結果をそのまま表示
print()
print(results_list)

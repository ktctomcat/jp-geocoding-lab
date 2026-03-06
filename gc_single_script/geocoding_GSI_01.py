#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) 2026 Tomoo Ito
# Licensed under the MIT License. See the LICENSE file in the project root.

"""
国土地理院 ジオコーディング APIを使用して住所から緯度経度を取得するサンプルコード
JSON形式、エラー対策なし
"""

import requests

# ジオコーディングしたい住所を指定
place = "江南区役所"

# 国土地理院 ジオコーディング APIのエンドポイントURL
BASE_URL = "https://msearch.gsi.go.jp/address-search/AddressSearch"

# APIリクエストのパラメータを設定
params = {
    "q": place
}

# APIリクエストを送信してレスポンスを取得
response = requests.get(BASE_URL, params=params, timeout=5)

# 結果をJSON形式で取得（GSIは常に配列）
results_list = response.json()

# 結果をそのまま表示
print()
print("JSON形式のレスポンス:")
print()
print(results_list)

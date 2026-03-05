#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) 2026 Tomoo Ito
# Licensed under the MIT License. See the LICENSE file in the project root.

"""
Yahoo!ジオコーダAPIを使用して住所から緯度経度を取得するサンプルコード
JSON形式、エラー対策なし
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

# 取得した緯度経度と住所を表示
print(results)

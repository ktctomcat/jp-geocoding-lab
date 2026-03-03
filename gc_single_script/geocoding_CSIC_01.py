#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) 2026 Tomoo Ito
# Licensed under the MIT License. See the LICENSE file in the project root.

"""
このスクリプトの目的や背景を簡潔に書く。
"""

import requests
import xmltodict

# CSICのジオコーディングAPIを使用して住所から緯度経度を取得するサンプルコード
# XML形式、エラー対策なし
BASE_URL = "https://geocode.csis.u-tokyo.ac.jp/cgi-bin/simple_geocode.cgi"
address = "新潟市西蒲区番屋１７００"

# パラメータ設定
params = {"addr": address}

# APIリクエストを送信してレスポンスを取得
response = requests.get(BASE_URL, params=params, timeout=5)

# XMLをそのまま表示
print()
print("Raw XML Response:")
print()
print(response.text)

pause = input("Press Enter to continue...")

# XMLを辞書形式に変換（1件の場合は辞書型、複数候補の場合はリストになる）
dict_data = xmltodict.parse(response.text)
print()
print("Parsed XML to Dictionary:")
print()
print(dict_data)

pause = input("Press Enter to continue...")

# 候補を取得（辞書 or リスト）
results = dict_data.get("results", {}).get("candidate", [])
print()
print("Extracted Candidate(s):")
print()
print(results)

# 辞書のままの場合はリストに変換
if isinstance(results, dict):
    result_list = [results]
else:
    result_list = results

pause = input("Press Enter to continue...")

# 候補を表示
print()
print("Candidate List:")
print()
print(result_list)
print()

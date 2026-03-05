#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) 2026 Tomoo Ito
# Licensed under the MIT License. See the LICENSE file in the project root.

from typing import Optional

import requests

# 独自モジュール
from .utils import safe_float


class YHOOClient:
    """
    Yahoo!ジオコーダ API クライアント
    requests.get() を使用し、全候補をリストで返す
    User-Agentの設定は必須ではないが、API利用規約に従い設定することを推奨
    Yahoo!ジオコーダ API は JSON を返が、そのトップレベルは 辞書（dict）
    """
    BASE_URL = 'https://map.yahooapis.jp/geocode/V1/geoCoder'
    CLIENT_ID = "<あなたのClient ID（アプリケーションID）>"

    def search(self, query: str) -> Optional[list[dict]]:
        # APIリクエスト
        params = {
            "appid": self.CLIENT_ID,
            "output": "json",
            "ei": "UTF-8",
            "al": 4,
            "recursive": "true",
            "query": query,
        }
        # User-Agentの設定
        headers = {
            'User-Agent': 'JP-Multi-Source-Geocoder-QGIS-Plugin/1.0'
        }
        try:
            response = requests.get(
                self.BASE_URL, params=params, headers=headers, timeout=5)
            response.raise_for_status()
        except Exception:
            return None

        # JSONデコード
        try:
            result = response.json()
        except ValueError:
            return None

        # 候補がない場合は None を返す
        if not result:
            return None

        # "Feature" キーの値を取得し、候補リストを作成
        result_list = result.get("Feature", [])

        # 複数候補をリストにまとめる処理
        candidate_list = []
        for candidate in result_list:
            # "Geometry" キーの値を取得し、さらに "Coordinates" キーの値を取得
            geom = candidate.get("Geometry", {})
            coords = geom.get("Coordinates")
            raw_lon, raw_lat = coords.split(",")
            lon = safe_float(raw_lon)
            lat = safe_float(raw_lat)

            # 住所の取得。Name を使用
            address = candidate.get("Name", "")

            # 候補リストに住所、緯度、経度を追加
            candidate_list.append({
                "address": address,
                "lon": lon,
                "lat": lat,
                "geocode_src": "YHOO_requests"
            })

        return candidate_list

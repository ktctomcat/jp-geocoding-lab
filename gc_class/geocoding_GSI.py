#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) 2026 Tomoo Ito
# Licensed under the MIT License. See the LICENSE file in the project root.

from typing import Optional

import requests


class GSIClient:
    """
    国土地理院 ジオコーディング API クライアント
    requests.get() を使用し、全候補をリストで返す
    """
    BASE_URL = "https://msearch.gsi.go.jp/address-search/AddressSearch"

    def search(self, query: str) -> Optional[list[dict]]:
        # パラメータ設定
        params = {
            "q": query
        }
        try:
            # APIリクエスト
            response = requests.get(self.BASE_URL, params=params, timeout=5)
            response.raise_for_status()
        except requests.RequestException:
            # リクエスト失敗時はNoneを返す
            return None

        # JSONデコード（必ずリストになる）
        try:
            results_list = response.json()
        except ValueError:
            return None

        # 候補がない場合はNoneを返す
        if not results_list:
            return None

        # 候補をリストとして作成してすべて返す
        candidate_list = []
        for candidate in results_list:
            # "geometry" キーの値を取得し、さらに "coordinates" キーの値を取得
            geom = candidate.get("geometry", {})
            coords = geom.get("coordinates", [None, None])
            lon = coords[0]
            lat = coords[1]

            # 住所の取得。properties.title を使用
            props = candidate.get("properties", {})
            address = props.get("title", "")

            # 住所、緯度、経度を候補リストに追加
            candidate_list.append({
                "address": address,
                "lon": lon,
                "lat": lat,
                "geocode_src": "GSI_requests"
            })

        return candidate_list

from typing import Optional

import requests

# 独自モジュール
from .utils import safe_float


class OSMClient:
    """
    OpenStreetMap Nominatim ジオコーディング API クライアント
    requests.get() を使用し、全候補をリストで返す
    """
    BASE_URL = 'https://nominatim.openstreetmap.org/search'

    def search(self, query: str) -> Optional[list[dict]]:
        # パラメータ設定
        params = {
            "q": query,
            'format': 'json',
            'limit': 20  # 最大値は 50件 まで。
        }
        # User-Agentの設定
        headers = {
            'User-Agent': 'JP-Multi-Source-Geocoder-QGIS-Plugin/1.0'
        }

        try:
            # APIリクエスト
            response = requests.get(self.BASE_URL, params=params, headers=headers, timeout=5)
            response.raise_for_status()
        except Exception:
            return None

        try:
            # JSONデコード（必ずリストになる）
            result_list = response.json()
        except ValueError:
            return None

        if not result_list:
            # APIからのレスポンスが空の場合は None を返す
            return None

        # 複数候補をリストにまとめる処理
        candidate_list = []
        for candidate in result_list:
            # "lon" と "lat" キーの値を取得し、数値に変換する
            raw_lon = candidate.get("lon")
            raw_lat = candidate.get("lat")
            lon = safe_float(raw_lon)
            lat = safe_float(raw_lat)

            # 住所の取得。display_name を使用
            address = candidate.get("display_name", "")

            # 住所、緯度、経度を候補リストに追加
            candidate_list.append({
                "address": address,
                "lon": lon,
                "lat": lat,
                "geocode_src": "OSM_requests"
            })

        return candidate_list

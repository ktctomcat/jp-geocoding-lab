
from typing import Optional

import requests
import xmltodict

# 独自モジュール
from .utils import safe_float


class GJPClient:
    """
    Geocoding.jp ジオコーダー API クライアント
    requests.get() を使用し、全候補をリストで返す ※Geocoding.jpは1件しか返さない仕様
    """
    BASE_URL = 'https://www.geocoding.jp/api/'

    def search(self, query: str) -> Optional[list[dict]]:
        # APIリクエスト
        params = {
            "q": query
        }
        try:
            response = requests.get(self.BASE_URL, params=params, timeout=5)
            response.raise_for_status()
        except Exception:
            return None

        # XMLを辞書に変換
        try:
            response = xmltodict.parse(response.text)
        except Exception:
            return None

        # APIの仕様上、候補は1件しか返さないが、将来複数返す可能性も考慮してリストで返す形にする
        results = response.get("result", {})

        # 候補がない場合は None を返す
        if not results:
            return None

        # 基本住所として result 直下のものを取得
        base_address = results.get("google_maps") or results.get("address")

        # 座標ノードを取得
        coords = results.get("coordinate")

        if not coords:
            return None

        # 複数候補か単一候補かを判定
        if isinstance(coords, dict):
            result_list = [coords]
        else:
            result_list = coords

        # 複数候補をリストにまとめる処理
        candidate_list = []
        for candidate in result_list:
            # 座標を取得
            raw_lon = candidate.get("lng") or candidate.get("longitude") or "0"
            raw_lat = candidate.get("lat") or candidate.get("latitude") or "0"
            lon = safe_float(raw_lon)
            lat = safe_float(raw_lat)

            # 住所を取得：候補内に住所があればそれ、なければ共通の住所を使う
            address = candidate.get("google_maps") or candidate.get("address") or base_address

            # 住所、緯度、経度を候補リストに追加
            candidate_list.append({
                "address": address,
                "lon": lon,
                "lat": lat,
                "geocode_src": "GJP_requests"
            })

        return candidate_list

from typing import Optional

import requests
import xmltodict

# 独自モジュール
from .utils import safe_float


class CSISClient:
    """
    東京大学 空間情報科学研究センター Simple Geocode API クライアント
    requests.get() を使用し、全候補をリストで返す
    """
    BASE_URL = 'https://geocode.csis.u-tokyo.ac.jp/cgi-bin/simple_geocode.cgi'

    def search(self, query: str) -> Optional[list[dict]]:
        # APIリクエスト
        params = {
            "addr": query
        }
        try:
            response = requests.get(self.BASE_URL, params=params, timeout=5)
            response.raise_for_status()
        except Exception:
            return None

        # XMLデコード
        try:
            response = xmltodict.parse(response.text)
        except Exception:
            return None

        # "results" キーの値を取得し、さらに "candidate" キーの値を取得
        results = response.get("results", {}).get("candidate", [])
        if not results:
            return None

        # 単一候補（dict）の場合、一貫性のためにリストに変換
        if isinstance(results, dict):
            result_list = [results]
        else:
            result_list = results

        # 複数候補をリストにまとめる処理
        candidate_list = []
        for candidate in result_list:
            # "lon" と "lat" キーの値を取得し、数値に変換する
            raw_lon = candidate.get("longitude")
            raw_lat = candidate.get("latitude")
            lon = safe_float(raw_lon)
            lat = safe_float(raw_lat)

            # 住所の取得。address タグを使用
            addrress = candidate.get("address", "")

            # 住所、緯度、経度を候補リストに追加
            candidate_list.append({
                "address": addrress,
                "lon": lon,
                "lat": lat,
                "geocode_src": "CSIS_requests"
            })

        return candidate_list

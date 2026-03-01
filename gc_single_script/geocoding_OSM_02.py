import requests

# OpenStreetMap（OSM） Nominatim APIを使用して住所から緯度経度を取得するサンプルコード
# リスト形式、エラー対策なし
BASE_URL = 'https://nominatim.openstreetmap.org/search'
address = "北区役所"

# APIリクエストのパラメータを設定
params = {
    "q": address,
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

# --- 全候補を表示 ---
for idx, cand in enumerate(results_list, start=1):
    # 緯度経度と住所を取得
    lon = cand.get("lon")
    lat = cand.get("lat")
    result_address = cand.get("display_name")

    # 結果を表示
    print(f"--- 候補 {idx} ---")
    print(f"緯度: {lat}")
    print(f"経度: {lon}")
    print(f"住所: {result_address}")
    print()

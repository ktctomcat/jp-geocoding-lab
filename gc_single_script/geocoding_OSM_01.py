import requests

# OpenStreetMap（OSM） Nominatim APIを使用して住所から緯度経度を取得するサンプルコード
# JSON形式、エラー対策なし
BASE_URL = 'https://nominatim.openstreetmap.org/search'
address = "新潟市西蒲区番屋"

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

# 結果をそのまま表示
print()
print(results_list)

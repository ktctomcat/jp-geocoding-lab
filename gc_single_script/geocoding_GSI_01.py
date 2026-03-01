import requests

# 国土地理院 ジオコーディング APIを使用して住所から緯度経度を取得するサンプルコード
# JSON形式そ、エラー対策なし
BASE_URL = "https://msearch.gsi.go.jp/address-search/AddressSearch"
address = "江南区役所"

# APIリクエストのパラメータを設定
params = {"q": address}

# APIリクエストを送信してレスポンスを取得
response = requests.get(BASE_URL, params=params, timeout=5)

# 結果をJSON形式で取得（GSIは常に配列）
results_list = response.json()

# 結果をそのまま表示
print()
print("JSON形式のレスポンス:")
print()
print(results_list)

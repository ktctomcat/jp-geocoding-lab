import requests
import xmltodict

# Geocoding.jp ジオコーダー（GJP）APIを使用して住所から緯度経度を取得するサンプルコード
# JSON形式、エラー対策なし
BASE_URL = 'https://www.geocoding.jp/api/'
address = "新潟市西蒲区番屋1700"

# APIリクエストのパラメータを設定
params = {"q": address}

# APIリクエストを送信してレスポンスを取得
response = requests.get(BASE_URL, params=params, timeout=5)

# XMLをそのまま表示
print()
print("XMLそのまま表示:")
print()
print(response.text)
print()

puse = input("Press Enter to continue...")

# XMLを辞書形式に変換（複数候補の場合はリストになる）
dict_data = xmltodict.parse(response.text)
print()
print("辞書型に変換:")
print()
print(dict_data)
print()

pause = input("Press Enter to continue...")

# 結果を取得
results = dict_data.get("result", [])
print()
print("候補抽出:")
print()
print(results)
print()

pause = input("Press Enter to continue...")

# 単数の場合は dict になるのでリストに包む
if isinstance(results, dict):
    results_list = [results]
else:
    results_list = results
print()
print("リスト化:")
print()
print(results_list)
print()

pause = input("Press Enter to continue...")

# 住所と結果をマージして候補ストを作成
candidate_list = []
for cand in results_list:
    coords = cand.get("coordinate", {})
    result_address = cand.get("google_maps", "")

    # google_maps を先頭に入れた辞書を作成
    merged = {"google_maps": result_address, **coords}
    candidate_list.append(merged)

# 候補ストを表示
print()
print("候補リストにマージ:")
print()
print(candidate_list)
print()

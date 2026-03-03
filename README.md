# jp-geocoder-lab

## 概要

日本国内で無料で利用出来るジオコーディングAPIのテスト用スクリプトです。  
色々なサイトでバラバラに紹介されていますが、情報をまとめてみました。

## 準備

外部ライブラリとして、requestsとxmltodictを使用していますので、あらかじめpip等でインストールしてください。

## 使い方

[gc_single_script](https://github.com/ktctomcat/jp-geocoding-lab/tree/main/gc_single_script)中にあるファイルは単体で動くテスト用のスクリプトです。ジオコードしたい住所等を直接スクリプト内で記述し実行させてください。

[gc_class](https://github.com/ktctomcat/jp-geocoding-lab/tree/main/gc_class)の中のファイルは調べたい住所等から緯度・経度と検索結果の住所をリストとして得るためのクラスで、geocoding.pyからインポートして使う仕組みになっています。  
geocoding.pyの中に、ジオコードしたい住所等を記述して実行させると、APIごとの結果の違いを確認することが出来ます。

## 採用 API 一覧

- GIS : 国土地理院ジオコーディング API
- CSIS : 東京大学空間情報科学研究センター シンプル ジオコーディング 実験 API
- GJP : Geocoding.jp API
- OSM : OpenStreetMap Nominatim API
- YHOO : Yhooジオコーダ API

## 【資料】リクエストURL及びレスポンスサンプル

---

### GIS : 国土地理院ジオコーディング API

#### GSI : リクエストURL

```url
https://msearch.gsi.go.jp/address-search/AddressSearch?q=[検索文字列]
```

#### GIS : レスポンスのサンプル（JSON 形式）

```json
[
  {
    "geometry": { "coordinates": [139.140961, 37.800068], "type": "Point" },
    "type": "Feature",
    "properties": {
      "addressCode": "",
      "title": "新潟県新潟市秋葉区新津東町二丁目１１番６号"
    }
  }
]
```

#### GSI : 参考サイト

- [国土地理院コンテンツ利用規約](https://www.gsi.go.jp/kikakuchousei/kikakuchousei40182.html)
- [国土地理院APIで住所から緯度・経度を取得(ジオコーディング) - Elsaの技術日記(徒然なるままに)](https://elsammit-beginnerblg.hatenablog.com/entry/2021/07/11/122916)

---

### CSIS : 東京大学空間情報科学研究センター API

#### CSIS : リクエストURL

```url
https://geocode.csis.u-tokyo.ac.jp/cgi-bin/simple_geocode.cgi?addr=<住所>[オプションパラメータ…]
```

#### CSIS : レスポンスのサンプル（XML 形式）

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<results>
    <query>新潟県新潟市秋葉区新津東町２−１１−６</query>
    <geodetic>wgs1984</geodetic>
    <iConf>5</iConf>
    <converted>新潟県新潟市秋葉区新津東町２−１１−６</converted>
    <candidate>
        <address>新潟県/新潟市/秋葉区/新津東町/二丁目/１１番/６号</address>
        <longitude>139.140961</longitude>
        <latitude>37.800068</latitude>
        <iLvl>8</iLvl>
    </candidate>
</results>
```

#### CSIS : 参考サイト

- [位置参照技術を用いたツールとユーティリティ](https://geocode.csis.u-tokyo.ac.jp/)
- [CSV アドレス マッチング サービス](https://geocode.csis.u-tokyo.ac.jp/home/csv-admatch/)
- [シンプル ジオコーディング 実験](https://geocode.csis.u-tokyo.ac.jp/home/simple-geocoding/)

---

### OSM : OpenStreetMap Nominatim API

#### OSM : リクエストURL

```url
http://nominatim.openstreetmap.org/search?q=調べたい住所&format=json&accept-language=ja&addressdetails=1&limit=取得件数
```

#### OSM : レスポンスサンプル（JSON 形式）

```json
[
  {
    "place_id": 241403170,
    "licence": "Data © OpenStreetMap contributors,ODbL 1.0. http://osm.org/copyright",
    "osm_type": "node",
    "osm_id": 11145437047,
    "lat": "37.7599150",
    "lon": "138.9668220",
    "class": "place",
    "type": "neighbourhood",
    "place_rank": 20,
    "importance": 0.1334006309605554,
    "addresstype": "neighbourhood",
    "name": "番屋",
    "display_name": "番屋, 西蒲区, 新潟市, 新潟県, 959-0511, 日本",
    "boundingbox": ["37.7499150", "37.7699150", "138.9568220", "138.9768220"]
  }
]
```

#### OSM : 参考サイト

- [JA:Nominatim](https://wiki.openstreetmap.org/wiki/JA:Nominatim)

---

### GJP : Geocoding.jp ジオコーダー API

#### GJP : リクエストURL

```url
https://www.geocoding.jp/api/?q=住所やランドマーク名称など
```

#### GJP : レスポンスサンプル（XML 形式）

```xml
成功時
<result>
    <version>1.2</version>
    <address>東京タワー</address>
    <coordinate>
        <lat>35.658581</lat>
        <lng>139.745433</lng>
        <lat_dms>35,39,30.89</lat_dms>
        <lng_dms>139,44,43.558</lng_dms>
    </coordinate>
    <open_location_code>8Q7XMP5W+C5</open_location_code>
    <url>https://www.geocoding.jp/?q=%E6%9D%B1%E4%BA%AC%E3%82%BF%E3%83%AF%E3%83%BC</url>
    <needs_to_verify>no</needs_to_verify>
    <google_maps>東京都港区芝公園４丁目２−８ 東京タワー</google_maps>
</result>

エラー時
<result>
    <address>たわーりんぐいんふぇるの</address>
    <error>001</error>
</result>
```

#### GJP : 参考サイト

[Gecoding.jp](https://www.geocoding.jp/)

---

### YHOO : Yhooジオコーダ API

#### YHOO : リクエストURL

```url
XML
https://map.yahooapis.jp/geocode/V1/geoCoder

JSON
https://map.yahooapis.jp/geocode/V1/geoCoder
```

#### YHOO : レスポンスサンプル（XML 形式）

```xml
<?xml version="1.0" encoding="UTF-8"?>
<YDF totalResultsReturned="1" totalResultsAvailable="1" firstResultPosition="1">
　<ResultInfo>
　　<Count>1</Count>
　　<Total>1</Total>
　　<Start>1</Start>
　　<Status>200</Status>
　　<Description/>
　　<Latency>0.054</Latency>
　</ResultInfo>
　<Feature>
　　<Id>13103.29</Id>
　　<Gid/>
　　<Name>東京都港区六本木</Name>
　　<Geometry>
　　　<Type>point</Type>
　　　<Coordinates>139.73359259,35.66288632</Coordinates>
　　　<BoundingBox>139.70869736,35.62303352 139.78198741,35.68270364</BoundingBox>
　　</Geometry>
　　<Category/>
　　<Description/>
　　<Style/>
　　<Property>
　　　<Uid>f9a30565b66313c33f4540a1424fa89e57ee7209</Uid>
　　　<CassetteId>b22fee69b0dcaf2c2fe2d6a27906dafc</CassetteId>
　　　<Yomi>トウキョウトミナトクロッポンギ</Yomi>
　　　<Country>
　　　　<Code>JP</Code>
　　　　<Name>日本</Name>
　　　</Country>
　　　<Address>東京都港区六本木</Address>
　　　<GovernmentCode>13103</GovernmentCode>
　　　<AddressMatchingLevel>3</AddressMatchingLevel>
　　</Property>
　</Feature>
</YDF>
```

#### YHOO : 参考サイト

[Yahoo!ジオコーダAPI](https://developer.yahoo.co.jp/webapi/map/openlocalplatform/v1/geocoder.html)

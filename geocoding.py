#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) 2026 Tomoo Ito
# Licensed under the MIT License. See the LICENSE file in the project root.

from gc_class import (geocoding_CSIS, geocoding_GJP, geocoding_GSI,
                      geocoding_OSM, geocoding_YHOO)

# ジオコーディングしたい住所等を指定
place = "新潟市西蒲区"

# 東京大学 空間情報科学研究センター クライアントを叩く
gc = geocoding_CSIS.CSISClient()
result_list = gc.search(place)

print()
print("========= 東京大学 空間情報科学研究センター(CSIS) =========")
print()

if not result_list:
    print("候補なし")
else:
    for idx, result in enumerate(result_list, start=1):
        print(f"--- 候補 {idx} ---")
        print(f"住所: {result.get('address')}")
        print(f"緯度: {result.get('lat')}, 経度: {result.get('lon')}")
        print()

# 国土地理院 ジオコーディング クライアントを叩く
gc = geocoding_GSI.GSIClient()
result_list = gc.search(place)

print()
print("========= 国土地理院(GSI) =========")
print()

if not result_list:
    print("候補なし")
else:
    for idx, result in enumerate(result_list, start=1):
        print(f"--- 候補 {idx} ---")
        print(f"住所: {result.get('address')}")
        print(f"緯度: {result.get('lat')}, 経度: {result.get('lon')}")
        print()

# Geocoding.jp ジオコーダー クライアントを叩く
gc = geocoding_GJP.GJPClient()
result_list = gc.search(place)

print()
print("========= Geocoding.jp(GJP) =========")
print()

if not result_list:
    print("候補なし")
else:
    for idx, result in enumerate(result_list, start=1):
        print(f"--- 候補 {idx} ---")
        print(f"住所: {result.get('address')}")
        print(f"緯度: {result.get('lat')}, 経度: {result.get('lon')}")
        print()

# OpenStreetMap Nominatim クライアントを叩く
gc = geocoding_OSM.OSMClient()
result_list = gc.search(place)

print()
print("========= OpenStreetMap Nominatim(OSM) =========")
print()

if not result_list:
    print("候補なし")
else:
    for idx, result in enumerate(result_list, start=1):
        print(f"--- 候補 {idx} ---")
        print(f"住所: {result.get('address')}")
        print(f"緯度: {result.get('lat')}, 経度: {result.get('lon')}")
        print()

# Yahoo!ジオコーダ クライアントを叩く
gc = geocoding_YHOO.YHOOClient()
result_list = gc.search(place)

print()
print("========= Yahoo!ジオコーダ(YHOO) =========")
print()

if not result_list:
    print("候補なし")
else:
    for idx, result in enumerate(result_list, start=1):
        print(f"--- 候補 {idx} ---")
        print(f"住所: {result.get('address')}")
        print(f"緯度: {result.get('lat')}, 経度: {result.get('lon')}")
        print()

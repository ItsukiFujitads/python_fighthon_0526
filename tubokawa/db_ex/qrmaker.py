"""
テキストファイルからURLを読み込み
QRコードを連番で作成するプログラム
"""

import os
import qrcode
import sys

args = sys.argv


# 引数からファイルパスを取得
input_path = args[1]


# QRコードの連番
seq = 0

# URLを保存する配列
url_array = []

# ファイルを読み込みurl_arrayに保存
with open(input_path, 'r', encoding="utf-8-sig") as uf:
    # １行ずつ読み込み
    for line in uf:
        # 改行コードを削除
        line = line.replace('\n','')
        # url_arrayに追加
        url_array.append(line)
        


# QRコードの作成
for url in url_array:
    # 連番を付与
    seq += 1
    # QRコードを作成
    qr_img = qrcode.make(url)

    # 出力先ファイルパスを指定
    # ファイル名は"連番(seq).png"
    path = os.path.join("../../../..","output","qr",f"{seq}.png")

    # QRコードを保存
    qr_img.save(path)

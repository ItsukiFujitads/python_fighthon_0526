import os
import qrcode
import sys

args = sys.argv

# 仮でパスを指定
# input_path = "/home/matcha-23training/python/input/qrmaker.txt"

# 引数からファイルパスを取得
input_path = args[1]

# 出力先ファイルパスを指定
output_path ="/home/matcha-23training/python/output"

# QRコードの連番
seq = 0

# URLを保存する配列
url_array = []

# ファイルを読み込み配列に保存
with open(input_path, 'r', encoding="utf-8-sig") as uf:
    for line in uf:
        line = line.replace('\n','')
        url_array.append(line)
        


# QRコードの作成
for url in url_array:
    seq += 1
    qr_img = qrcode.make(url)

    # 保存先と保存ファイル名
    path = os.path.join(output_path,"qr",f"{seq}.png")

    # QRコードを保存
    qr_img.save(path)



# print(url_array)
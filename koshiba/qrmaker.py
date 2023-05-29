import os
import qrcode

# qrlistのファイルを開く
# qr_list = open('qr_list.txt', 'r')

# 個数計算
count = 1

with open('qr_list.txt', encoding="utf-8") as f:
    for line in f:
       print(line)
# for i in range(1, count+1):
    # # ファイルの保存場所・名前
    # path = os.path.join("../../../files", "output", f"{i}.png")

    # # pngファイルの生成
    # img = qrcode.make('qrlist')
    # img.save(path)

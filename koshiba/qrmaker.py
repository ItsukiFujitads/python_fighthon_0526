import os
import qrcode

# qrlistのファイルを開く
# qr_list = open('qr_list.txt', 'r')


count = 1
with open('qrlist.txt', encoding="utf-8") as f:
    for i in f:
        print(i)
        # ファイルの保存場所・名前
        path = os.path.join("../../..", "output", f"{count}.png")

        # pngファイルの生成
        img = qrcode.make(i)
        img.save(path)
        count += 1

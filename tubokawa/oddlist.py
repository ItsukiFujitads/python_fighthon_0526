"""
配列から奇数の要素を抽出する処理
"""


# 名前を配列に格納
names = ["Kurita", "Tanaka", "Kaneda", "Noda", "Koyama",
              "Adachi", "Kuriyama", "Ohyama", "Kishida"]


# 奇数の要素のみ格納する空の配列を作成
odd_list = []


# 奇数の要素数の時に出力する
for name in names:
    # 要素番号が奇数か判定
    if names.index(name) % 2 != 0:
        # 奇数の時の処理
        odd_list.append(name)

print(odd_list, end="") 


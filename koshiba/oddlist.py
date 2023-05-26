# リストの定義
names = ["Kurita", "Tanaka", "Kaneda", "Noda", "Koyama", "Adachi", "Kuriyama", "Ohyama", "Kishida"]

# 空リストの定義
names_selected = []

# 要素数の計算
count = len(names)

# 偶数・奇数別に繰り返し回数を計算
if count % 2 != 0:
    repeat_number = count - 2
else:
    repeat_number = count - 1

# 要素の抽出(空リストに挿入)
for i in range(1, repeat_number+1, 2):
    names_selected.append(names[i])

# 抽出済みのリストを出力
print(names_selected, end="")




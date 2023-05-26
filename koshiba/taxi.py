import sys
args = sys.argv

# 引数を変数に代入
distance = int(args[1])

# 1500 mを境に運賃計算
if distance <= 1500:
    price = 630
else:
    step = (distance - 1500) // 344 + 1 
    price = 630 + 98 * step

# 料金の出力
print(int(round(price, 0)), end="")
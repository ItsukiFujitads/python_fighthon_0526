import sys
args = sys.argv

# 引数を変数に代入
number = int(args[1])

# 絶対値計算
number_abs = abs(number)

# 引数の整数およびその絶対値の出力
print(f'{number} {number_abs}', end="")
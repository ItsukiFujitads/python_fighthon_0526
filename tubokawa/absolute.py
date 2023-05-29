import sys
args = sys.argv

import math

#入力値を取得
input_num = int(args[1])

# 絶対値を算出し格納
num_abs =  abs(input_num)

# 絶対値を出力
print(f'{input_num} {num_abs}')
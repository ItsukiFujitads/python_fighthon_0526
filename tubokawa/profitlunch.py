"""
唐揚げ定食とカレーセットの売り上げ、原価、粗利率を出力するプログラム
"""


# saleslunch.pyを活用

import sys
args = sys.argv
from decimal import Decimal

# 唐揚げ定食とカレーセットの注文数を取得
chicken_order_num = int(args[1])
curry_order_num = int(args[2])

# 唐揚げ定食とカレーセットの値段を設定
chicken_fee = 760
curry_fee = 850


# 唐揚げ定食とカレーセットの粗利率を設定
chicken_cost_rate = 32.3 / 100
curry_cost_rate = 28.4 /100


# 唐揚げ定食とカレーセットの売上高計算
chicken_sales = chicken_order_num * chicken_fee
curry_sales = curry_order_num * curry_fee

# 唐揚げ定食とカレーセットの粗利率計算
chiken_cost = chicken_cost_rate * chicken_sales
curry_cost = curry_cost_rate * curry_sales

# 一日の売上高の計算
total_sales = chicken_sales + curry_sales

# round関数の場合、四捨五入時に誤差が生じる可能性があるため、Deimalを使用
# https://note.nkmk.me/python-round-decimal-quantize/

# 原価の計算(少数第一位を四捨五入)
total_cost = Decimal(chiken_cost + curry_cost).quantize(Decimal('0'), rounding='ROUND_HALF_UP')


# 粗利の計算
total_profit = total_sales - total_cost

# 出力
print(f'売上高：{total_sales}、原価：{total_cost}、粗利：{total_profit}', end="")


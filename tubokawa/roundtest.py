"""
decimalとround()の違いを確かめるためのプログラム
"""


from decimal import Decimal
import math

# 少数第一位で四捨五入したい
# 2001が出力されるはずだが...
decimal_num = Decimal(2000.5).quantize(Decimal('0'), rounding='ROUND_HALF_UP')
round_num = round(2000.5)
math_floor = math.floor(2000.6)
math_ceil = math.ceil(2000.6)

# decunak -> 2001, round() -> 2000が出力
print(f'decimal : {decimal_num}, round : {round_num}, floor : {math_floor}')



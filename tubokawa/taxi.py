"""
タクシー運賃を出力するプログラム
"""

#モジュールをインポート
import sys
args = sys.argv

import math

#入力値を距離として渡す
distance = int(args[1])

#初乗り距離
distance_starting = 1500

# 初乗り料金
fee_starting = 630

# 加算距離
distance_add = 344

# 一定距離ごとの加算料金
fee_per_add = 98

#　加算料金合計
fee_add = 0

# 運賃
fee = 0

# -----運賃計算----------------------

# 距離が初乗り距離を超えているのか判定
if distance >= distance_starting:
    #加算距離を計算
    fee_add = math.ceil((distance - distance_starting) / distance_add) * fee_per_add

fee = fee_starting + fee_add

#-------------------------運賃計算-----

# タクシー運賃を出力
print(fee, end='')
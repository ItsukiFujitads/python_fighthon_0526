import sys
args = sys.argv
from decimal import Decimal, ROUND_HALF_UP

# 引数を変数に代入
number_fried_chicken = int(args[1])
number_curry = int(args[2])

# 値段設定(価格改定があればここを操作)
prices = {"fried_chicken" : 760, "curry" : 850}
cost_rate = {"fried_chicken" : 0.323, "curry" : 0.284}

# 原価計算(商品別)
cost_fried_chicken = prices["fried_chicken"] * cost_rate["fried_chicken"]
cost_curry = prices["curry"] * cost_rate["curry"]

# 粗利計算(商品別)
profit_fried_chicken = prices["fried_chicken"] - cost_fried_chicken
profit_curry = prices["curry"] - cost_curry

# 合計値計算
sales = prices["fried_chicken"] * number_fried_chicken + prices["curry"] * number_curry
cost = cost_fried_chicken * number_fried_chicken + cost_curry * number_curry
cost = Decimal(cost).quantize(Decimal("0"),rounding=ROUND_HALF_UP)
profit = sales - cost

# 出力
print(f'売上高：{sales}、原価：{cost}、粗利：{profit}', end="")



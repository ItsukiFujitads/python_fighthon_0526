import sys
args = sys.argv

# 引数を変数に代入
number_fried_chicken = int(args[1])
number_curry = int(args[2])

# 値段設定(価格改定があればここを操作)
prices = {"fried_chicken" : 760, "curry" : 850}
cost_rate = {"fried_chicken" : 32.3, "curry" : 28.4}

# 原価計算
cost_fried_chicken = int(round(prices["fried_chicken"] * cost_rate["fried_chicken"], 0))
cost_curry = int(round(prices["curry"] * cost_rate["curry"], 0))

# 粗利計算
profit_fried_chicken = prices["fried_chicken"] - cost_fried_chicken
profit_curry = prices["curry"] - cost_curry
# 合計値計算
profit = profit_fried_chicken + profit_curry




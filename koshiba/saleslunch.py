import sys
args = sys.argv

# 引数を変数に代入
number_fried_chicken = int(args[1])
number_curry = int(args[2])

# 値段設定(価格改定があればここを操作)
prices = {"fried_chicken" : 760, "curry" : 850}

# 価格計算
sales = prices["fried_chicken"] * number_fried_chicken + prices["curry"] * number_curry
print(sales, end="")
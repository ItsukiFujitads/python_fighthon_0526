import sys
args = sys.argv

# 唐揚げ定食とカレーセットの注文数を取得
chicken_order_num = int(args[1])
curry_order_num = int(args[2])

# 唐揚げ定食とカレーセットの値段を設定
chicken_fee = 760
curry_fee = 850

# 唐揚げ定食とカレーセットの売上高計算
chicken_sales = chicken_order_num * chicken_fee
curry_sales = curry_order_num * curry_fee

# 一日の売上高の計算
total_sales = chicken_sales + curry_sales

print(total_sales)
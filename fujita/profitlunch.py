#モジュールインポート
import sys

#引数受取
karaage=int(sys.argv[1])
curry=int(sys.argv[2])

#値段設定
karaage_price=760
curry_price=850

#原価率設定
karaage_rate=0.323
curry_rate=0.284

#売り上げ計算
karaage_sales=karaage*karaage_price
curry_sales=curry*curry_price

#原価計算
karaage_cost=round(karaage_sales*karaage_rate)
curry_cost=round(curry_sales*curry_rate)

#粗利計算
karaage_profit=karaage_sales-karaage_cost
curry_profit=curry_sales-curry_cost

#売り上げ、原価、粗利、それぞれ合計
total_sales=karaage_sales+curry_sales
total_cost=karaage_cost+curry_cost
total_profit=karaage_profit+curry_profit

#出力
print(f'売上高：{total_sales}、原価：{total_cost}、粗利：{total_profit}',end='')
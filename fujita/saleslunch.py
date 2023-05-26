#モジュールインポート
import sys

#引数受取
karaage=int(sys.argv[1])
curry=int(sys.argv[2])

#値段設定
karaage_price=760
curry_price=850

#売り上げ計算
sales=karaage*karaage_price+curry*curry_price

#出力
print(sales,end='')
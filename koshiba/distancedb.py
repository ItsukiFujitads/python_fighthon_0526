from database import session # 1. データベースへの接続
from tables import Attendnum # 2. テーブルの定義
from decimal import Decimal, ROUND_HALF_UP
import sys
args = sys.argv

# 引数を変数に代入
first_station_name = args[1]
last_station_name = args[2]

# 乗車駅と後者駅の照合
first_station_position = session.query(Attendnum).filter_by(=first_station_name).first()
last_station_position = session.query(Attendnum).filter_by(=last_station_name).first()

# 取得したデータから距離を計算(ただし、計算結果は少数第2位まで出力)
distance = abs(last_station_position - first_station_position)
distance = Decimal(distance).quantize(Decimal("0"),rounding=ROUND_HALF_UP)

# 出力
print(distance, end="")


from database import session
from create_stations import Station

import sys
args = sys.argv

# 入力値の取得
dep_station = args[1]
arr_station = args[2]

# ---------データベースより駅名が一致するデータの東京からの距離を取得する処理

# 出発駅からの距離を取得
dep_station_distance = session.query(Station.kilo).filter_by(
    name = dep_station
).first().kilo

# 到着駅からの距離を取得
arr_station_distance = session.query(Station.kilo).filter_by(
    name = arr_station
).first().kilo
# 以下もOK
# arr_station_distance = session.query(Station).filter_by(
#     name = arr_station
# ).first().kilo

#---------------------------------------------

# ２駅間の距離を絶対値で返す
distance_bet = abs(dep_station_distance - arr_station_distance)

print(distance_bet, end="")



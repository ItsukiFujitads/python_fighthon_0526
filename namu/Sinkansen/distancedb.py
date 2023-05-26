import sys
from database import session
from tables import Station
args = sys.argv

station1 = args[1]
station2 = args[2]

sta1_dis = session.query(Station.sta_dis).filter_by(sta_name=station1).all()
sta2_dis = session.query(Station.sta_dis).filter_by(sta_name=station2).all()

try:
    result = float(sta1_dis[0][0])-float(sta2_dis[0][0])
    if result < 0:
        result *= -1 
    print(format(result, '.2f'), end="")
except KeyError:
    print("のぞみの停車駅を引数に設定してください", end="")
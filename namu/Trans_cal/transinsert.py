import sys
from tables import TTT
from database import session
import datetime

args = sys.argv

input1 = args[1]
input2 = args[2]
input3 = args[3]
input4 = args[4]
input5 = args[5]
input6 = args[6]

input1_int = datetime.datetime.strptime(input1,"%Y%m%d")

try:
    Transportaion = TTT(
        tra_date = input1_int,
        tra_num = int(input2),
        tra_sta = input3,
        tra_end = input4,
        tra_line = input5,
        tra_fee = int(input6)
    )
    session.add(Transportaion)
    session.commit()
    print("交通費計算テーブルにデータを登録しました", end="")

except Exception as e:
    print("交通費計算テーブルにデータを登録できませんでした", e)
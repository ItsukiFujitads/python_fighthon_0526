"""
transportテーブルにデータを挿入するプログラム
"""

from database import session
from create_transport import Transport
import sys
import datetime
args = sys.argv



# 入力値の取得
# 日付の取得
input_date = datetime.datetime.strptime(args[1], '%Y%m%d')
print(input_date)
#　連番の取得
input_seq = int(args[2])

# 出発駅の取得
input_dep_station = args[3]

# 到着駅の取得
input_arr_station = args[4]

# 交通機関の取得
input_via = args[5]

# 金額の取得
input_amount = int(args[6])


try:
    # データを登録
    data_transport = Transport(
        date = input_date,
        seq = input_seq,
        departure = input_dep_station,
        arrival = input_arr_station,
        via = input_via,
        amount = input_amount
    )

    session.add(data_transport)

    session.commit()

    print('交通費精算テーブルにデータを登録しました')
except:
    print('error:交通費精算テーブルにデータを登録出来ませんでした')

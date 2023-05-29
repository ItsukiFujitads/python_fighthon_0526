"""
交通費精算テーブル(transport)にデータを挿入するプログラム
"""

from database import session
from create_transport import Transport
import sys
import datetime
args = sys.argv



# 入力値の取得
# 日付を取得し、date型に変換
input_date = datetime.datetime.strptime(args[1], '%Y%m%d')

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
        # 利用日
        date = input_date,
        # 連番
        seq = input_seq,
        # 出発地
        departure = input_dep_station,
        # 到着地
        arrival = input_arr_station,
        # 経由/利用交通機関
        via = input_via,
        # 金額
        amount = input_amount
    )

    # データ追加
    session.add(data_transport)

    session.commit()

    print('交通費精算テーブルにデータを登録しました')

# DBにデータ追加できなかった時用のエラー処理
except:
    print('error:交通費精算テーブルにデータを登録出来ませんでした')

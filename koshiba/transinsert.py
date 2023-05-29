from database import session # 1. データベースへの接続
from tables import Transport # 2. テーブルの定義
from datetime import date
import sys
args = sys.argv

# 引数を変数に代入
day = args[1]
first_station = args[2]
last_station = args[3]
line_name = args[4]
total_price = int(args[5])

try:
    # 入力値(日付)の分割(日付を文字列から日付型に変更)
    year, month, today =  day[:4], day[4:6], day[6:]
    dt = date(int(year), int(month), int(today))

    # seqのカウント
    seq_check = session.query(Transport).filter_by(data=day).count()
    seq_num = seq_check + 1

    # 登録するデータの編集
    transport = Transport(
        data = dt,
        seq = seq_num,
        departure = first_station,
        arrival = last_station,
        via = line_name,
        amount = total_price
    )

    # INSERT処理
    session.add(transport)

    # コミット
    session.commit()

    # 正常にデータが登録できた場合
    print('交通費清算テーブルにデータを登録しました')

except:
    # データが登録できない場合
    print('error:交通費清算テーブルにデータを登録できませんでした')


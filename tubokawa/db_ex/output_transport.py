from database import session
from create_transport import Transport
import datetime
import os

# 保存先ディレクトリパスの設定
# path = os.path.join("../../../")
path = "/home/matcha-23training/python/output/output.txt"


# データを取得
transport_datas = session.query(
    Transport.date, Transport.seq, Transport.departure, Transport.arrival, Transport.via ,Transport.amount
    ).all()

# ファイルの書き込み処理
with open(path, mode="w") as tf:
    for transport_data in transport_datas:
        # print(transport_data.date.strftime('%Y%m%d'))
        # データから抽出した内容を変数に格納
        output_date = transport_data.date.strftime('%Y%m%d')
        output_seq = transport_data.seq
        output_dep = transport_data.departure
        output_arr = transport_data.arrival
        output_via = transport_data.via
        output_amount = transport_data.amount

        # データを書き込む処理
        tf.write(f'"{output_date}", "{output_seq}", "{output_dep}", "{output_arr}", "{output_via}", "{output_amount}"\n')


"""
交通費精算データをテキストファイルで出力するプログラム
"""

from database import session
from create_transport import Transport
import os

# 保存先ディレクトリパスの設定
path = os.path.join("../../../..","output","output.txt")



# データを取得
transport_datas = session.query(
    Transport.date, Transport.seq, Transport.departure, Transport.arrival, Transport.via ,Transport.amount
    ).all()

# ファイルの書き込み処理
with open(path, mode="w") as tf:
    for transport_data in transport_datas:
        # print(transport_data.date.strftime('%Y%m%d'))
        # データから抽出した内容を変数に格納
        # 利用日
        output_date = transport_data.date.strftime('%Y%m%d')
        # 連番
        output_seq = transport_data.seq
        # 出発地
        output_dep = transport_data.departure
        # 到着地
        output_arr = transport_data.arrival
        # 経由/利用交通機関
        output_via = transport_data.via
        # 金額
        output_amount = transport_data.amount

        # データを書き込む処理
        tf.write(f'"{output_date}", "{output_seq}", "{output_dep}", "{output_arr}", "{output_via}", "{output_amount}"\n')


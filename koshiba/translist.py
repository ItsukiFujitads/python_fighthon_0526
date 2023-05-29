import sys
args = sys.argv
from database import session # 1. データベースへの接続
from tables import Transport # 2. テーブルの定義

# ファイルの読み書き
sh = open("../../../files/output.txt", mode="w", encoding="utf-8")

# データヴェースから個数を取得
count = session.query(Transport).filter().count()

# 全件出力
for i in range(1, count+1):
    # データの抽出
    data_unit = session.query(Transport).filter_by(seq=i).first()

    # 日付の表記変換
    date_str = str(data_unit.data)
    date_str = date_str[:4] + date_str[5:7] + date_str[8:]

    # データの反映
    if i < count:
        sh.write(f'"{date_str}", "{data_unit.seq}", "{data_unit.departure}", "{data_unit.arrival}", "{data_unit.via}", "{data_unit.amount}"\n')
    else:
        sh.write(f'"{date_str}", "{data_unit.seq}", "{data_unit.departure}", "{data_unit.arrival}", "{data_unit.via}", "{data_unit.amount}"')

# 終了
sh.close
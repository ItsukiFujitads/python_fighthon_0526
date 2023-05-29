"""
Stationsテーブルにデータを挿入するプログラム
"""


from database import session
from create_stations import Station


# 駅名と東京駅からの距離を辞書データとして格納
datas_from_Tokyo = {
    '東京' : 0.00,
    '品川' : 6.78,
    '新横浜' : 25.54,
    '名古屋' : 342.02,
    '京都' : 476.31,
    '新大阪' : 515.35
}

# 連番の初期値を0に設定
seq = 0

# 距離データをデータベースに追加
for key in datas_from_Tokyo.keys():
    # データ数が増えると連番+1
    seq += 1
    data_from_Tokyo = Station(
        # 連番
        seq = seq,
        # 駅名
        name = key,
        # 東京駅からの距離
        kilo = datas_from_Tokyo[key]
    )

    # データ追加
    session.add(data_from_Tokyo)

session.commit()

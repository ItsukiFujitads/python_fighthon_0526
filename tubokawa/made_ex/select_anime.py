"""
データをDBから取得し表示するプログラム

第一引数に条件、第２引数にデータ数を入力
条件は以下
    "名前順","放送順","評価順"
出力はアニメの名前とスコアを出力
"""

from database import session
from create_anime_table import Anime
from sqlalchemy import asc


import sys
args = sys.argv

# 条件が入っている辞書型配列
conditions = {
            "名前順":Anime.name,
            "放送順": Anime.date,
            "評価順": Anime.score
                                    }

# 入力値の取得
input_condition = args[1]
data_num = int(args[2])

# している条件を入力しているか判定する変数
is_condition = False

# 条件が存在していたらis_condition=True
for key in conditions.keys():
    if key == input_condition:
        condition = conditions[key]
        is_condition = True
        break

# 存在しない条件を入力していた場合
if is_condition==False:
    print('正しい条件を入力してください')
else:
    outputs = session.query(Anime.name, Anime.date, Anime.score, Anime.eval_num).\
        order_by(asc(condition)).\
        limit(data_num).all()

# 結果の出力
    print('************************')
    print(f'{key}で並べた結果を出力します')
    print('************************')

    for output in outputs:
        output_name = output[0]
        # date型を文字型に変換（年月日を追加）
        output_date = output[1].strftime('%Y年%m月%d日')
        output_score = output[2]
        output_eval_num = output[3]
        print(f'{output_name}:{output_score}点 {output_date}放送')
        

    print('************************')

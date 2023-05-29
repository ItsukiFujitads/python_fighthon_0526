import csv
import datetime
from database import session
from create_anime_table import Anime



# CSVファイルの読み込み
with open('anime_data.csv', 'r', encoding="utf-8-sig") as af:
    reader = csv.reader(af)
    next(af)
    for line in reader:
        # アニメの名前
        name = line[0]
        # アニメの初回放送日
        date = datetime.datetime.strptime(line[1], '%Y%m')
        print(date)
        # アニメの評価
        score = float(line[2])
        # 評価者数
        eval_num = int(line[3])

        # データを挿入
        data_anime = Anime(
            name = name,
            date = date,
            score = score,
            eval_num = eval_num,
        )

        session.add(data_anime)

        session.commit()


    print('アニメを登録しました')

    # print(f'名前:{name}, 放送日:{date}, 評価:{rate}')

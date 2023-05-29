"""
交通費精算テーブルを作成するプログラム
"""

import sys
from sqlalchemy import Column, String, Integer, Date
from database import Base
from database import ENGINE

# Stationnsテーブル（交通費精算テーブル）の定義
class Transport(Base):
    # テーブル名
    __tablename__ = 'transport'
    # 利用日
    date = Column('date', Date, primary_key=True)
    # 連番
    seq = Column('seq', Integer, primary_key=True)
    # 出発地
    departure = Column('departure', String(20))
    # 到着地
    arrival = Column('arrival', String(20))
    # 経由/利用交通機関
    via = Column('via', String(40))
    # 金額
    amount= Column('amount', Integer)


def main(args):
    Base.metadata.create_all(bind=ENGINE)

if __name__ == '__main__':
    main(sys.argv)

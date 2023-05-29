"""
stationsテーブルを作成するプログラム
"""


import sys
from sqlalchemy import Column, String, Integer, DECIMAL
from database import Base
from database import ENGINE

# Stationnsテーブルの定義
class Station(Base):
    # テーブル名定義
    __tablename__ = 'stations'
    # 連番
    seq = Column('seq', Integer, primary_key=True)
    # 駅名
    name = Column('name', String(20))
    # 東京駅からの距離
    kilo = Column('kilo', DECIMAL(6,2))


def main(args):
    Base.metadata.create_all(bind=ENGINE)

if __name__ == '__main__':
    main(sys.argv)

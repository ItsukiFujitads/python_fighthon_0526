"""
アニメテーブルを作成するプログラム
"""

import sys
from sqlalchemy import Column, String, Integer, Float, Date
from database import Base
from database import ENGINE


import csv
import datetime

# animesテーブルの定義
class Anime(Base):
    __tablename__ = 'animes'
    name = Column('name', String(40), primary_key=True)
    date = Column('date', Date, primary_key=True)
    score = Column('score', Float)
    eval_num = Column('eval_num', Integer)

def main(args):
    Base.metadata.create_all(bind=ENGINE)

if __name__ == '__main__':
    main(sys.argv)

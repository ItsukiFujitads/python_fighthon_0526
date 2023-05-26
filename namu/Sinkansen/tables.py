import sys
from sqlalchemy import Column, Integer, VARCHAR, DECIMAL
from database import Base
from database import ENGINE

#テーブル：Holidayの定義
class Station(Base):
    __tablename__ = 'station'
    sta_num = Column('seq', Integer, primary_key = True)
    sta_name = Column('name', VARCHAR(20))
    sta_dis = Column('distance', DECIMAL(6,2))

def main(args):
    """
    メイン関数
    """
    Base.metadata.create_all(bind = ENGINE)

if __name__ == "__main__":
    main(sys.argv)

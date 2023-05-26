import sys
from sqlalchemy import Column, Integer, VARCHAR, Date
from database import Base
from database import ENGINE

#テーブル：Holidayの定義
class TTT(Base):
    __tablename__ = 'Transportaion'
    tra_date = Column('data', Date, primary_key = True)
    tra_num = Column('seq', Integer, primary_key = True)
    tra_sta = Column('departure', VARCHAR(20))
    tra_end = Column('arrival', VARCHAR(20))
    tra_line = Column('via', VARCHAR(40))
    tra_fee = Column('amount', Integer)


def main(args):
    """
    メイン関数
    """
    Base.metadata.create_all(bind = ENGINE)

if __name__ == "__main__":
    main(sys.argv)

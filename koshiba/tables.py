import sys
from sqlalchemy import Column, String, Date, Integer, Numeric
from database import Base
from database import ENGINE

# テーブル : Stationsの定義
class Stations(Base):
    __tablename__ = 'stations'
    seq = Column('seq', Integer, primary_key = True)
    name = Column('name', String(20))
    kilo = Column('kilo', Numeric(6,2))

# テーブル : Transportの定義
class Transport(Base):
    __tablename__ = 'transport'
    data = Column('data', Date, primary_key = True) # 利用日
    seq = Column('seq', Integer, primary_key = True) # 連番
    departure = Column('departure', String(20)) # 出発地
    arrival = Column('arrival', String(20)) # 到着地
    via = Column('via', String(40)) # 経由/利用交通機関
    amount = Column('amount', Integer) # 金額

def main(args):
    """メイン関数"""
    Base.metadata.create_all(bind = ENGINE)

if __name__ == "__main__":
    main(sys.argv)

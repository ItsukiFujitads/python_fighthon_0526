import sys
from sqlalchemy import Column, String, Integer, Date
from database import Base
from database import ENGINE

# Stationnsテーブルの定義
class Transport(Base):
    __tablename__ = 'transport'
    date = Column('date', Date, primary_key=True)
    seq = Column('seq', Integer, primary_key=True)
    departure = Column('departure', String(20))
    arrival = Column('arrival', String(20))
    via = Column('via', String(40))
    amount= Column('amount', Integer)


def main(args):
    Base.metadata.create_all(bind=ENGINE)

if __name__ == '__main__':
    main(sys.argv)

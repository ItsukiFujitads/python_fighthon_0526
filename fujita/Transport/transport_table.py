import sys
from sqlalchemy import Column,Integer,VARCHAR,DECIMAL,Date
from distance_config import Base,ENGINE
#テーブル
class Transport(Base):
  __tablename__ = 'transport'
  date=Column('date',Date,primary_key=True)
  seq = Column('seq', Integer, primary_key = True)
  departure=Column('departure',VARCHAR(20))
  arrival=Column('arrival',VARCHAR(20))
  via=Column('via',VARCHAR(40))
  amount=Column('amount',Integer)


Base.metadata.create_all(bind=ENGINE)
import sys
from sqlalchemy import Column,Integer,VARCHAR,DECIMAL
from distance_config import Base,ENGINE
#テーブル
class Stations(Base):
  __tablename__ = 'stations'
  seq = Column('seq', Integer, primary_key = True)
  name = Column('name', VARCHAR(20))
  kilo=Column('kilo',DECIMAL(6,2))

Base.metadata.create_all(bind=ENGINE)

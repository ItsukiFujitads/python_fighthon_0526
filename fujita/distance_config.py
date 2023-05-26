import sys
from sqlalchemy import Column, String, Date, Integer,NUMERIC
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

# MySQL DB settings
DATABASE = "mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8".format(**{
  "user": os.getenv("DB_USER", "root"),#DB_USERがなければrootの意味
  "password": os.getenv("DB_PASSWORD", "mysql"),
  "host": os.getenv("DB_HOST", "localhost"),
  "database": os.getenv("DB_DATABASE", "ENSHU") 
})
ENGINE = create_engine(
  DATABASE,
  encoding="utf-8",
  echo=True # True: SQL is output each time it is executed
)
# Session creation
session = scoped_session(
  # ORM execution settings
  sessionmaker(
    autocommit = False,
    autoflush = False,
    bind = ENGINE
    )
)
# tables.pyで継承する
Base = declarative_base()
Base.query = session.query_property()

#テーブル：Holidayの定義
class Stations(Base):
  __tablename__ = 'stations'
  seq = Column('seq', Integer, primary_key = True)
  name = Column('name', String(20))
  kilo=Column('kilo',NUMERIC(6,2))

Base.metadata.create_all(bind=ENGINE)

tokyo=Stations(
  seq=1,
  name='東京',
  kilo=0.00
)
shinagawa=Stations(
  seq=2,
  name='品川',
  kilo=6.78
)
shinyokohama=Stations(
  seq=3,
  name='新横浜',
  kilo=25.54
)
nagoya=Stations(
  seq=4,
  name='名古屋',
  kilo=342.02
)
kyoto=Stations(
  seq=5,
  name='京都',
  kilo=476.31
)
shinoosaka=Stations(
  seq=6,
  name='新大阪',
  kilo=515.35
)

session.add(tokyo)
session.add(shinagawa)
session.add(shinyokohama)
session.add(nagoya)
session.add(kyoto)
session.add(shinoosaka)

session.commit()
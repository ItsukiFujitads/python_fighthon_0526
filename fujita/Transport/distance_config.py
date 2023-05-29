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
  echo=False # True: SQL is output each time it is executed
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
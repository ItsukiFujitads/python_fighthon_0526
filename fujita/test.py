from distance_config import session
from sqlalchemy import inspect
ins=inspect(ENGINE)
print(ins.get_columns("stations"))
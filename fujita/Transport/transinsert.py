from distance_config import session 
from transport_table import Transport
import sys

args=sys.argv
date=args[1]
seq=int(args[2])
departure=args[3]
arrival=args[4]
via=args[5]
amount=int(args[6])

add_column=Transport(
  date=date,
  seq=seq,
  departure=departure,
  arrival=arrival,
  via=via,
  amount=amount
)

try:
    session.add(add_column)
    session.commit()
except Exception as e:
    print('error:交通費精算テーブルにデータを登録できませんでした')
    #print(e)

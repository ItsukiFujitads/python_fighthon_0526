import sys
from distance_config import session
from transport_table import Transport
from sqlalchemy import inspect

filename=sys.argv[1]
all_record=session.query(Transport).all()

with open('output/'+filename,mode='w',encoding='utf-8') as f:
    for r in all_record:
        add_str='"'+str(r.date)+'","'+str(r.seq)+'","'+str(r.departure)+'","'+str(r.arrival)+'","'+str(r.via)+'","'+str(r.amount)+'"\n'
        f.write(add_str)
    

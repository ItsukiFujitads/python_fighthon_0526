from database import session
from create_transport import Transport
import datetime

transport_datas = session.query(
    Transport.date, Transport.seq, Transport.departure, Transport.arrival, Transport.via ,Transport.amount
    ).all()



print(transport_datas[1].date.strftime('%Y%m%d'))

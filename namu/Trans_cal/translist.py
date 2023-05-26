from tables import TTT
from database import session
import re

with open("../output/output.txt", mode="w", encoding="utf-8") as f:
    i = 0
    for i in range(len(session.query(TTT.tra_num).all())):
        ddd = session.query(TTT.tra_date).all()
        ddd2 = ddd[i][0]
        ddd3 = str(ddd2)
        ddd4 = ddd3.replace("-","")

        eee = session.query(TTT.tra_num).all()[i][0]
        rrr = session.query(TTT.tra_sta).all()[i][0]
        qqq = session.query(TTT.tra_end).all()[i][0]
        fff = session.query(TTT.tra_line).all()[i][0]
        zzz = session.query(TTT.tra_fee).all()[i][0]

        f.write("\"{0}\"、\"{1}\"、\"{2}\"、\"{3}\"、\"{4}\"、\"{5}\"\n".format(ddd4, eee, rrr, qqq, fff, zzz))
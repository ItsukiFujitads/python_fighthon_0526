import sys
from distance_config import session
from distance_table import Stations
st1=sys.argv[1]
st2=sys.argv[2]

st1_dist=session.query(Stations.kilo).filter_by(name=st1).all()
st2_dist=session.query(Stations.kilo).filter_by(name=st2).all()

distance=round(abs(float(st1_dist[0][0])-float(st2_dist[0][0])),2)

print(distance)
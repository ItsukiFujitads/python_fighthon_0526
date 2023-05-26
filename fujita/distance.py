import sys
import os
from distance_config import session,Stations
st1=sys.argv[1]
st2=sys.argv[2]

st1_dist=session.query(Stations.kilo).filter_by(name=st1).all()
st2_dist=session.query(Stations.kilo).filter_by(name=st2).all()

distance=abs(st1_dist-st2_dist)

print(distance)
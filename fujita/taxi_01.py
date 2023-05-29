#モジュールインポート

import sys
import math

#引数受取
distance=int(sys.argv[1])

#運賃設定
initial_fare=630
initial_distance=1500

fare=98
per_m=344

#運賃計算
if distance-initial_distance > 0:
    dist=distance-initial_distance
else:
    dist=0
total_fare=(math.ceil(dist/per_m))*98 + initial_fare

#出力
print(total_fare,end='')
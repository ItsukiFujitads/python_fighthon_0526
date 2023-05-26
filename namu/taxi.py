import sys
args = sys.argv

distance = int(args[1])
fee = 630

if distance <= 1500:
    print(fee, end="")
else:
    a = divmod(distance-1500, 344)
    b = int(a[0]) * 98 
    fee += b
    if a[1] == 0:
        pass
    else:
        fee += 98
    print(fee, end="")

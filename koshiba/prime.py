import sys
args = sys.argv

# 引数を変数に代入
num = int(args[1])


# 素数判定。2からnum-1の整数でnumを割り、一回でも余りが0になれば素数ではない。
if num < 1000 and num != 1:
    # 素数検出
    for i in range(2, num):
        if num % i == 0:
            num = num / i
            while num % i == 0:
                num = num / i
            else:
                pass
        else:
            pass

    if num == int(args[1]):
        print("prime", end="")
    else:
        print("not", end="")
elif num == 1:
    print("prime", end="")
else:
    print("1000以上は判定できません", end="")





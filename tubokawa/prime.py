# モジュールをインポート
import sys
args = sys.argv
import math


input_num = int(args[1])

if input_num >= 1000:
    print('1000以上は判定できません', end="")
    
else:
    # 入力値の平方根を求め、切り上げる処理
    dev_max_num = math.ceil(math.sqrt(input_num))

    # 素数か判定する変数
    is_prime = True

    # 入力値が素数か判定する処理
    # 入力値の平方根+1回分だけ処理を実行することで処理回数の減少
    for num in range(2,dev_max_num+1):
        if input_num % num == 0:
            # 割り切れたので素数ではない : False
            is_prime = False
            break

    if is_prime:
        print('prime', end="")
    else:
        print('not', end="")

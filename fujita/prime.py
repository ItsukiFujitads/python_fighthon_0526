#モジュールインポート
import sys

#引数受取
num=int(sys.argv[1])

#フラグ設定
flag=True

if num < 2:
    print('not',end='')
elif num >=1000:
    print('1000以上は判定できません',end='')
else:
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            flag=False
    if flag:
        print('Prime',end='')
    else:
        print('not',end='')

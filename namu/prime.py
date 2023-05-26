import sys
args = sys.argv

input_num= int(args[1])
sousu = 0

def primenumber(input_num):
    for i in range(2, input_num):	
    	if input_num % i == 0:		
            return False
    return True	

if primenumber(input_num) == True:
    print("prime", end="")
elif input_num >= 1000:
    print("1000以上は判定できません", end="")
else:
    print("not", end="")
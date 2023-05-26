import sys
args = sys.argv

number = int(args[1])

print(number, end="")

if number < 0:
    number *= -1

print(" "+str(number), end="")
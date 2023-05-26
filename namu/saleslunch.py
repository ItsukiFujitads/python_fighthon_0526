import sys
args = sys.argv

karaage = int(args[1])
curry = int(args[2])

sales = karaage*760 + curry*850

print(sales, end="")

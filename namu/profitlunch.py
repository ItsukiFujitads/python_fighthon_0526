import sys
args = sys.argv

karaage_num = int(args[1])
curry_num = int(args[2])

kara_pc = 760 * 32.3 / 100
curry_pc = 850 * 28.4 / 100

sales = karaage_num*760 + curry_num*850
prime_cost = kara_pc*karaage_num + curry_pc*curry_num
arari = sales-prime_cost


print("売上高：{0}、原価：{1}、粗利：{2}".format(sales, round(prime_cost), round(arari)), end="")
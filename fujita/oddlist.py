name_list=["Kurita","Tanaka","Kaneda","Noda","Koyama","Adachi","Kuriyama","Ohyama","Kishida"]
odd_list=[]
for i in range(1,len(name_list),2):
    odd_list.append(name_list[i])
print(odd_list,end='')
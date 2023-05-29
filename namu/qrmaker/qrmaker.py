import qrcode
import os

myFile = open('qrlist.txt', 'r', encoding="UTF-8")
data = myFile.read()
aaa = [data.splitlines()]

# for i in range(x):
# i = myFile.readline()
# print(i)
# print(aaa[0][1])

star = int(len(aaa))
#txt fileからライン数でアドレスをもらってくる
for i in range(star):
    img = qrcode.make(aaa[0][i])
    path = os.path.join("../output",  "png{0}.png".format(star))
    img.save(path)

myFile.close()
import sys
import qrcode

text_pass=sys.argv[1]
with open(text_pass,mode='r') as f:
    pass_list=f.read().split('\n')

file_num=1
for qr_pass in pass_list:
    img=qrcode.make(qr_pass)
    img.save('output/'+str(file_num)+'.png')
    file_num+=1

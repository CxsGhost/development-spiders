import re
import requests


file=open('wangyeyuan.txt','rb')
html=file.read()
file.close()

pic=re.findall('src="(.*)">',html.decode('utf-8'))
print(pic)
i=0
for each in pic:
    print("now downloads:"+each)
    pic_1=requests.get(each)
    fp=open('get到内容//'+"此处是文件名",'wb')
    fp.write(pic_1.content)
    fp.close()
    i+=1

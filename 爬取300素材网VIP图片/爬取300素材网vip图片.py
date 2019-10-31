import requests
import re
hea={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362"}
url=requests.get("http://300ppt.miaoying1.cn/muban/dzqybqjd.html",headers=hea).text
print(url)


list_1=re.findall("<div class='m-l'(.*?)本作品内容为27张渐变色低多边形PPT背景图片",url,re.S)
list_2=re.findall('data-original="(.*?)">',list_1[0],re.S)
number=0
for pic_url in list_2:

    print("正在下载第{}张图片：".format(number),pic_url)
    pic=requests.get(pic_url)
    file=open("picture//"+"{}".format(number),"wb")
    file.write(pic.content)
    file.close()
    number+=1






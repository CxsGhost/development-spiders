import re
text=open("E:\py\爬虫开发\百度文库爬虫\百度文库VIP文章检查元素源代码.txt","r",encoding="utf-8")
text_content=text.read()
print(text_content)
text_connect=[]
for index in range(18,136):
    need=re.findall('z-index:{};false">(.*?)</p>'.format(index),text_content,re.S)
    if len(need)!=0:
        text_connect.extend(need)
complete_text="".join(text_connect)
print(complete_text)

text.close()
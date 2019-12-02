import re
text=open("E:\py\爬虫开发\百度文库爬虫\百度文库VIP文章检查元素源代码.txt","r",encoding="utf-8")
text_content=text.read()
print(text_content)
text_connect=[]
need=re.findall('<div class="t_cover" style="left:(.*?)</div></div>',text_content,re.S)
for i in need:
    code=re.findall('">(.*?)',i)
    print(i)
    print(code)


text.close()
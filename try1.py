from lxml import etree
import requests

headers_1={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362"}
url=requests.get("https://wenku.baidu.com/view/208672d933d4b14e8524681f.html",headers=headers_1).content


print(url)

xpath_url=etree.HTML(url)
class_title=xpath_url.xpath('//*[@id="pageNo-1"]/div/div/div/div/div/p[19]/text()')
print(class_title)
#print(type(class_title[0]))
print("sdfsdf\\")


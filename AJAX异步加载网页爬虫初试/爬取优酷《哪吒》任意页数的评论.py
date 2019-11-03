import requests
import json
import time
import re
#得到当前时间戳的近似值
time_correct=time.time()
time_approximate=int(time_correct)

#构建评论列表的URL，接下来用以得到杰森格式的评论内容
comment_url="https://p.comments.youku.com/ycp/comment/pc/commentList?jsoncallback=n_commentList&\
app=100-DDwODVkv&objectId=1097963004&objectType=1&listType=0&current\
Page=385&pageSize=30&sign=8fc6ac73638d4f0263358f1ae323489b&time=1572784759".format(input("请输入，来获取本页的评论:"))

#得到包含在元组中的json数据
head={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"}
html=requests.get(comment_url,headers=head).text

#最重要的一步，也是最难的一步，卡了老子半天！！cnmd。
# 用正则表达式加以字符串操作函数，才终于去掉圆括号！！（json格式无法识别圆括号）
html_json=re.findall("ist(.*)",html,re.S)[0].strip(")").replace("(","")

#转化为json后，通过debug调试，发现是一个由列表和字典混合组成多层嵌套的字典，需要层层挖掘信息，格式化输出
json_content=json.loads(html_json)
content_data=json_content["data"]
data_comment=content_data["comment"]
number=1
for each_comment in data_comment:
    print("第{}条评论\n".format(number),"账号：",each_comment["userId"])
    print("用户名：",each_comment["user"]["userName"])
    if len(each_comment["user"]["vipInfo"])==0:
        print("VIP等级：非会员")
    else:
        print("VIP等级：",each_comment["user"]["vipInfo"]["name"])
    print("评论内容:".format(number),each_comment["content"],"\n","--"*25)
    number+=1



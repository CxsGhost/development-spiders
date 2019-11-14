import requests
from multiprocessing.dummy import Pool as ThreadPool
from lxml import etree
import re

pool = ThreadPool(8)
list_1 = [j*50 for j in range(0, 5)]
url_list = ["https://tieba.baidu.com/f?kw=%E8%B6%B3%E7%90%83&ie=\
utf-8&tab=good&cid=&pn={}".format(k) for k in list_1]


def Get_Html(quality_post_url):
    head = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"}
    number = re.search("pn=(.*)", quality_post_url, re.S).group(0).replace("pn=", '')
    print("正在处理第{}页".format(int(number)//50+1))
    qp_html = requests.get(quality_post_url, headers=head)
    return qp_html

# 首先统计本页共有多少精品贴


def Statistics(html_text):
    user_number = re.findall("data-field='{&quot;user_id&quot;:(.*?)}", html_text.text, re.S)
    return len(user_number)
# 开始获取每一个


def Spiders(url):
    qp_html = Get_Html(url)
    list_number = Statistics(qp_html)
    html_new = qp_html.text.replace(r'<!--', '"').replace(r'-->', '"')
    selector = etree.HTML(html_new)
    for i in range(1, list_number):
        data_field = selector.xpath('//*[@id="thread_list"]/li[{}]'.format(i))
        title = data_field[0].xpath('div/div[2]/div[1]/div[1]/a/text()')
        print('本页第{}条帖子'.format(i), ":\n", title[0])
        print()
        print("--"*20)


post_content = pool.map(Spiders, url_list)

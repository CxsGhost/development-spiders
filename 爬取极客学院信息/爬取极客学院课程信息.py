#
import requests
import re
import os
# 为了加快速度，创建一个线程池
from multiprocessing.dummy import Pool as threadpool
pool = threadpool(8)


class spider(object):
    # 选择要获取的网页
    def needpages(self):  # 将会在getallpages函数调用
        try:
            begin = int(input("input the begin page:"))
            end = int(input("input the finishing page:"))
            return begin, end
        except ValueError:
            print('the page is illegal!')
            os._exit(0)  # 此处一定要给与参数

    def get_all_pages(self):
        url_list = []
        begin_page, end_page = spider1.needpages()
        for page in range(begin_page,end_page+1):
            url_list.append("https://www.jikexueyuan.com/course/?pageNum={0}".format(page))
        return url_list

# 获取每个页面的课程列表
    class_code = []
    def get_all_class(self,web_url):
        # 将会在getcontent函数调用
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36\
         (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362"}
        print("正在处理：{}".format(web_url))
        class_list = requests.get(web_url, headers=headers)
        html_1 = class_list.text
        class_list_code = re.findall("<!--list-->(.*?)<!--list end-->", html_1, re.S)
        spider1.class_code.append(class_list_code)
        # return spider.class_code

#  爬取每个页面想要的指定内容
    def get_content(self):
        url = spider1.get_all_pages()
        pool.map(spider1.get_all_class, url)

        for page_code in spider.class_code:
            # 真正的源代码还在page code这个单元素列表中，所以下方使用正则表达式的时候，还需要加入一个索引
            list_1 = re.findall('class="lessonimg" title="(.*?)"', page_code[0], re.S)
            list_2 = re.findall('<p style="height: 0px; opacity: 0; display: none;">(.*?)</p>'\
                                , page_code[0], re.S)
            list_3 = re.findall('<i class="time-icon"></i><em>(.*?)</em>', page_code[0], re.S)
            spider1.print_the_infor(list_1, list_2, list_3)

    # 印出所爬取的信息
    def print_the_infor(self, list_1, list_2, list_3):  # 也在getcontent函数调用
        title, intro, timelong = list_1, list_2, list_3
        dic = []
        for i in range(len(title)):
            names = locals()
            names["dic_{}".format(i)] = {"title": title[i], "intro": intro[i], "infor": timelong[i]}
            dic.append(names['dic_{}'.format(i)])
            print()
            print('title:', dic[i]["title"])
            print('intro:', dic[i]['intro'])
            print('infor:', dic[i]["infor"])
            print()
            print("-"*200)


spider1 = spider()
spider1.get_content()





import requests  # 这就写爬虫最基本的库嘛
import re  # 正则表达式
import threading  # 为了加快速度


# 选择要获取的网页
def need_pages():  # 将会在getallpages函数调用
    while True:
        try:
            begin = int(input("开始页面："))
            end = int(input("结束页面："))
            return begin, end
        except ValueError:
            print('输入页码错误！请重试！')


def get_all_pages():
    url_list = []
    begin_page, end_page = need_pages()
    for page in range(begin_page, end_page+1):
        url_list.append("https://www.jikexueyuan.com/course/?pageNum={0}".format(page))
    return url_list


# 获取每个页面的课程列表
def get_all_class(url):
    # 将会在getcontent函数调用
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36\
     (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362"}
    print("正在处理：{}".format(url))
    class_list = requests.get(url, headers=headers).text
    class_code = re.findall("<!--list-->(.*?)<!--list end-->", class_list, re.S)
    # 采取一个先爬大再爬小的原则
    return class_code


#  爬取每个页面想要的指定内容
def get_content(url):
    class_content = get_all_class(url)[0]
    list_1 = re.findall('class="lessonimg" title="(.*?)"', class_content, re.S)
    list_2 = re.findall('<p style="height: 0px; opacity: 0; display: none;">(.*?)</p>', class_content, re.S)
    list_3 = re.findall('<i class="time-icon"></i><em>(.*?)</em>', class_content, re.S)
    print_the_info(list_1, list_2, list_3)


# 印出所爬取的信息
def print_the_info(list_1, list_2, list_3):  # 也在getcontent函数调用
    title, intro, timelong = list_1, list_2, list_3
    class_info = zip(title, intro, timelong)
    for i, j, k in class_info:
        print("课程名称：《{0}》\n课程简介：{1}\n课程时长：{2}\n{3}\n".format(i, j, k, "--"*50))
        # 我发现这个地方必须写成一个字符串，不然因为多线程的缘故，就会出现“抢着打印”的现象，就乱套了。。


if __name__ == "__main__":
    for t in get_all_pages():
        threading.Thread(target=get_content, args=(t,)).start()




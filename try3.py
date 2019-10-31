import requests
from requests.packages import urllib3
urllib3.disable_warnings()
url="https://weibo.com"

cook={"Cookie":"_T_WM=90597154397; SCF=AhYorgeF6658Wy6IYRTmqomKnrZ07BMWYTKLeDHlYoFiA4w-C3yv0-5QHNCLvA_fuH_OrrVTIjQ8nbJC3TS7FJM.; MLOGIN=1; SUB=_2A25wvHMRDeRhGeNK7VIV9SfMyj6IHXVQXx1ZrDV6PUJbkdANLWvhkW1NSUwdEW4I0xt2AsxA-nxGS63EaSDEfpeB; SUHB=08J7KNTMM0Pp0b; SSOLoginState=1572340545"}
hea={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"}
post_data={
    "username": "13156126936",
    "password": "Woaiziji11",
    "savestate": "1",
    "r": "https://weibo.cn/?luicode=20000174",
    "ec": "0",
    "pagerefer": "https://weibo.cn/pub/",
    "entry": "mweibo",
    "wentry": "",
    "loginfrom": "",
    "client_id": "",
    "code": "",
    "qq": "",
    "mainpageflag": "1",
    "hff": "",
    "hfp": "",
}

code=requests.get(url,cookies=cook).content
print(code.decode("gbk"))

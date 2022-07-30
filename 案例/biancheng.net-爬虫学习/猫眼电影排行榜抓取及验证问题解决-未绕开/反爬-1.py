import requests as req
import re
from bs4 import BeautifulSoup as bs
import time as ti

def link(url):
    header = {
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36",
        "cookie" : "__mta=151852934.1587443709643.1587598935122.1587600366133.43; uuid_n_v=v1; uuid=F37C1E10838811EA8ABB63E31D5D873EFCF954692DBF4022A2CA534951698F60; _lxsdk_cuid=1719b014425c8-0c9bf88d1425e9-4313f6b-1fa400-1719b014425c8; _lxsdk=F37C1E10838811EA8ABB63E31D5D873EFCF954692DBF4022A2CA534951698F60; mojo-uuid=d174ce0bb6042f1360f126301f67ba77; t_lxid=1719b0145b6c8-091e3087e85102-4313f6b-1fa400-1719b0145b6c8-tid; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; __mta=219069734.1587443484067.1587459109767.1587475084518.17; _csrf=1d00bd0bae5d97db8d8b75aba18f671878162878089874b0349b5d2a5037d688; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1587531265,1587558230,1587564223,1587598925; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1587600366; _lxsdk_s=171a4e020da-6c5-2ad-67c%7C%7C1"
    }
    res = req.get(url,headers = header)
    if res.status_code == 200:
        return bs(res.text,"lxml")
    return None

for i in range(0,20,10):
    url = "https://www.maoyan.com/board/4?timeStamp=1656322591954&channelId=40011&index=6&signKey=bc2b56e46a50708668e7352ad481242d&sVersion=1&webdriver=false&offset=" + str(i)
    movies = link(url).find_all("dd")
    for i in movies:
        img = i.find("img",class_ = "board-img").get("data-src")
        num = i.find("i").text
        name = i.find("a").get("title")
        actor = re.findall("主演：(.*)",i.find("p",class_ = "star").text)[0]
        when = re.findall("上映时间：(.*)",i.find("p",class_ = "releasetime").text)[0]
        score = i.find("i",class_ = "integer").text + i.find("i",class_ = "fraction").text
        url1 = "https://maoyan.com" + i.find("p",class_ = "name").a.get("href")
        movie = link(url1)
        ti.sleep(1)
        about = movie.find("span",class_ = "dra").text
        word = movie.find("span",class_ = "name").text +  ":  " + movie.find("div",class_ = "comment-content").text.replace(" ","")
        boss = movie.find("a",class_= "name").text.replace("\n","").replace(" ","")

        a = {
            "片名" : name,
            "排名" : num,
            "评分" : score,
            "网址" : url1,
            "演员" : actor,
            "上映时间" : when,
            "图片" : img,
            "评论" : word,
            "导演" : boss,
            "简介" : about
        }
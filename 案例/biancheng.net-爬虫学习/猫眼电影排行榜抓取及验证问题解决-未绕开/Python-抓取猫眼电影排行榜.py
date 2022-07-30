import pandas as pd
import time
import re
import csv
import random
from urllib import request
from requests.auth import HTTPBasicAuth#导入HTTPBasicAuth类
import requests

from ua_info import ua_list

#定义一个爬虫类
class MaoyanSpider(object):
    #1.初始化
    #1.1定义初始化页面URL
    def __init__(self):
        self.url = 'https://maoyan.com/board/4?offset={}'

    #1.2请求函数
    def get_html(self,url):
        # headers = {'User-Agent':random.choice(ua_list)}
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36",
            "cookie": "__mta=151852934.1587443709643.1587598935122.1587600366133.43; uuid_n_v=v1; uuid=F37C1E10838811EA8ABB63E31D5D873EFCF954692DBF4022A2CA534951698F60; _lxsdk_cuid=1719b014425c8-0c9bf88d1425e9-4313f6b-1fa400-1719b014425c8; _lxsdk=F37C1E10838811EA8ABB63E31D5D873EFCF954692DBF4022A2CA534951698F60; mojo-uuid=d174ce0bb6042f1360f126301f67ba77; t_lxid=1719b0145b6c8-091e3087e85102-4313f6b-1fa400-1719b0145b6c8-tid; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; __mta=219069734.1587443484067.1587459109767.1587475084518.17; _csrf=1d00bd0bae5d97db8d8b75aba18f671878162878089874b0349b5d2a5037d688; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1587531265,1587558230,1587564223,1587598925; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1587600366; _lxsdk_s=171a4e020da-6c5-2ad-67c%7C%7C1"
        }
        req = request.Request(url = url,headers= headers)
        res = request.urlopen(req)
        html = res.read().decode()
        #调用解析函数
        self.parse_html(html)
    #1.3解析函数
    def parse_html(self,html):
        #正则表达式
        re_bds = '<div class="movie-item-info">.*?title="(.*?)".*?<p class="star">(.*?)</p>.*?class="releasetime">(.*?)</p>'
        #生成正则对象
        pattern = re.compile(re_bds,re.S)
        r_list = pattern.findall(html)
        self.save_html(r_list)
    #1.4保存函数
    def save_html(self,r_list):
        #生成文件对象
        with open('maoyan.csv','a',newline = '',encoding='utf-8') as f:
            #生成CSV操作对象
            writer = csv.writer(f)
            #整理数据
            for r in r_list:
                name = r[0].strip()
                star = r[1].strip()[3:]
                #切片截取时间
                time = r[2].strip()[5:15]
                L = [name,star,time]
                #写入CSV
                writer.writerow(L)
                print(name,star,time)
    #1.5主函数
    def run(self):
        #抓取第一页数据
        for offset in range(0,11,10):
            url = self.url.format(offset)
            self.get_html(url)
            #生成1-2之间的浮点数,爬取休眠，避免识别
            time.sleep(random.uniform(1,2))

#主函数以脚本方式启动
if __name__ == '__main__':
    try:
        spider = MaoyanSpider()
        spider.run()
    except Exception as e:
        print('异常原因：',str(e))

# 反爬尝试
# ah = HTTPBasicAuth('admin','admin')
# url = 'https://www.maoyan.com'
# headers = {
#     'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
#     # 'Accept-Encoding': 'gzip, deflate, br',
#     'Accept-Language': 'zh-CN,zh;q=0.9',
#     'Connection': 'keep-alive',
#     'Referer':'https://www.maoyan.com/board?timeStamp=1656323547501&channelId=40011&index=6&signKey=b5e59b1c9ae866896ef06d4b36373f63&sVersion=1&webdriver=false',
#     'Cookie':'__mta=146051339.1656322557835.1656322876385.1656322886285.20; uuid_n_v=v1; uuid=8C1828C0F5FC11EC9A8FED2897673EE3026F5074A77E4E36AE7AED31A164E445; _csrf=ba7c38ec003d1213489b9d75174d1ac666a537f34d951f781140fbbca01f6b4e; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1656322558; _lxsdk_cuid=181a4848716c8-0afeca68c0efb6-613f5653-1fa400-181a48487162; _lxsdk=8C1828C0F5FC11EC9A8FED2897673EE3026F5074A77E4E36AE7AED31A164E445; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1656323188; __mta=146051339.1656322557835.1656322886285.1656323187647.21; _lxsdk_s=181a4848718-be8-d6-f4%7C%7C67',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36'
# }
# req = request.Request(url = url,headers= headers)
# res = request.urlopen(req)
# html = res.read().decode('utf-8')
# print(html)
# result = requests.get(url=url,headers= headers,auth= ah)
# if result.status_code == 200:
#     print(result.text)
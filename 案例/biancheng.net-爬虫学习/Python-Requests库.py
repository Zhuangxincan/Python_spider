# encoding	查看或者指定响应字符编码
# status_code	返回HTTP响应码
# url	查看请求的 url 地址
# headers	查看请求头信息
# cookies	查看cookies 信息
# text	以字符串形式输出
# content	以字节流形式输出，若要保存下载图片需使用该属性

import requests
from ua_info import ua_list
import random
url = 'https://img0.baidu.com/it/u=3434652324,1525281230&fm=253&fmt=auto&app=138&f=JPEG'

#简单定义浏览器ua信息
headers = {'User-Agent':random.choice(ua_list)}

#读取图片需要使用content属性
html = requests.get(url=url ,headers= headers).content

#以二进制形式下载图片
with open('./python.jpg','wb') as f:
    f.write(html)
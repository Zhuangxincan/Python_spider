import requests
from lxml import etree
from fake_useragent import UserAgent
import json

url = 'http://app.mi.com/categotyAllListApi?page=1&categoryId={}&pageSize=30'
url1 = 'http://app.mi.com/'
headers = {'User-Agent': UserAgent().random}
html = requests.get(url=url1, headers=headers).text
parse_html = etree.HTML(html)
# 获取分类
xpath_bds = '//ul[@class="category-list"]/li'
li_list = parse_html.xpath(xpath_bds)
print(li_list)
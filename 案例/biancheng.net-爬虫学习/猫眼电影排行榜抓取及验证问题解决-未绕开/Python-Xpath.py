# coding:utf8

import requests
from lxml import etree
from ua_info import ua_list
import random

class MaoyanSpider(object):
    def __init__(self):
        self.url = 'https://maoyan.com/board/4?offset=50'
        self.headers={'User-Agent':random.choice(ua_list)}

    def save_html(self):
        html = requests.get(url=self.url,headers=self.headers).text
        parse_html = etree.HTML(html)

        #基准xpath表达式，匹配10个<dd>节点对象
        dd_list = parse_html.xpath('//dl[@class="board-wrapper"]/dd')
        print(dd_list)
        # .// 表示dd节点的所有子节点后代节点
        # 构建item空字典将提取的数据放入其中
        item  = {}
        for dd in dd_list:
            #处理字典数据，注意xpath匹配结果是列表，因此需要索引【0】提取数据
            item['name']=dd.xpath('.//p[@class="name"]/a/text()')[0].strip()
            item['star'] = dd.xpath('.//p[@class="star"]/text()')[0].strip()
            item['time'] = dd.xpath('.//p[@class="releasetime"]/text()')[0].strip()
            # 输出数据
            print(item)
    def run(self):
        self.save_html()

if __name__ == '__main__':
    spider= MaoyanSpider()
    spider.run()
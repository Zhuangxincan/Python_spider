##scrapy用法不详，暂时无法实用

import scrapy
import re
import requests
from fontTools.ttLib import TTFont
from io import BytesIO
import time
from items import QidianxiaoshuoItem

class MainSpider(scrapy.Spider):
    name = 'main'
    star_urls = [f'https://www.qidian.com/rank/readIndex?page={i}' for i in range(1,2)]
    #将woff写入字典
    def get_font(self,url):
        time.sleep(1)
        response = requests.get(url)
        font = TTFont(BytesIO(response.content))
        cmap = font.getBestCmap()
        font.close()
        return cmap

    #将字典中的乱码解析为可识别字符
    def get_encode(self,cmap,values):
        WORD_MAP = {'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'period':'.','zero':0}
        word_count = ''
        list = values.split(';')
        list.pop(-1)
        for value in list:
            value = value[2:]
            key = cmap[int(value)]
            word_count += WORD_MAP[key]
        return word_count

    #从页面所需爬取数据
    def get_nums(self,url):
        #获取当前页面的html
        time.sleep(1)
        response = requests.get(url).text
        url_ttf_pattern = re.compile('</style><span.*?>(.*?)</span>', re.S)
        #获取当前页面所有数字字符
        numberlist = re.findall(url_ttf_pattern,response)
        #获取当前包含字体文件链接的文本
        reg = re.compile('<style>(.*?)\s*</style>',re.S)
        fonturl = re.findall(reg,response)[0]
        #通过正则获取当前页面字体文件链接
        url = re.search('woff.*?url.*?\'(.+?)\'.*?truetype',fonturl).group(1)
        cmap = self.get_font(url)
        print('cmap:',cmap)
        num_list = []
        for list1 in numberlist:
            num_list.append(self.get_encode(cmap,list1))
        return num_list

    def parse(self, response):
        res = response.xpath('//*[@id="rank-view-list"]/div/ul/li')
        for i in res:
            url = i.css('div:nth-child(1) a::attr(href)').extract_first()
            url = 'https:'+url
            yield  scrapy.Request(url,callback=self.parse_one,meta={'url':url})

    def parse_one(self,response):
        book_name = response.css('div.book-info h1 em::text').extract_first()
        author = response.css('a.writer::text').extract_first()
        intro = response.xpath('/html/body/div/div[6]/div[1]/div[2]/p[2]/text()').extract_first()
        num_list = self.get_nums(response.meta['url'])
        del num_list[1]
        word_num = str(num_list[0]) +response.xpath('/html/body/div/div[6]/div[1]/div[2]/p[3]/cite[1]/text()').extract_first()
        recommend_all = str(num_list[0]) +response.xpath('/html/body/div/div[6]/div[1]/div[2]/p[3]/cite[2]/text()').extract_first()
        recommend_week = str(num_list[0]) +response.xpath('/html/body/div/div[6]/div[1]/div[2]/p[3]/cite[3]/text()').extract_first()

        item = QidianxiaoshuoItem()
        item['book_name'] = book_name
        item['author']  = author
        item['intro'] = intro
        item['word_num'] = word_num
        item['recommend_all'] = recommend_all
        item['recommend_week'] = recommend_week

        yield item


if __name__ == '__main__':
    MainSpider

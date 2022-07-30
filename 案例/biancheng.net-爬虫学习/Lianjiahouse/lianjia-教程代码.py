import scrapy
# from Lianjiahouse.items import LianjiahouseItem 该方法导入失败
from ..items import LianjiahouseItem #使用该方法可行

class LianjiaSpider(scrapy.Spider):
    # name 指定爬虫文件名字
    name = 'lianjia'
    allowed_domains = ['bj.lianjia.com']# 网站域名
    start_urls = ['https://bj.lianjia.com/ershoufang/pg1/']# 第一个要抓取的url
    pg = 0

    def parse(self, response):
        # 基准xpath，匹配电影信息的dd节点对象列表
        h_list = response.xpath('//ul[@class="sellListContent"]/li[@class="clear LOGVIEWDATA LOGCLICKDATA"]')
        # 给items.py 中的类：Maoyan100Item（）实例化
        item = LianjiahouseItem()
        for h in h_list:
            item['name'] = h.xpath('.//a[@data-el="region"]/text()').get()
            item['model'] = h.xpath('.//div[@class="houseInfo"]/text()').get()[0].split('|')[0].strip()
            item['area'] = h.xpath('.//div[@class="houseInfo"]/text()').get()[0].split('|')[1].strip()
            item['direction'] = h.xpath('.//div[@class="houseInfo"]/text()').get()[0].split('|')[2].strip()
            item['perfect'] = h.xpath('.//div[@class="houseInfo"]/text()').get()[0].split('|')[3].strip()
            item['floor'] = h.xpath('.//div[@class="houseInfo"]/text()').get()[0].split('|')[4].strip()
            item['address'] = h.xpath('.//div[@class="positionInfo"]/a/text()').get()[0].strip()
            item['total_list'] =h.xpath('.//div[@class="totalPrice totalPrice2"]/span/text()').get()[0].strip()
            item['price_list'] = h.xpath('.//div[@class="unitPrice"]/span/text()').get()[0].strip()
            yield item
            # 需要setting.py中的注释取消ITEM_PIPELINES
        if self.pg <3:
            self.pg += 1
            url = 'https://bj.lianjia.com/ershoufang/pg{}/'
            # 把url交给secheduer入队列
            # response会自动传给 callback 回调的 parse()函数
            #Scrapy.request()向url发起请求，并将响应结果交给回调的解析函数
            yield scrapy.Request(url=url.format(self.pg),callback=self.parse())
        pass

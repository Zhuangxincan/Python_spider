import scrapy
# from Lianjiahouse.items import LianjiahouseItem 该方法导入失败
# from ..items import LianjiahouseItem #使用该方法可行（该方法报错attempted relative import with no known parent package）
from Lianjiahouse.items import LianjiahouseItem
# 通过将爬虫项目文件设置为源目录，引入items。（右键-> 将目录标记为 -> 源 根）

class LianjiaSpider(scrapy.Spider):
    # name 指定爬虫文件名字
    name = 'lianjia'
    allowed_domains = ['bj.lianjia.com','https://bj.lianjia.com/ershoufang/pg2/']# 网站域名
    start_urls = ['https://bj.lianjia.com/ershoufang/pg1/']# 第一个要抓取的url
    pg = 1
    def parse(self, response):
        # 基准xpath，匹配电影信息的dd节点对象列表
        h_list = response.xpath('//ul[@class="sellListContent"]/li[@class="clear LOGVIEWDATA LOGCLICKDATA"]')
        # 给items.py 中的类：Maoyan100Item（）实例化
        # print(h_list)

        item = LianjiahouseItem()
        # 测试字段可行性
        # for h in h_list:
        #     item['name'] = h.xpath('.//a[@data-el="region"]/text()').get()
        #     item['model'] = h.xpath('.//div[@class="houseInfo"]/text()').get().split('|')[0].strip()
        #     item['area'] = h.xpath('.//div[@class="houseInfo"]/text()').get().split('|')[1].strip()
        #     print(item)
        for h in h_list:
            item['name'] = h.xpath('.//a[@data-el="region"]/text()').get()
            item['model'] = h.xpath('.//div[@class="houseInfo"]/text()').get().split('|')[0].strip()
            item['area'] = h.xpath('.//div[@class="houseInfo"]/text()').get().split('|')[1].strip()
            item['direction'] = h.xpath('.//div[@class="houseInfo"]/text()').get().split('|')[2].strip()
            item['perfect'] = h.xpath('.//div[@class="houseInfo"]/text()').get().split('|')[3].strip()
            item['floor'] = h.xpath('.//div[@class="houseInfo"]/text()').get().split('|')[4].strip()
            item['address'] = h.xpath('.//div[@class="positionInfo"]/a/text()').get().strip()
            item['total_list'] =h.xpath('.//div[@class="totalPrice totalPrice2"]/span/text()').get().strip()
            item['price_list'] = h.xpath('.//div[@class="unitPrice"]/span/text()').get().strip()
            yield item
            # 需要setting.py中的注释取消ITEM_PIPELINES

        if self.pg < 3:
            self.pg += 1
            # 方案1失败,使用.format()拼接
            # url = 'https://bj.lianjia.com/ershoufang/pg{}/'
            # url1 = url.format(self.pg)
            # print(url1)
            # # 把url交给secheduer入队列
            # # response会自动传给 callback 回调的 parse()函数
            #     #Scrapy.request()向url发起请求，并将响应结果交给回调的解析函数
            # yield scrapy.Request(url=url1, callback=self.parse(), dont_filter=True) #无法正确回滚
            # yield scrapy.Request(url=url.format(self.pg), callback=self.parse())
            # yield scrapy.Request(url=response.urljoin(url1),callback=self.parse())#无法正确回滚
            # 疑似被过滤了
            # 解决方法：1.allowed_domains 中加入url 2.scrapy.Request(）设置 dont_filter=True 两种方法都失败了
            #方案2 直接拼接
            url = 'https://bj.lianjia.com/ershoufang/pg' + str(self.pg) +'/'
            print(url)
            yield scrapy.Request(url = url,callback=self.parse)

            # 问题原因为 callback=self.parse() 错误，callback=self.parse 正确

        pass

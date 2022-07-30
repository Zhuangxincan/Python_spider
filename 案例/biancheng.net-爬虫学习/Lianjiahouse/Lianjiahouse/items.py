# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiahouseItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    model = scrapy.Field()
    area = scrapy.Field()
    direction = scrapy.Field()
    perfect = scrapy.Field()
    floor = scrapy.Field()
    address = scrapy.Field()
    total_list = scrapy.Field()
    price_list = scrapy.Field()
    pass

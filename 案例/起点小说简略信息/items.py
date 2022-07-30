import scrapy

class QidianxiaoshuoItem(scrapy.Item):
    #定义fields
    book_name = scrapy.Field()
    author = scrapy.Field()
    intro = scrapy.Field()
    word_num = scrapy.Field()
    recomment_all = scrapy.Field()
    recomment_week = scrapy.Field()
from scrapy import cmdline
#执行爬虫文件 -o 指定输出文件的格式

cmdline.execute('scrapy crawl lianjia -o lianjia.csv'.split())
#导出CSV文件乱码，应该跟格式有关，暂时未做调整和整理
#配置文件中编码改为gbk
# FEED_EXPORT_ENCODING='GBK'


# 正常调用spider方法
# cmdline.execute('scrapy crawl lianjia'.split())
#执行项目，并且将数据存csv文件格式
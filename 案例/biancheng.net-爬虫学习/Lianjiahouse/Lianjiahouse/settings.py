# Scrapy settings for Lianjiahouse project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Lianjiahouse'

SPIDER_MODULES = ['Lianjiahouse.spiders']
NEWSPIDER_MODULE = 'Lianjiahouse.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'Lianjiahouse (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#设置下载器延迟时间，秒为单位
DOWNLOAD_DELAY = 2
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
   'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'Lianjiahouse.middlewares.LianjiahouseSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'Lianjiahouse.middlewares.LianjiahouseDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'Lianjiahouse.pipelines.LianjiahousePipeline': 300,
# 执行数据存储mysql
   'Lianjiahouse.pipelines.LianjiahouseMysqlPipeline': 200
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

#设置日志级别： DEBUG < INFO < WARNING < ERROR < CRITICAL
#日志需要自己添加，配置文件中没有，在空白处添加即可
LOG_LEVEL='DEBUG'
#定义日志输出文件
LOG_FILE='lianjia.log'
#设置导出数据的编码格式
# FEED_EXPORT_ENCODING='utf-8'
FEED_EXPORT_ENCODING='GBK'

#在配置文件末尾添加mysql常用变量
MYSQL_HOST='localhost'
MYSQL_USER='root'
MYSQL_PWD='123456'
MYSQL_DB='lianjia'
MYSQL_CHARSET='utf8'


# #设置 robots.txt 为False
# ROBOTSTXT_OBEY = False
# #设置日志级别： DEBUG < INFO < WARNING < ERROR < CRITICAL
# #日志需要自己添加，配置文件中没有，在空白处添加即可
# LOG_LEVEL='DEBUG'
# #定义日志输出文件
# LOG_FILE='maoyan.log'
# #设置导出数据的编码格式
# FEED_EXPORT_ENCODING='utf-8'
# #设置下载器延迟时间，秒为单位
# DOWNLOAD_DELAY = 1
# #请求头，添加useragent等信息
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#   'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'
# }
# #激活管道，并添加数据存放mysql的类，200为执行优先级
# ITEM_PIPELINES = {
#    'Maoyan100.pipelines.Maoyan100Pipeline': 300,
#     # 执行数据存储mysql
#    'Maoyan100.pipelines.Maoyan100MysqlPipeline': 200
#
# }
# #在配置文件末尾添加mysql常用变量
# MYSQL_HOST='localhost'
# MYSQL_USER='root'
# MYSQL_PWD='123456'
# MYSQL_DB='maoyandb'
# MYSQL_CHARSET='utf8'
import scrapy


# 常用指令
# 命令	格式	说明
# startproject	scrapy startproject <项目名>	创建一个新项目。
# genspider 	scrapy genspider <爬虫文件名> <域名>	新建爬虫文件。
# runspider	    scrapy runspider <爬虫文件>	运行一个爬虫文件，不需要创建项目。
# crawl	        scrapy crawl <spidername>	运行一个爬虫项目，必须要创建项目。
# list	        scrapy list	                列出项目中所有爬虫文件。
# view	        scrapy view <url地址>	    从浏览器中打开 url 地址。
# shell	        csrapy shell <url地址>	    命令行交互模式。
# settings	    scrapy settings 	        查看当前项目的配置信息。


# Scrapy 五大组件
# 名称	            作用说明
# Engine(引擎)	    整个 Scrapy 框架的核心，主要负责数据和信号在不同模块间传递。
# Scheduler(调度器)	用来维护引擎发送过来的 request 请求队列。
# Downloader(下载器)	接收引擎发送过来的 request 请求，并生成请求的响应对象，将响应结果返回给引擎。
# Spider(爬虫程序)	处理引擎发送过来的 response， 主要用来解析、提取数据和获取需要跟进的二级URL，然后将这些数据交回给引擎。
# Pipeline(项目管道)	用实现数据存储，对引擎发送过来的数据进一步处理，比如存  MySQL 数据库等

# 在整个执行过程中，还涉及到两个 middlewares 中间件，
# 分别是下载器中间件（Downloader Middlewares）和蜘蛛中间件（Spider Middlewares），
# 它们分别承担着不同的作用：
# 下载器中间件，位于引擎和下载器之间，主要用来包装 request 请求头，比如 UersAgent、Cookies 和代理 IP 等
# 蜘蛛中间件，位于引擎与爬虫文件之间，它主要用来修改响应对象的属性
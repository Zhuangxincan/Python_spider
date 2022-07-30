from threading import Thread
#线程创建、启动、回收
# t = Thread(target='') #创建线程对象
# t.start()#创建并启动线程
# t.join() #阻塞等待回收线程
#
# #创建多线程
# t_list = []
# for i in range(5):
#     t = Thread(target='')
#     t_list.append(t)
#     t.start()
#
# for t in t_list:
#     t.join()

# 在处理线程的过程中要时刻注意线程的同步问题，即多个线程不能操作同一个数据，
# 否则会造成数据的不确定性。通过 threading 模块的 Lock 对象能够保证数据的正确性。
from threading import Lock
# lock = Lock()
# # 获取锁
# lock.acquire()
# wirter.writerows("线程锁问题解决")
# # 释放锁
# lock.release()

# Queue队列模型
from queue import Queue
# q = Queue()#创建队列对象
# q.put(url) #向队列添加爬取一个URL链接
# q.get() # 获取一个url，当队列为空时，阻塞
# q.empty() # 判断队列是否为空，True/False

import requests
import time
import random
from fake_useragent import UserAgent
from lxml import etree
import csv
import json
# ----小米页面已取消类型标签----
class XiaomiSpider(object):
    def __init__(self):
        self.url = 'http://app.mi.com/categotyAllListApi?page={}&categoryId={}&pageSize=30'
        # 存放所有URL地址的队列
        self.q = Queue()
        self.i = 0
        # 存放所有类型id的空列表
        self.id_list = []
        # 打开文件
        self.f = open('XiaomiShangcheng.csv','a',encoding='utf-8')
        self.writer = csv.writer(self.f)
        #创建锁
        self.lock = Lock()

    def get_cateid(self):
        #请求
        url =  'http://app.mi.com/'
        headers = {'User-Agent':UserAgent().random}
        html = requests.get(url=url,headers=headers).text
        #解析
        parse_html = etree.HTML(html)
        #获取分类
        xpath_bds = '//ul[@class="category-list"]/li'
        li_list = parse_html.xpath(xpath_bds)
        for li in li_list:
            type_name = li.xpath('./a/text()')[0]
            type_id = li.xpath('./a/@href')[0].split('/')[-1]
            #计算每个类型的页数
            pages = self.get_pages(type_id)
            #往列表添加二元组
            self.id_list.append((type_id,pages))

        #入队列
        self.url_in()

    # 获取count的值并计算页数
    def get_pages(self,type_id):
        # 获取count的值，即app总数
        url = self.url.format(0,type_id)
        html = requests.get(url=url,headers={'User-Agent':UserAgent().random}).json()
        count = html['count']
        pages = int(count)//30 +1
        return pages

    # url入队函数，拼接url，并将url加入队列
    def url_in(self):
        for id in self.id_list:
            # id格式：('4',pages)
            for page in range(1,id[1]+1):
                url = self.url.format(page,id[0])
                # 把URL地址入队列
                self.q.put(url)

    # 线程事件函数: get() - 请求 - 解析 - 处理数据, 三步骤
    def get_date(self):
        while True:
            # 判断队列不为空则执行，否则终止
            if not self.q.empty():
                url = self.q.get()
                headers = {'User-Agent': UserAgent().random}
                html = requests.get(url=url, headers=headers)
                res_html= html.content.decode(encoding='utf-8')
                html = json.loads(res_html)
                self.parse_html(html)
            else:
                break

    # 解析函数
    def parse_html(self,html):
        # 写入到csv文件
        app_list = []
        for app in html['data']:
            # app名称 + 分类 + 详情链接
            name = app['displayName']
            link = 'http://app.mi.com/details?id=' + app['packageName']
            type_name = app['level1CategoryName']
            print(name,type_name)
            self.i += i
        # 向CSV文件中写入数据
        self.lock.acquire()
        self.writer.writerow(app_list)
        self.lock.release()

    def main(self):
        #URL入队列
        self.get_cateid()
        t_list = []
        #创建多线程
        for i in range(1):
            t = Thread(target=self.get_date())
            t_list.append(t)
            #启动线程
            t.start()

        for t in t_list:
            # 回收线程
            t.join()
        self.f.close()
        print('数量：',self.i)

if __name__ == '__main__':
    start = time.time()
    spider = XiaomiSpider()
    spider.main()
    end = time.time()
    print('执行时间:%.1f' % (end-start))
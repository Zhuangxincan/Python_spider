#coding = gbk
from urllib import request
import re
import time
import random
from ua_info import ua_list
import pymysql

# 理论上需要先创建数据库
# # 1. 连接到mysql数据库
# mysql -h127.0.0.1 -uroot -p123456
# # 2. 建库
# create database maoyandb charset utf8;
# # 3. 切换数据库
# use maoyandb;
# # 4. 创建数据表
# create table filmtab(
# name varchar(100),
# star varchar(400),
# time varchar(30)
# );

class MaoyanSpider(object):
    def __init__(self):
        #初始化属性对象
        self.url = 'https://maoyan.com/board/4?offset={}'
        #数据库连接对象
        self.db = pymysql.connect('localhost','root','123456','maoyandb',charset='utf8')
        #创建游标对象
        self.cursor = self.db.cursor()

    def get_html(self,url):
        headers = {'User-Agent':random.choice(ua_list)}
        req = request.Request(url = url ,headers= headers)
        res = request.urlopen(req)
        html = res.read().decode()
        #直接解析
        self.parse_html(html)

    def parese_html(self,html):
        re_bds = '<div class="movie-item-info">.*?title="(.*?)".*?<p class="star">(.*?)</p>.*?class="releasetime">(.*?)</p>'
        pattern = re.compile(re_bds, re.S)
        r_list = pattern.findall(html)
        self.save_html(r_list)

    def save_html(self,r_list):
        L = []
        sql = 'insert into filmtab values(%s,%s,%s)'
        #整理数据
        for r in r_list:
            t= (
                r[0].strip(),
                r[1].strip()[3:],
                r[2].strip()[3:15]
            )
            L.append(t)
            print(L)
        #插入数据库，一次插入多条 L:[(),(),()]
        try:
            self.cursor.executemany(sql,L)
            #将数据提交给数据库
            self.db.commit()
        except:
            #发生错误则回滚
            self.db.rollback()

    def run(self):
        for offest in range(0,11,10):
            url = self.url.format(offest)
            self.get_html(url)
            time.sleep(random.uniform(1,3))

            #断开游标与数据库连接
            self.cursor.close()
            self.db.close()

if __name__ == '__main__':
    #记录开始时间
    start = time.time()
    spider = MaoyanSpider()
    spider.run()
    #记录结束时间
    end = time.time()
    print('执行时间：%.2f'%(end-start))

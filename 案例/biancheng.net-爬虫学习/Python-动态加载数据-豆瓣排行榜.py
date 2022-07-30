#coding:utf8
import requests
import time
import random
import re
import json
from ua_info import ua_list

class DoubanSpider(object):
    def __init__(self):
        self.url = 'https://movie.douban.com/j/chart/top_list?'
        self.i = 0

    #获取随机headers
    def get_headers(self):
        headers = {'User-Agent':random.choice(ua_list)}
        return headers

    #获取页面
    def get_page(self,params):
        #将json转换为Python数据类型，并返回
        html = requests.get(url=self.url,headers=self.get_headers(),params = params).text
        #将html写成字典
        html = json.loads(html)
        self.parse_page(html)

    #解析并保存数据
    def parse_page(self,html):
        item = {}
        # html列表类型： [{电影1},{电影2},{电影3}...]
        for one in html:
            #名称+评分
            item['name'] = one['title'].strip()
            item['score'] = float(one['score'])
            print(item)
            self.i += 1

    #获取电影总数
    def total_number(self,type_number):
        #F12抓包抓到的地址，type表示电影类型
        url =  'https://movie.douban.com/j/chart/top_list_count?type={}&interval_id=100%3A90'.format(type_number)
        headers = self.get_headers()
        html = requests.get(url=url,headers=headers).json()
        total = int(html['total'])
        return total

    #获取所有电影类型和对应type值
    def get_all_type_films(self):
        #获取类型与类型码
        url = 'https://movie.douban.com/chart'
        headers = self.get_headers()
        html = requests.get(url=url,headers=headers).text
        re_bds = r'<a href=.*?type_name=(.*?)&type=(.*?)&.*?</a>'
        pattern = re.compile(re_bds,re.S)
        r_list = pattern.findall(html)
        #存放类型和类型码的字典
        type_dict = {}
        #定义一个选择电影类型的菜单
        menu = ''
        for r in r_list:
            type_dict[r[0].strip()] = r[1].strip()
            #获取input菜单，显示所有电影类型
            menu += r[0].strip() + '|'
        return type_dict,menu

    def main(self):
        #获取type值
        type_dict,menu = self.get_all_type_films()
        menu = menu +'\n 输入你想了解的电影类型：'
        name = input(menu)
        type_number = type_dict[name]
        #获取电影总数
        total = self.total_number(type_number)
        for start in range(0,(total+1),20):
            #构建查询参数
            params = {
                'type': type_number,
                'interval_id': '100:90',
                'action': '',
                'start': str(start),
                'limit': '20'
            }
            #调用解析函数，传递参数
            self.get_page(params)
            #随机睡眠
            time.sleep(random.randint(1,3))
        print('电影总数量：%d部'%self.i)

if __name__ == '__main__':
    spider = DoubanSpider()
    spider.main()
from selenium import webdriver
# 驱动包定位
from selenium.webdriver.firefox.service import Service
# by方法导入
from selenium.webdriver.common.by import By

from time import sleep

import pymongo

class JdSpider(object):
    def __init__(self):
        self.url = 'https:www.jd.com/'
        self.options = webdriver.FirefoxOptions()#无浏览器模式/无头模式
        self.service = Service(r'D:\软件\Python\Scripts\geckodriver.exe')#浏览器驱动包位置
        self.options.add_argument('--headless')
        self.browser = webdriver.Firefox(service=self.service,options=self.options)
        self.i = 0 #初始化计数项，共多少件商品

        # 输入地址+输入商品+点击按钮，切记这里元素节点是京东首页的输入栏、搜索按钮
    def get_html(self):
        self.browser.get(self.url)
        self.browser.find_element(By.XPATH,'//*[@id="key"]').send_keys('python书籍')
        self.browser.find_element(By.XPATH,"//*[@class='form']/button").click()

    # 把进度条件拉倒最底部+提取商品信息
    def get_data(self):
        # 执行js语句，将滚动条拉到底部
        self.browser.execute_script(
            'window.scrollTo(0,document.body.scrollHeight)'
        )
        # 给页面元素加载时预留时间
        sleep(2)
        # 用 xpath 提取每页中所有商品，最终形成一个大列表
        # find_elements 注意此处会找到多个 “li” 所以不能用find_element
        li_list = self.browser.find_elements(By.XPATH,'//*[@id="J_goodsList"]/ul/li')
        for li in li_list:
            #构建空字典
            item = {}
            item['name'] = li.find_element(By.XPATH,'.//div[@class="p-name"]/a/em').text.strip()
            item['price'] = li.find_element(By.XPATH,'.//div[@class="p-price"]/strong/i').text.strip()
            item['count'] = li.find_element(By.XPATH,'.//div[@class="p-commit"]/strong').text.strip()
            item['shop'] = li.find_element(By.XPATH,'.//div[@class="p-shopnum"]').text.strip()
            print(item)
            self.i += 1

    def run(self):
        #搜索想要抓取商品的页面
        self.get_html()
        #循环执行点击”下一页“操作
        while True:
            #获取每页抓取数据
            self.get_data()
            #判断是否最后一页
            if self.browser.page_source.find('pn-next disabled') == -1:
                self.browser.find_element(By.CLASS_NAME,'pn-next').click()
                # 预留元素加载时间
                sleep(1)
            else:
                print('数量', self.i)
                break
        self.browser.quit()
if __name__ == '__main__':
    spider = JdSpider()
    spider.run()
        # broswer.quit()
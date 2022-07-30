from urllib import request,parse
import time
import random
#实用自定义ua池
from ua_info import ua_list

#定义一个爬虫类
class TiebaSpider(object):
    #初始化URL属性
    def __init__(self):
        self.url = 'http://tieba.baidu.com/f?{}'

    # 1请求函数，得到页面，三步
    def get_html(self,url):
        req = request.Request(url = url,headers={'User-Agent':random.choice(ua_list)})
        res = request.urlopen(req)
        #windows会存在乱码问题，需要使用 gbk解码，并使用ignore忽略不能处理的字节
        #linux不会存在上述问题，可以直接使用decode('utf-8')解码
        html = res.read().decode('gbk','ignore')
        return html

    # 2解析函数，此处代码暂时省略，未介绍解析模块
    def parse_html(self):
        pass

    # 3保存文件
    def save_html(self,filename,html):
        with open(filename,'w') as f:
            f.write(html)

    # 4入口函数
    def run(self):
        name = input('请输入贴吧名：')
        begin = int(input('请输入起始页:'))
        stop = int(input('请输入结束页：'))
        #+1操作保证能取到整数
        for page in range(begin,stop+1):
            pn = (page-1)*50
            params={
                'kw':name,
                'pn':str(pn)
            }
            #拼接URL地址
            params = parse.urlencode(params)
            url = self.url.format(params)
            #发送请求
            html = self.get_html(url)
            #定义路劲
            filename = '{}-{}页.html'.format(name,page)
            self.save_html(filename,html)
            #提示
            print('第%d页抓取成功'%page)
            #每爬取一个页面随机休息1-2秒时间
            time.sleep(random.randint(1,2))
#以脚本形式启动爬虫
if __name__ == '__main__':
    start = time.time()
    #实例化一个对象spider
    spider = TiebaSpider()
    #调用入口函数
    spider.run()
    end = time.time()
    #查看程序执行时间
    #执行时间
    print('执行时间：%.2f'%(end-start))
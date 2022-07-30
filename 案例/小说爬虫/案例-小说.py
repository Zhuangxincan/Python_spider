
import requests
from bs4 import BeautifulSoup
import re
import time
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36'

}
f = open(r'/案例/小说爬虫/doupo.txt', 'a+') #新建文档，追加

def get_info(url):                                          #定义获取信息的函数
    res = requests.get(url,headers=headers)
    if res.status_code == 200:                      #判断请求码是否正常
        contents = re.findall('<p>(.*?)<p>',res.content.decode('utf-8'),re.S)
        for content in contents:
            f.write(content+'\n')                   #文本写入
    else:
        pass                                        #获取错误跳过
if  __name__ == '__main__':
    urls = ['http://www.doupoxs.com/doupocangqiong/{}.html'.format(str(i)) for i in range(2,4)]
    for url in urls:
        get_info(url) #循环调用get_info 函数
        time.sleep(1) #睡眠1秒
f.close()

# res = requests.get('http://bj.xiaozhu.com/',headers= headers)
# soup = BeautifulSoup(res.text,'html.parser')
# print(soup.prettify())




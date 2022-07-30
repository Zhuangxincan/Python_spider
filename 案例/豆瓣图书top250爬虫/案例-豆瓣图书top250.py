import requests
from lxml import html
et = html.etree
import csv
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36'
}
#创建CSV
fr = open('/案例/豆瓣图书top250爬虫/doubanbook.csv', 'wt', newline='', encoding='utf-8')
writer = csv.writer(fr)
#写入header
writer.writerow(('name','url','author','publisher','date','price','rate','comment'))
#构造URL
urls = ['https://book.douban.com/top250?star={}'.format(str(i)) for i in range(0,250,50)]

for url in urls:
    html = requests.get(url,headers=headers)
    selector = et.HTML(html.text)
    # // *[ @ id = "content"] / h1
    #取最大标签，以此循环
    # 循环URL，根据“先抓大后抓小，寻找循环点”的原则，找到每条信息的标签
    infos = selector.xpath('//tr[@class="item"]')
    for info in infos:
        name = info.xpath('td/div/a/@title')[0]
        url = info.xpath('td/div/a/@href')[0]
        book_infos = info.xpath('td/p/text()')[0]
        author = book_infos.split('/')[0]
        publisher = book_infos.split('/')[-3]
        date = book_infos.split('/')[-2]
        price = book_infos.split('/')[-1]
        rate = info.xpath('td/div/span[2]/text()')[0]
        comments = info.xpath('td/p/span/text()')
        comment = comments[0] if len(comments) != 0 else '空'
        #写入
        writer.writerow((name,url,author,publisher,date,price,rate,comment))
#关闭CSV文件
fr.close()

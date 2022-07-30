#导入库文件
import xlwt
import requests
from lxml import html
et = html.etree
import  time

#初始化列表，存入爬虫数据
all_info_list = []

#定义获取爬虫信息的函数

def get_info(url):
    html = requests.get(url)
    # html.encoding = 'gbk'
    selector = et.HTML(html.text)
    infos = selector.xpath('//ul[@class="all-img-list cf"]/li')
    for info in infos:
        title = info.xpath('div[2]/h2/a/text()')[0]
        author = info.xpath('div[2]/p[1]/a[1]/text()')[0]
        style_1 = info.xpath('div[2]/p[1]/a[2]/text()')[0]
        style_2 = info.xpath('div[2]/p[1]/a[3]/text()')[0]
        style = style_1+'*'+style_2
        complete = info.xpath('div[2]/p[1]/span/text()')[0]
        # strip()函数将从原始字符串的开头和结尾删除给定的字符。
        introduce = info.xpath('div[2]/p[2]/text()')[0].strip()
        word = info.xpath('div[2]/p[3]/span/text()')[0].strip('万字')
        # word = word.encode('iso-8859-1').decode('gbk')
        info_list = [title,author,style,complete,introduce,word]
        #数据存入列表
        all_info_list.append(info_list)
    time.sleep(1)
    # #测试网页编码
    # html = requests.get('https://www.qidian.com/all/',headers=headers)
    # print(html.encoding)
if __name__ == '__main__':
    urls = ['https://www.qidian.com/all/page{}'.format(str(i)) for i in range(1,2)]
    # 模拟URL翻页
    for url in urls:
        get_info(url)
    #定义表头
    header = ['title','author','style','complete','introduce','word']
    #创建工作簿
    book = xlwt.Workbook(encoding='urf-8')
    #创建Sheet页
    sheet = book.add_sheet('起点中文20页简略信息')
    #写入表头
    for h in range(len(header)):
        sheet.write(0,h,header[h])
    i = 1
    #写入爬虫数据
    for list in all_info_list:
        j = 0
        for date in list:
            sheet.write(i,j,date)
            j += 1
        i += 1
#保存
book.save('xiaoshuo.xls')

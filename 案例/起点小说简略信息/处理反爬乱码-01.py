#导入库文件
import re
from io import BytesIO, StringIO

from fontTools.ttLib import TTFont
import xlwt
import requests
from lxml import html
et = html.etree
import  time

all_info_list = []

def get_info(url):
    html = requests.get(url)
    selector = et.HTML(html.text)
    source = html.text
    #1.获取字体文件字典
    #1.1获取文件字体并且以ttf结尾，每次不断变化，采用正则表达式
    url_ttf_pattern = re.compile('<style>(.*?)</style>',re.S)
    fonturl = re.findall(url_ttf_pattern,source)[0]
    font_url = re.search('woff.*?url.*?\'(.+?)\'.*?truetype',fonturl).group(1)
    # print(font_url)
    #1.2下载文件，转化为字典形式 cmap
    ziti = requests.get(font_url)
    font = TTFont(BytesIO(ziti.content))
    cmap = font['cmap'].getBestCmap()
    font.close()
    # print(cmap)
    #2建立英文字母和阿拉伯数字映射字典 d
    d = {'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'period':'.','zero':0}
    #2.1获取乱码数字无法通过xpath获取，需要通过正则表达式匹配
    infos = selector.xpath('//ul[@class="all-img-list cf"]/li')
    num_list = re.findall('</style><span.*?>(.*?)</span>',source)
    i = 0
    for info in infos:
        title = info.xpath('div[2]/h2/a/text()')[0]
        author = info.xpath('div[2]/p[1]/a[1]/text()')[0]
        style_1 = info.xpath('div[2]/p[1]/a[2]/text()')[0]
        style_2 = info.xpath('div[2]/p[1]/a[3]/text()')[0]
        style = style_1 + '·' + style_2
        complete = info.xpath('div[2]/p[1]/span/text()')[0]
        # strip()函数将从原始字符串的开头和结尾删除给定的字符。
        introduce = info.xpath('div[2]/p[2]/text()')[0].strip()
        #xpath无法获取反爬字符
        # word = info.xpath('div[2]/p[3]/span/text()')[0].strip('万字')
        #通过cmap和d字典将乱码转化为数字，并组合成字符串
        #3.1一个乱码对应一个 &# 妇保对应一个数或“.”,通过“;”连接。以“;”才能使用字典对应
        num = num_list[i].split(";")
        i+= 1
        #3.2最后一个元素存在换行，换行需要pop列表
        num.pop(-1)
        #3.3利用 &# 符号列表使用 cmap和d 字典将乱码转换为阿拉伯数字
        word_list = []
        for n in num:
            n = d[cmap[int(n[2:])]]
            word_list.append(n)
        #4将转化后的阿拉伯数字列表组成字符串
        word_list1 = [str(j) for j in word_list]
        word = ''.join(word_list1)+'万字'
        # print(word)
        info_list = [title, author, style, complete, introduce, word]
        # 数据存入列表
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
book.save('fanpa-01.xls')

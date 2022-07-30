# Tag：标签类，HTML 文档中所有的标签都可以看做 Tag 对象。
# NavigableString：字符串类，指的是标签中的文本内容，使用 text、string、strings 来获取文本内容。
# BeautifulSoup：表示一个 HTML 文档的全部内容，您可以把它当作一个人特殊的 Tag 对象。
# Comment：表示 HTML 文档中的注释内容以及特殊字符串，它是一个特殊的 NavigableString。

html_doc = """
<html><head><title>"c语言中文网"</title></head>
<body>
<p class="title"><b>c.biancheng.net</b></p>
<p class="website">一个学习编程的网站</p>
<a href="http://c.biancheng.net/python/" id="link1">python教程</a>
<a href="http://c.biancheng.net/c/" id="link2">c语言教程</a>
<a href="http://c.biancheng.net/django/" id="link3">django教程</a>
<p class="vip">加入我们阅读所有教程</p>
<a href="http://vip.biancheng.net/?from=index" id="link4">成为vip</a>
<p class="introduce">介绍:
<a href="http://c.biancheng.net/view/8066.html" id="link5">关于网站</a>
<a href="http://c.biancheng.net/view/8092.html" id="link6">关于站长</a>
</p>
"""
from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc,'html.parser')
# 打开外部文档
# soup = BeautifulSoup(open('html_doc.html', encoding='utf8'), 'lxml')
#prettify()用于格式化输出html/xml文档
# print(soup.prettify())

# soup = BeautifulSoup('<p class="Web site url"><b>c.biancheng.net</b></p>', 'html.parser')
# #获取整个p标签的html代码
# print(soup.p)
# #获取b标签
# print(soup.p.b)
# # #获取p标签内容，使用NavigableString类中的string、text、get_text()
# print(soup.p.text)
# # #返回一个字典，里面是多有属性和值
# print(soup.p.attrs)
# # #查看返回的数据类型
# print(type(soup.p))
# # #根据属性，获取标签的属性值，返回值为列表
# print(soup.p['class'])
# # #给class属性赋值,此时属性值由列表转换为字符串
# soup.p['class']=['Web','Site']
# print(soup.p)
#
# soup = BeautifulSoup(html_doc,'html.parser')
# body_tag= soup.body
# print(body_tag)
#以列表的形式输出，所有子节点
# print(body_tag.contents) # 按照标签 分割，中间插入换行符
# for child in body_tag.children:
#     print(child)


# find_all()与find()
# find_all( name , attrs , recursive , text , limit )
# name：查找所有名字为 name 的 tag 标签，字符串对象会被自动忽略。
# attrs：按照属性名和属性值搜索 tag 标签，注意由于 class 是 Python 的关键字吗，所以要使用 "class_"。
# recursive：find_all() 会搜索 tag 的所有子孙节点，设置 recursive=False 可以只搜索 tag 的直接子节点。
# text：用来搜文档中的字符串内容，该参数可以接受字符串 、正则表达式 、列表、True。
# limit：由于 find_all() 会返回所有的搜索结果，这样会影响执行效率，通过 limit 参数可以限制返回结果的数量。
import re
# #查找所有的a标签并返回,列表
# print(soup.find_all('a'))
# #查找前2条a标签并返回,只返回2条a标签
# print(soup.find_all('a',limit=2))

# 按照标签属性以及属性值查找HTML文档
print('\n',soup.find_all('p',class_ = 'website'))
# print('\n',soup.find_all(id = 'link4'))

# 正则表达式、列表，以及 True 也可以当做过滤条件
#列表行书查找tag标签
# print('查找tag\n',soup.find_all(['b','a']))

# 正则表达式匹配id属性值
# print('正则表达式\n',soup.find_all('a',id = re.compile(r'.\d')))
# print('正则表达式2\n',soup.find_all(id = True))

#True可以匹配任何值，下面代码会查找所有tag，并返回相应的tag名称
# for tag in soup.find_all(True):
#     print(tag.name,end=" ")

# 输出所有以b开始的tag 标签
# for tag in soup.find_all(re.compile(r'^b')):
#     print("\n",tag.name)

#简化前
# print(soup.find_all("a"))
#简化后
# print(soup("a"))

# find() 仅返回一个符合条件的结果
# 使用 find() 时，如果没有找到查询标签会返回 None，而 find_all() 方法返回空列表

#简化写法
# print(soup.head.title)
#上面代码等价于
# print(soup.find("head").find("title"))

# CSS选择器
#根据元素标签查找
# print(soup.select('title'))
#根据属性选择器查找
# print(soup.select('a[href]'))
# print(soup.select('p[class]'))
#根据类查找,"." 作用是替代 =前的标签
# print(soup.select('.vip'))
#后代节点查找
# print(soup.select('html head title'))
#查找兄弟节点 p后面第一个a,
# print(soup.select('p + a'))
#根据id选择p标签的兄弟节点
# print(soup.select('p ~ #link2'))
#nth-of-type(n)选择器，用于匹配同类型中第n个同级兄弟元素，从第一个P之后
# print(soup.select('p ~ a:nth-of-type(4)'))
#查找子节点
# print(soup.select('p > a'))
# print(soup.select('.introduce > #link5'))

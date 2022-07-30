#导入parse模块
from urllib import  parse

# ---编码-----
#构建查询字符串字典
query_string = {
'wd':'爬虫'
}
# 调用parse模块的urlencode（）进行编码
result = parse.urlencode(query_string)
# 使用format函数格式化字符串，拼接URL
url = 'http://www.baidu.com/s?{}'.format(result)
print(url)

#调用quote(string)方法实现编码
#注意url书写格式的不同
url_quote = 'http://www.baidu.com/s?wd={}'
word = input('请输入要搜索的内容:')
#quote()只能对字符串进行编码
query_string_quote = parse.quote(word)
print(url.format(query_string_quote))

# -----解码-----
string = '%E7%88%AC%E8%99%AB'
result = parse.unquote(string)
print(result)

# -----URL地址拼接方式-----
# 1、字符串相加
baseurl = 'http://www.baidu.com/s?'
params='wd=%E7%88%AC%E8%99%AB'
url = baseurl + params

# 2、字符串格式化（占位符）
params='wd=%E7%88%AC%E8%99%AB'
url = 'http://www.baidu.com/s?%s'% params

# 3、format()方法
url = 'http://www.baidu.com/s?{}'
params='wd=%E7%88%AC%E8%99%AB'
url = url.format(params)
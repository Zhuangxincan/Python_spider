#导入请求和解码包
from urllib import request
from urllib import parse

#配置URL地址
url = 'http://www.baidu.com/s?wd={}'
#搜索内容
word = input('请输入搜索内容:')
params = parse.quote(word)
full_url = url.format(params)

#重构请求头,伪装为电脑请求
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36'
}
#创建请求
req = request.Request(url = full_url,headers= headers)
#获取响应对象
res = request.urlopen(req)
#获取响应对象内容
html = res.read().decode('utf-8')
#保存到本地文件夹
filename = word + '.html'
with open(filename,'w',encoding='utf-8') as f:
    f.write(html)

# ------函数式编程-------
#拼接URL地址
def get_url(word):
    url = 'http://www.baidu.com/s?{}'
    # 使用urlencode()编码
    params = parse.urlencode({'wd':word})
    url = url.format(params)
    return url

#发请求,保存本地文件
def request_url(url,filename):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36'
    }
    #请求对象+响应对象+提取内容
    req = request.Request(url=url,headers=headers)
    res = request.urlopen(req)
    html = res.read().decode('utf-8')
    #保存到本地
    with open(filename,'w',encoding='utf-8') as f:
        f.write(html)

#主程序入口
if __name__ == '__main__':
    word = input('请输入搜索内容:')
    url = get_url(word)
    filename = word + '.html'
    request_url(url,filename)


#导入模块
import urllib.request
#向网站发送get请求
response=urllib.request.urlopen('http://httpbin.org/get')
# 注意：httpbin.org 这个网站能测试 HTTP 请求和响应的各种信息，
# 比如 cookie、IP、headers 和登录验证等，且支持 GET、POST 等多种方法，对 Web 开发和测试很有帮助。
html = response.read().decode()
print(html)

from urllib import request
# 定义变量：URL 与 headers
url = 'http://httpbin.org/get' #向测试网站发送请求
#重构请求头，伪装成 Mac火狐浏览器访问，可以使用上表中任意浏览器的UA信息
headers = {
'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:65.0) Gecko/20100101 Firefox/65.0'}
# 1、创建请求对象，包装ua信息
req = request.Request(url=url,headers=headers)
# 2、发送请求，获取响应对象
res = request.urlopen(req)
# 3、提取响应内容
html = res.read().decode('utf-8')
print(html)

from fake_useragent import UserAgent
#实例化一个对象
ua = UserAgent()
# Error occurred during loading data. Trying to use cache server
# ua = UserAgent(use_cache_server=False)
# 随机获取一个ie浏览器ua
print(ua.ie)
print(ua.ie)
# 随机获取一个火狐浏览器ua
print(ua.firefox)
print(ua.firefox)
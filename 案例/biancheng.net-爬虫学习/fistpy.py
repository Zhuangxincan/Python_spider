#导入urllib
import urllib.request
# from urllib import request

#urlopen()向URL发请求，返回响应对象，URL必须完整
response = urllib.request.urlopen('http://www.baidu.com/')
print(response)

#提取响应内容
html = response.read().decode('utf-8')
#打印响应内容
# print(html)

# bytes = response.read() # read()返回结果为 bytes 数据类型
# string = response.read().decode() # decode()将字节串转换为 string 类型
# url = response.geturl() # 返回响应对象的URL地址
# code = response.getcode() # 返回请求时的HTTP响应码

#字符串转换为字节码
# string.encode("utf-8")
#字节码转换为字符串
# bytes.decode("utf-8")
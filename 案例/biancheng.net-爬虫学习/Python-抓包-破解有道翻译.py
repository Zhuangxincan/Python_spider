# var
# r = function(e)
# {
#     var
# t = n.md5(navigator.appVersion)
# , r = "" + (new Date).getTime()
# , i = r + parseInt(10 * Math.random(), 10);
# return {
#     ts: r,
#     bv: t,
#     salt: i,
#     sign: n.md5("fanyideskweb" + e + i + "Ygy_4c=r#e#4EX^NUGUc5")
# }
# };
# ------实现页面JS加密----------
# #lts 毫秒时间戳
# lst = str(int(time.time()*1000))
# #salt,lts +从0-9的随机数
# salt = lst+str(random.randint(0,9))
# word = input()
# #sign加密字符串
# string = "fanyideskweb"+ word + salt +"Tbh5E8=q6U3EXe+&L[4c@"
# s = md5()
# #md5的加密串必须为字节码
# s.update(string.encode())
# #16进制加密
# sign = s.hexdigest()

import random
import time
from hashlib import md5

import requests


class YoudaoSpider(object):
    def __init__(self):
    # -----反爬---
    # url一定要写抓包时抓到的POST请求的提交地址，但是还需要去掉 url中的“_o”，
    # “_o”这是一种url反爬策略，做了页面跳转，若直接访问会返回{"errorCode":50}
        self.url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
        }
    def get_lts_salt_sign(self,word):
        #获取lts时间戳，salt加密，sign加密签名
        lts = str(int(time.time()*1000))
        salt = lts +str(random.randint(0,9))
        string = "fanyideskweb"+ word + salt +"Ygy_4c=r#e#4EX^NUGUc5"
        s = md5()
        s.update(string.encode())
        sign = s.hexdigest()
        print(lts,salt,sign)
        return lts,salt,sign

    def attack_yd(self,word):
        lts,salt,sign = self.get_lts_salt_sign(word)
        #构建form 表单数据
        data = {
            'i':word,
            'from':'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': salt,
            'sign': sign,
            'lts': lts,
            'bv': 'f0819a82107e6150005e75ef5fddcc3b',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_REALTlME'
        }

        #使用requests.post()方法提交请求
        res = requests.post(
            url=self.url,
            data=data,
            headers=self.headers
        )

        #res.json() 将json格式的字符串转化为python数据类型
        # 客户端与服务器数据交互以json字符串传递，因此需要将它转换为python数据类型
        html = res.json()
        # 查看响应结果response  html:{"translateResult":[[{"tgt":"hello","src":"你好"}]],"errorCode":0,"type":"zh-CHS2en"}
        print(html)
        reslut = html['translateResult'][0][0]['tgt']
        print('翻译结果：',reslut)

    def run(self):
        try:
            word = input('请输入要翻译的单词：')
            self.attack_yd(word)
        except Exception as e:
            print('错误原因:',e)

if __name__ == '__main__':
    spider = YoudaoSpider()
    spider.run()
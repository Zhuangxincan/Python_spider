import json
import requests
import random
import hashlib
import urllib
import pandas as pd
#调用百度翻译API
#原始语言
fromlang = 'zh'
#目标语言#选择翻译类型为英文
tolang = 'en'
#平台ID
appid  = '20220524001226863'
#密钥
key = '2qgfsAQ2_rbMWD8xVCqt'
#随机码
salt = random.randint(3276, 65536)
#输入中文提示语
word =  input('请输入中文:')
#API链接'http://api.fanyi.baidu.com/api/trans/vip/translate'
url = 'http://api.fanyi.baidu.com/api/trans/vip/translate'

sign = appid + word + str(salt) + key
sign = hashlib.md5(sign.encode()).hexdigest()
myurl = url + '?appid=' + appid + '&q=' + urllib.parse.quote(word) + '&from=' + fromlang + \
        '&to=' + tolang + '&salt=' + str(salt) + '&sign=' + sign
# url = 'http://api.fanyi.baidu.com/api/trans/vip/translate?q=apple&from=en&to=zh&appid=20220524001226863&salt=1435660288&sign={}'.format(word)
res = requests.get(myurl)
#调用接口传入参数
json_data = json.loads(res.text)
print(json_data)
#dict字典
print(type(json_data))
#转换成DataFrame并取出翻译后的文本
df = pd.DataFrame(json_data)
print(df['trans_result'][0]['dst'])
# print(json_data['trans_result'][0]['dst'])
# {'from': 'zh', 'to': 'en', 'trans_result': [{'src': '我想拥抱全世界', 'dst': 'I want to embrace the world'}]}
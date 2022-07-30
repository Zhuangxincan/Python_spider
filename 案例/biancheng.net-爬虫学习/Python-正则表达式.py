import re

# ----------贪婪与非贪婪验证-------------
html = """
<div><p>www.biancheng.net</p></div>
<div><p>编程帮</p></div>
"""
#贪婪匹配,re.S可以匹配换行符
#创建正则表达式对象
pattern = re.compile('<div><p>.*</p></div>',re.S)
#匹配HTMLX元素，提取信息
re_list = pattern.findall(html)
print(re_list)

#非贪婪模式匹配，re.S可以匹配换行符
pattern = re.compile('<div><p>.*?</p></div>',re.S)
re_list = pattern.findall(html)
print(re_list)

# --------正则表达式分组--------
#正则表达式分组
website = "编程帮 www.biancheng.net"

#提取所有信息
#注意此时正则表达式的“.”需要转义，实用\.
pattern_1 = re.compile('\w+\s+\w+\.\w+\.\w+')
print(pattern_1.findall(website))

#提取匹配信息的第一项
pattern_2 = re.compile('(\w+)\s+\w+\.\w+\.\w+')
print(pattern_2.findall(website))

#有两个及以上的()则以元组形式显示
pattern_3=re.compile('(\w+)\s+(\w+\.\w+\.\w+)')
print(pattern_3.findall(website))

# --------模拟网页信息提取--------
html="""
<div class="movie-item-info">
<p class="name">
<a title="你好，李焕英">你好，李焕英</a>
</p>
<p class="star">
主演：贾玲,张小斐,沈腾
</p>    
</div>

<div class="movie-item-info">
<p class="name">
<a title="刺杀，小说家">刺杀，小说家</a>
</p>
<p class="star">
主演：雷佳音,杨幂,董子健,于和伟
</p>    
</div> 
"""
# 寻找HTML规律，书写正则表达式，使用正则表达式分组提取信息
pattern=re.compile(r'<div.*?<a title="(.*?)".*?star">(.*?)</p.*?div>',re.S)
r_list=pattern.findall(html)
print(r_list)
#整理格式并输出
if r_list:
    for r_info in r_list:
        print('影片名称：',r_info[0])
        print('影片主演：',r_info[1].strip())
        print(20*'*')
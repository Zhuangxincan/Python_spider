#测试代码
#导入 webdriver
import time
import random
from selenium import webdriver
#导入驱动配置包
from selenium.webdriver.firefox.service import Service

# 定位方法
from selenium.webdriver.common.by import By


# #一、 WebDriver定位常用方法
# # 请求url
# get(url)
# # 模拟键盘输入文本
# send_keys (value)
# # 清除已经输入的文本
# clear()：
# # 单击已经定位的元素
# click()：
# # 用于提交表单，比如百度搜索框内输入关键字之后的“回车” 操作
# submit()：
# #返回属性的属性值，返回元素的属性值，可以是id、name、type 或其他任意属性
# get_attribute(name)
# # 返回布尔值，检查元素是否用户可见，比如 display属性为hidden或者none
# is_displayed()
# find_element_by_id 方法舍弃使用driver.find_element(By.ID,'kw').send_keys(Keys.CONTROL,'a')
Serveice = Service(r'D:\软件\Python\Scripts\geckodriver.exe')
# driver = webdriver.Firefox(service = Serveice)
# driver.get("http://www.baidu.com")

# 1) 设置浏览器窗口大小、位置
# #参数数字为像素点
# driver.set_window_size(480, 800)
# #设置窗口位置
# driver.set_window_position(100,200)
# #同时设置窗口的大小和坐标
# driver.set_window_rect(450,300,100,200)
# #退出浏览器
# driver.quit()

# 2) 控制网页前进、后退、刷新页面
# # 访问C语言中文网首页
# first_url= 'http://c.biancheng.net'
# driver.get(first_url)
#
# #访问c语言教程
# second_url = 'http://c.biancheng.net/c/'
# driver.get(second_url)
#
# # 返回（后退）到c语言中文网首页
# driver.back()
#
# #前进到c语言教程页
# driver.forward()
#
# #刷新C语言教程页
# driver.refresh()
#
# #退出、关闭浏览器
# driver.quit()


# 二、WebDriver常用方法示例
# #模拟键盘，输出文本
# driver.find_element(By.ID, 'kw').send_keys('c语言中文网')
# #单击 ‘百度一下’
# # driver.find_element(By.ID,'su').click()
# driver.find_element(By.ID,'su').submit()
# #暂停三秒再继续
# time.sleep(3)
# # #退出、关闭浏览器
# driver.quit()

# 三、WebDriver常用属性示例
# # 获取HTML结构源码
# time.sleep(6)
# driver.page_source
#
# # #在源码中查找指定的字符串
# driver.page_source.find('百度')
#
# # 返回百度页面底部备案信息
# text = driver.find_element(By.ID,'bottom_layer').text
# print(text)
#
# # 获取输入框的尺寸
# size = driver.find_element(By.ID,'kw').size
# print(size)

# 四、Selenium事件处理
# 一些事件处理函数（鼠标、键盘等）
from selenium.webdriver.common.action_chains import ActionChains

#1)  鼠标事件
# 方法	                            说明
# ActionChains(driver)	            构造 ActionChains 鼠标对象。
# click()	                        单击
# click_and_hold(on_element=None) 	单击鼠标左键，不松开
# context_click()	                右击
# double_click()	                双击
# drag_and_drop()	                拖动
# move_to_element(above)	        执行鼠标悬停操作
# context_click()	                用于模拟鼠标右键操作， 在调用时需要指定元素定位。
# perform()	                        将所有鼠标操作提交执行。

# 示例
# driver.get('http://c.biancheng.net')
# #通过xpath表达式定位到要悬停的元素
# above = driver.find_element(By.XPATH,"/html/body/div[@id='main']/div[@id='promotion']/div[@id='promotion-list']/div[@id='project-list']/dl/dd[@class='clearfix'][5]/p[@class='left info']/a")
# #对定位到的元素执行鼠标悬停操作
# ActionChains(driver).move_to_element(above).perform()


# 2) 键盘事件
#调用键盘按键操作，引入keys包
from selenium.webdriver.common.keys import Keys
# 方法	说明
# send_keys(Keys.BACK_SPACE)	删除键（BackSpace）
# send_keys(Keys.SPACE)	        空格键(Space)
# send_keys(Keys.TAB)	        制表键(Tab)
# send_keys(Keys.ESCAPE)	    回退键（Esc）
# send_keys(Keys.ENTER)	        回车键（Enter）
# send_keys(Keys.CONTROL,'a'）	全选（Ctrl+A）
# send_keys(Keys.CONTROL,'c')	复制（Ctrl+C）
# send_keys(Keys.CONTROL,'x')	剪切（Ctrl+X）
# send_keys(Keys.CONTROL,'v'）	粘贴（Ctrl+V）
# send_keys(Keys.F1…Fn)	        键盘 F1…Fn
# keys.down(value,element=None)	按下键盘上的某个键
# keys.up(value,element=None)	松开键盘上的某个键

# # 输入框输入内容
# driver.find_element(By.ID,'kw').send_keys('C语言中文网HHH')
# time.sleep(1)
# #删除多输入的H,操作可以乘以次数
# driver.find_element(By.ID,'kw').send_keys(Keys.BACK_SPACE*3)
# #单击 “百度一下”
# driver.find_element(By.ID,'su').click()
# #输入空格键+ “Python教程”
# driver.find_element(By.ID,'kw').send_keys(Keys.SPACE*2)
# driver.find_element(By.ID,'kw').send_keys("python教程")
#
# #ctrl + a全选输入框内容
# driver.find_element(By.ID,'kw').send_keys(Keys.CONTROL,'a')
# #ctrl + x剪切输入框内容
# driver.find_element(By.ID,'kw').send_keys(Keys.CONTROL,'x')
# time.sleep(2)
# #ctrl + v粘贴输入框内容
# driver.find_element(By.ID,'kw').send_keys(Keys.CONTROL,'v')
# #使用回车代替单击
# driver.find_element(By.ID,'su').send_keys(Keys.ENTER)

# 五、无界面浏览器
# Selenium 为了增强浏览器的交互能力，允许使用无头浏览器模式，
# 也就是无界面浏览器，它被广泛的应用于爬虫和自动化测试中。
# 设置无界面浏览器使用.FirefoxOptions().add_argument()
options = webdriver.FirefoxOptions()
# options.add_argument('--headless')#无界面浏览器
# driver = webdriver.Firefox(service = Serveice,options=options)
# driver.get('https://www.baidu.com')
# print(driver.title)
# time.sleep(3)
# #关闭当前界面，只有一个窗口
# driver.close()
# #关闭所有界面
# driver.quit()
# # Selenium 还支持其他一些浏览器参数设置
# opption.add_argument('--window-size=600,600') #设置窗口大小
# opption.add_argument('--incognito') #无痕模式
# opption.add_argument('--disable-infobars') #去掉chrome正受到自动测试软件的控制的提示
# opption.add_argument('user-agent="XXXX"') #添加请求头
# opption.add_argument("--proxy-server=http://200.130.123.43:3456")#代理服务器访问
# opption.add_experimental_option('excludeSwitches', ['enable-automation'])#开发者模式
# opption.add_argument('blink-settings=imagesEnabled=false')  #禁止加载图片
# opption.add_argument('lang=zh_CN.UTF-8') #设置默认编码为utf-8
# opption.add_extension(create_proxyauth_extension(
#            proxy_host='host',
#            proxy_port='port',
#            proxy_username="username",
#            proxy_password="password"
#        ))# 设置有账号密码的代理
# opption.add_argument('--disable-gpu')  # 这个参数可以规避谷歌的部分bug
# opption.add_argument('--disable-javascript')  # 禁用javascript
# opption.add_argument('--hide-scrollbars')  # 隐藏滚动条


# 六、执行JS脚本
# WebDriver 提供了 execute_script() 方法来执行 JavaScript 代码，比如控制浏览器的滚动条。
driver = webdriver.Firefox(service=Serveice)
driver.get('https://www.baidu.com')
#最大化窗口
driver.maximize_window()
#搜索
driver.find_element(By.ID,'kw').send_keys('C语言中文网')
driver.find_element(By.ID,'su').click()
time.sleep(2)

# 通过js代码设置滚动条位置，数值代表(左边距，上边距)
js="window.scrollTo(100,500);"
# 执行JS代码
driver.execute_script(js)
time.sleep(5)
driver.quit()
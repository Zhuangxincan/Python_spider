#测试代码
#导入 webdriver
from selenium import webdriver
#导入驱动配置包
from selenium.webdriver.firefox.service import Service

# 定位方法
from selenium.webdriver.common.by import By

#调用键盘按键操作，引入keys包
from selenium.webdriver.common.keys import Keys

#调用环境变量指定的PhantomJS浏览器创建浏览器对象
#因为高版本selenium放弃了phantomjs
# driver = webdriver.PhantomJS()

#如果没有再环境变量中指定PhantomJs位置
# driver = webdriver.PhantomJS(executable_phth = './phantomjs')

#方法测试：还有一个较为简便的解决办法，就是浏览器自带的无界面浏览--失败
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
# driver = webdriver.Chrome(chrome_options=chrome_options)

# 方法一：报错SessionNotCreatedException--失败驱动错误
# Service =Service('C:\webdirvers\chromedriver.exe')
# driver = webdriver.Chrome(service=Service)
# 方法二：报错SessionNotCreatedException---失败驱动错误
# executable_path = r'D:\软件\Python\Scripts\chromedriver.exe'
# driver = webdriver.Chrome(executable_path = executable_path)
#get 方法会一直等到页面被完全加载才会继续程序，通常测试会在这里选择time.sleep(2)

# 方法三：换火狐浏览器
#提示executable_path已弃用
# executable_path = r'D:\软件\Python\Scripts\geckodriver.exe'
# driver = webdriver.Firefox(executable_path = executable_path)
#改用serveice方法
Serveice = Service(r'D:\软件\Python\Scripts\geckodriver.exe')
driver = webdriver.Firefox(service = Serveice)
driver.get('http://www.baidu.com/')

#获取页面为wrapper的id标签的文本内容
data = driver.find_element(By.ID,'head_wrapper').text

#打印数据
print(data)

#打印页面标题 ’百度一下，你就知道‘
print (driver.title)

#生成当前页面快照并保存
driver.save_screenshot('baidu.png')

#id = 'kw' 是百度搜索输入框，搜索输入字符串 '长城'
driver.find_element(By.ID,'kw').send_keys(u'长城')

#id = 'su' 是百度搜索按钮，click() 是模拟点击
driver.find_element(By.ID,'su').click()

#获取新的页面快照
driver.save_screenshot('长城.png')

#打印网页渲染后的源代码
print(driver.page_source)

#获取当前页面Cookie
print(driver.get_cookies())

#ctrl+a 全选输入框内容
driver.find_element(By.ID,'kw').send_keys(Keys.CONTROL,'a')

#ctrl+x 全选输入框内容
driver.find_element(By.ID,'kw').send_keys(Keys.CONTROL,'x')

# 输入框重新输入内容
driver.find_element(By.ID,'kw').send_keys('itcast')

#模拟回车键Enter
driver.find_element(By.ID,'kw').send_keys(Keys.RETURN)

#清除输入框内容
driver.find_element(By.ID,'kw').clear()

#生成新的页面快照
driver.save_screenshot('itcast.png')

#获取当前url
print(driver.current_url)

#关闭当前页面，如果只有一个页面，会关闭浏览器
driver.close()

#关闭浏览器
driver.quit()

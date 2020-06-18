from selenium import webdriver

# 创建 WebDriver 实例对象，指明使用chrome浏览器驱动
wd = webdriver.Chrome()

wd.implicitly_wait(10)
# WebDriver 实例对象的get方法 可以让浏览器打开指定网址     
wd.get('https://www.baidu.com')
# 返回一个webElement类型的对象
element =  wd.find_element_by_id('kw')


element.send_keys("你好")
# 输入回车 确认
from selenium.webdriver.common.keys import Keys
element.send_keys(Keys.ENTER)

element = wd.find_element_by_id('1')
print(element.text)

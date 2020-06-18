from selenium import webdriver

wd = webdriver.Chrome()
wd.implicitly_wait(8)

wd.get('https://www.baidu.com')


#
# wd.find_element_by_id('kw').send_keys('你好')
# wd.find_element_by_id('su').click()


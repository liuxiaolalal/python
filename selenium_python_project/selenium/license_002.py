from selenium import webdriver
wd = webdriver.Chrome()
wd.implicitly_wait(10)
wd.get('http://127.0.0.1/mgr/sign.html')
element = wd.find_element_by_id('password')
element.send_keys('88888888')
wd.find_element_by_class_name("col-xs-12").click()



# from selenium.webdriver.common.keys import Keys
# element.send_keys(Keys.ENTER)

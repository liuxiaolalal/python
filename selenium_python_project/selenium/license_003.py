from selenium import webdriver

wd = webdriver.Chrome()

wd.get('http://127.0.0.1/mgr/sign.html')
# set (username and password)
wd.find_element_by_id('username').send_keys('byh')
wd.find_element_by_id('password').send_keys('888888')
# log in
wd.find_element_by_class_name('col-xs-12').click()
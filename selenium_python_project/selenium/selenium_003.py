from selenium import webdriver

wd = webdriver.Chrome()
wd.get('http://cdn1.python3.vip/files/selenium/sample1.html')

elements = wd.find_elements_by_tag_name('div')
for ele in elements:
    print(ele.text)

r
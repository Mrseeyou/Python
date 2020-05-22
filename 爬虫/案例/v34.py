from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

browser.get('http://www.baidu.com')

text = browser.find_element_by_id('wrapper').text

print(text)
print(browser.title)

# 得到页面的快照
browser.save_screenshot('index.png')

# id'kw'的是百度的输入框,我们得到的输入框的ui元素后直接输入'大熊猫'
browser.find_element_by_id('kw').send_keys(u'大熊猫')
# id='su'的是百度的搜索按钮.click模拟点击
browser.find_element_by_id('su').click()
time.sleep(5)
# 保存
browser.save_screenshot('daxiongmao.png')

# 获取当前页面的cookie
print(browser.get_cookies())

# 模拟输入框 两个按键ctrl+a
browser.find_element_by_id('kw').send_keys(Keys.CONTROL, 'a')
# 两个按键ctrl+x
browser.find_element_by_id('kw').send_keys(Keys.CONTROL, 'x')
# 搜索别的内容
browser.find_element_by_id('kw').send_keys(u'长颈鹿')
browser.save_screenshot('changjinglu.png')
# 搜索框点击回车键
browser.find_element_by_id('su').send_keys(Keys.RETURN)
time.sleep(5)
browser.save_screenshot('changjinglu2.png')

# 清空按钮
browser.find_element_by_id('kw').clear()
browser.save_screenshot('clear.png')

# 关闭浏览器
browser.quit()

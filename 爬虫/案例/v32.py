from urllib import request
from bs4 import BeautifulSoup

url = "http://www.baidu.com"

rsp = request.urlopen(url)
content = rsp.read()

soup = BeautifulSoup(content, 'lxml')

# 需要用for循环遍历出来
tags = soup.find_all(name='meta')
for tag in tags:
    print(tag)
print("="*30)

import re
tags = soup.find_all(re.compile('^me'),content="always")
for tag in tags:
    print(tag)

from urllib import request
from bs4 import BeautifulSoup

url = "http://www.baidu.com"

rsp = request.urlopen(url)
content = rsp.read()

soup = BeautifulSoup(content, "lxml")

print(soup.name)
print("="*30)

# 通过遍历加条件,获取期望的结果
for i in soup.head.contents:
    if i.name == "meta":
        print(i)
    if i.name == "title":
        print(i)
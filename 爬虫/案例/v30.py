from urllib import request
from bs4 import BeautifulSoup

url = "http://www.baidu.com"

rsp = request.urlopen(url)
content = rsp.read()

# 会自动解码
# 创建一个实例 第一次参数用什么来创建 第二个参数指定引擎
soup = BeautifulSoup(content, 'lxml')

# 整理出来
content = soup.prettify()
print(content)

print("="*20)
print(soup.link)
print(soup.link.name)
print(soup.link.attrs)
# 读取
print(soup.link.attrs['type'])
# 修改
soup.link.attrs['type'] = 'onetwotherr'
print(soup.link)
print("="*20)
print(soup.title)
print(soup.title.name)
print(soup.title.attrs)
# 查看内容
print(soup.title.string)
print("="*20)
print(soup.name)
print(soup.attrs)

from urllib import request,error
import re

'''
利用正则 爬取猫眼电影
url:https://maoyan.com/board

查看源代码分析:
1.每个影片以dd开头的单元
2.单元内存储一部电影的全部信息

思路:
1.利用re把dd内容都分别查找出来
2.对应每一个dd,用re查找需要的信息

'''

# 1.下载页面内容
url = "https://maoyan.com/board"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
}
req = request.Request(url, headers=headers)

rsp = request.urlopen(req)

html = rsp.read().decode()

#2. 提取每个dd 缩小处理范围

s = r'<dd>(.*?)</dd>'

pattern = re.compile(s, re.S)

films = pattern.findall(html)
print(len(films))

#3. 提取电影名称
for film in films:
    s = r'<a.*?title="(.*?)"'
    pattern = re.compile(s)
    title = pattern.findall(film)[0]
    print(title)

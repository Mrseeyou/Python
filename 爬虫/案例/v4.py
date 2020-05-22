# 掌握对url进行参数编码的方法
# 需要使用parse模块

import urllib.request, urllib.parse

if __name__ == '__main__':

    url = "http://www.baidu.com/s?"
    wd = input("Input your keyword:")

    # 要想使用data, 需要使用字典结构
    qs = {"wd":wd}
    # 转换url编码
    qs = urllib.parse.urlencode(qs)
    print(qs)

    fullurl = url + qs
    print(fullurl)

    # 如果直接使用带参数的url 是不能访问的
    rsp = urllib.request.urlopen(fullurl)

    # 解码
    html = rsp.read().decode()

    print(html)


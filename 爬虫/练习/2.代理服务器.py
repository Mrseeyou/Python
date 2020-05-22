from urllib import request,error
import random

url = 'http://www.baidu.com'

proxy_list = [
    {"http":"175.42.122.46:9999"},
    {"http":"36.248.133.247:9999"},
    {"http":"163.125.69.31:8888"},
    {"https":"61.140.28.228:4216"},
    {"https":"118.113.247.204:9999"},
]

# 创建ProxyHandler
proxy_handler_list = []
for proxy in proxy_list:
    proxy_handler = request.ProxyHandler(proxy)
    proxy_handler_list.append(proxy_handler)
# 创建Opener
opener_list = []
for proxy_handler in proxy_handler_list:
    opener = request.build_opener(proxy_handler)
    opener_list.append(opener)



try:
    opener = random.choice(opener_list)
    # 安装Opener
    request.install_opener(opener)
    rsp = request.urlopen(url)
    html = rsp.read().decode()
    print(html)
except error.URLError as e:
    print(e)
except Exception as e:
    print(e)
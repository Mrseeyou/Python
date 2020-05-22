import requests

# 两种请求方式

url = "http://www.baidu.com"

# 使用get请求
rsp = requests.get(url)
print(rsp.text)

# 使用request请求
req = requests.request("get",url)
print(req.text)

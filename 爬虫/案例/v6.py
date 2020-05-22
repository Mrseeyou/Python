# 利用Request来实现V5的内容
from urllib import request, parse
import json

url = "https://fanyi.baidu.com/sug"

data = {'kw':'girl'}

data = parse.urlencode(data).encode()

# 需要构造一个请求头,请求头部应该至少包含传入数据的长度
# 要求传入有的请求头是一个字典类型
headers = {
    'Content-Length':len(data)
}

# 构造一个Request的实例
req = request.Request(url=url, data=data, headers=headers)

rsp = request.urlopen(req)

json_data = rsp.read().decode()

json_data = json.loads(json_data)
for items in json_data["data"] :
    print(items["v"])



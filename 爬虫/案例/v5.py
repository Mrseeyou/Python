'''
利用parse模块模拟post请求
分析百度词典
    1.打开F12
    2.尝试输入单词girl, 发现每敲一个字母后都有请求
    3.请求地址是 : http://fanyi.baidu.com/sug
    4.利用NetWork-All-Heardets, 查看, 发现FormData的值 是kw:***
    5.检查返回内容的格式,  json
'''
from urllib import request, parse
import json

'''
流程
    1.利用data构造函数, 然后urlopen打开
    2.返回一个json格式的结果
    3.结果就应该是girl的释义
'''
url = "https://fanyi.baidu.com/"

# girl应该是由用户输入,此处使用硬编码
# 必须是字典格式才能使用data
data = {'kw':'girl'}

# 更改请求方式,对data进行编译, 还需要转换成bytes格式
data = parse.urlencode(data).encode('utf-8')

# 确定要打开的内容
rsp = request.urlopen(url,data=data)

# 指定解码格式
json_data = rsp.read().decode('utf-8')
print(type(json_data))
print(json_data)

# 上述代码不能成功解码
json_data = json.loads(json_data)
print(type(json_data))
for items in json_data['data']:
    print(items['v'])
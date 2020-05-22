import requests

url = "http://www.baidu.com/?"

kw = {
    "wd":"呵呵"
}

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
}

rsp = requests.get(url, params=kw, headers=headers)

print(rsp.text)
print(rsp.content)
print(rsp.url)
print(rsp.encoding)
print(rsp.status_code) # 请求返回码

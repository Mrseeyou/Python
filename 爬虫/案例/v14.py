from urllib import request,parse
from http import cookiejar

cookie = cookiejar.CookieJar()

cookie_handler = request.HTTPCookieProcessor(cookie)
http_handler = request.HTTPHandler()
https_handler = request.HTTPSHandler()

opener = request.build_opener(cookie_handler,https_handler,http_handler)

def login():
    url = 'http://www.renren.com/PLogin.do'
    data = {
        'email': '13112520315',
        'password': '249399289'
    }
    data = parse.urlencode(data).encode()
    req = request.Request(url,data=data)

    rsq = opener.open(req)

if __name__ == '__main__':
    login()

    print(cookie)
    for item in cookie:
        print(type(item))
        print(item)
        for i in dir(item):
            print(i)

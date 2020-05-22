from urllib import request,parse
from http import cookiejar

filename = "cookie.txt"
cookie = cookiejar.MozillaCookieJar(filename)

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

    # 保存cookie到文件
    # ignore_discard表示即使cookie将要被删除也保存下来
    # ignore_expire表示如果文件中cookie即使过期也保存下来
    cookie.save(ignore_discard=True,ignore_expires=True)

if __name__ == '__main__':
    login()
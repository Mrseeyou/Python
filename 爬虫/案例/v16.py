from urllib import request,parse
from http import cookiejar

cookie = cookiejar.MozillaCookieJar()
cookie.load('cookie.txt',ignore_expires=True,ignore_discard=True)

cookie_handler = request.HTTPCookieProcessor(cookie)
http_handler = request.HTTPHandler()
https_handler = request.HTTPSHandler()

opener = request.build_opener(cookie_handler,https_handler,http_handler)

def getHomePage():
    url = 'http://www.renren.com/973032462/newsfeed/photo'

    # 如果已经执行了login函数,则opener自动已经包含相应的cookie值
    rsp = opener.open(url)

    html = rsp.read().decode()

    with open("rsp4.html","w",encoding="utf-8") as f:
        f.write(html)

if __name__ == '__main__':
    getHomePage()
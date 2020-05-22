from urllib import request,parse

'''
步骤:
1.查看源代码,查找登录入口
    https://security.kaixin001.com/login/login_post.php 
    相应的用户名密码名称:email,password
2.构造opener
3.构造login函数

'''
import ssl
# 忽略安全问题
ssl._create_default_https_context = ssl._create_unverified_context

# 构造opener
from http import cookiejar

cookie = cookiejar.CookieJar()
cookie_handler = request.HTTPCookieProcessor(cookie)
http_handler = request.HTTPHandler()
https_handler = request.HTTPHandler()

opener = request.build_opener(http_handler, https_handler, cookie_handler)

# 构造login
def login():
    login_url = "https://security.kaixin001.com/login/login_post.php"

    data = {
        "email":"15501903290",
        "password":"123456"
    }

    # 对post的data进行编码
    data = parse.urlencode(data)

    # http协议的请求头
    headers = {
        "Content-length":len(data),
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    }

    # 构建请求Request对象
    # data要求是一个bytes对象,所以需要进行编码
    req = request.Request(login_url, data=data.encode(), headers=headers)

    rsp = opener.open(req)

    html = rsp.read()
    html = html.decode()
    # print(html)

# 构建我的主页
def getHomePage():
    base_url = "http://www.kaixin001.com/home/?uid=181921463"
    rsp = opener.open(base_url)
    html = rsp.read()
    html = html.decode()

    print(html)
if __name__ == '__main__':
    login()
    getHomePage()
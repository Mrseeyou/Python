from urllib import request,parse

def youdao(key):

    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

    data = {
        "i":"girl",
        "from":"AUTO",
        "to":"AUTO",
        "smartresult":"dict",
        "client":"fanyideskweb",
        "salt":"15759889253989",
        "sign":"e87ec35d90276484cec74bd0dc806ea8",
        "ts":"1575988925398",
        "bv":"ab57a166e6a56368c9f95952de6192b5",
        "doctype":"json",
        "version":"2.1",
        "keyfrom":"fanyi.web",
        "action":"FY_BY_REALTlME"
    }

    headers = {
        "Accept":"application/json, text/javascript, */*; q=0.01",
        #"Accept-Encoding":"gzip, deflate",
        "Accept-Language":"zh-CN,zh;q=0.9",
        "Connection":"keep-alive",
        "Content-Length":"237",
        "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie":"OUTFOX_SEARCH_USER_ID=1664548967@10.169.0.84; JSESSIONID=aaaM3XFL5LElm9kCvqW7w; OUTFOX_SEARCH_USER_ID_NCOO=901115725.592805; ___rl__test__cookies=1575989409848",
        "DNT":"1",
        "Host":"fanyi.youdao.com",
        "Origin":"http://fanyi.youdao.com",
        "Referer":"http://fanyi.youdao.com/",
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
        "X-Requested-With":"XMLHttpRequest"
    }

    data = parse.urlencode(data).encode()

    req = request.Request(url=url, data=data, headers=headers)

    rsp = request.urlopen(req)

    html = rsp.read().decode()

    print(html)
if __name__ == '__main__':
    youdao('girl')
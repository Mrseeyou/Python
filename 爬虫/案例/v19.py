'''
1.获取salt的算法 salt = "" + (new Date).getTime()+parseInt(10 * Math.random(), 10);
2.获取sign的算法 sign = n.md5("fanyideskweb" + e + i + "n%A-rKaT5fb[Gy?;N5@Tj")
第二条前后字符串是固定的,求e值和i值
通过代码可知,i值就是salt  e值则是传入的参数(输入的需要翻译的单词)
3.获取ts的算法 "" + (new Date).getTime()
4.获取bv的算法  ts = n.md5(navigator.appVersion)
在控制台输入navigator.appVersion获取版本号
5.获取__rl__test__cookies的算法  (new Date).getTime()

'''
import time, random, hashlib

times = time.time()

def getTs():
    ts = int(times*1000)
    return ts

def getSalt():
    salt =  int(str(getTs()) + str(random.randint(0,10)))
    return salt

def getMD5(value):
    md5 = hashlib.md5()
    md5.update(value.encode("utf-8"))
    md5_str = md5.hexdigest()
    return md5_str

def getSign(key, salt):
    sign = "fanyideskweb"+ key + str(salt) + "n%A-rKaT5fb[Gy?;N5@Tj"
    sign = getMD5(sign)
    return sign

from urllib import request,parse

def youdao(key):

    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    # 确保是同一个盐
    salt = getSalt()
    ts = getTs()

    data = {
        "i":key,
        "from":"AUTO",
        "to":"AUTO",
        "smartresult":"dict",
        "client":"fanyideskweb",
        "salt":str(salt),
        "sign":getSign(key,salt),
        "ts":str(ts),
        "bv":"ab57a166e6a56368c9f95952de6192b5",
        "doctype":"json",
        "version":"2.1",
        "keyfrom":"fanyi.web",
        "action":"FY_BY_REALTlME"
    }
    headers = {
        "Cookie":"OUTFOX_SEARCH_USER_ID=1664548967@10.169.0.84; OUTFOX_SEARCH_USER_ID_NCOO=901115725.592805; JSESSIONID=aaaRzZds-xIn85JdDM57w; ___rl__test__cookies=" + str(getTs()),
        "Host":"fanyi.youdao.com",
        "Origin":"http://fanyi.youdao.com",
        "Referer":"http://fanyi.youdao.com/",
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
    }
    data = parse.urlencode(data).encode()

    req = request.Request(url=url, data=data, headers=headers)

    rsp = request.urlopen(req)

    html = rsp.read().decode()

    print(html)
if __name__ == '__main__':
    youdao('love')


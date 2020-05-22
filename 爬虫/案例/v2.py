import urllib
import chardet
# 利用request下载页面 自动检测页面编码

if __name__ == '__main__':
    url = "https://hao.360.com/?wd_xp1"

    rsp = urllib.request.urlopen(url)

    html = rsp.read()

    # 利用 chardet自动检测
    cs = chardet.detect(html)
    print(type(cs))
    print(cs)

    # 使用get取值确保不会出错,如果encoding取到值,用encoding 如果没取到 用utf-8
    html = html.decode(cs.get("encoding","utf-8"))
    print(html)
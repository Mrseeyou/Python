from urllib import request

# 使用urllib.request请求一个网页内容,并把内容打印出来

if __name__ == '__main__':
    url = "http://001dlcifcdiji.jumpbc.chuairan.com/"
    # 打开相应url并把相应页面作为返回
    rsp = request.urlopen(url)

    # 把返回的结果读取出来
    # 读取出来的内容类型为bytes
    html = rsp.read()

    # 如果需要把bytes内容转换成字符串, 需要解码
    html = html.decode()
    print(html)
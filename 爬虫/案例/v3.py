import urllib

if __name__ == '__main__':
    url = "http://www.7junshi.com/?qid=360cn"

    rsp = urllib.request.urlopen(url)
    print(type(rsp))
    print(rsp)

    print("URL:{0}".format(rsp.geturl()))
    print("INFO:{0}".format(rsp.info()))
    print("CODE:{0}".format(rsp.getcode()))

    html = rsp.read()

    html = html.decode()
    # print(html)
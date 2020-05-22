from urllib import request,error

if __name__ == '__main__':
    url = 'http://www.baidu.com'

    try:
        # 使用head方法伪装UA
        # headers = {}
        # headers['User-Agent'] = 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400) '
        # req = request.Request(url, headers=headers)

        # 使用add_header方法伪装UA
        req = request.Request(url)
        req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0 ")

        # 正常访问
        rsp = request.urlopen(req)
        html = rsp.read().decode()
        print(html)

    except error.HTTPError as e:
        print(e)
    except error.URLError as e:
        print(e)
    except Exception as e:
        print(e)
    print('DOME.......')


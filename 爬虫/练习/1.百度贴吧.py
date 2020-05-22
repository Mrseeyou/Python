from urllib import parse, request
'''
中国吧
    主页是:   http://tieba.baidu.com/f?kw=中国吧
    第一页是: http://tieba.baidu.com/f?kw=%E4%B8%AD%E5%9B%BD&ie=utf-8&pn=0
    第二页是: http://tieba.baidu.com/f?kw=%E4%B8%AD%E5%9B%BD&ie=utf-8&pn=50
    第三页是: http://tieba.baidu.com/f?kw=%E4%B8%AD%E5%9B%BD&ie=utf-8&pn=100
    第四页是: http://tieba.baidu.com/f?kw=%E4%B8%AD%E5%9B%BD&ie=utf-8&pn=150
    第五页是: http://tieba.baidu.com/f?kw=%E4%B8%AD%E5%9B%BD&ie=utf-8&pn=200  
'''

if __name__ == '__main__':
    # 1.构建参数字典
    qs = {
        'kw':'中国吧',
        'ie':'utf-8',
        'pn':0
    }
    # 2.使用parse构建完整的url 假设只要前10页
    urls = []
    baseurl = "http://tieba.baidu.com/f?"
    for i in range(10):
        # 构建新的qs
        pn = i*50
        qs['pn'] = str(pn)
        # 把qs编码后和基础url进行拼接 而后装入url列表中
        urls.append(baseurl + parse.urlencode(qs))
    print(urls)

    # 3.使用for循环下载
    for url in urls:
        rsp = request.urlopen(url)
        html = rsp.read().decode()
        print(html)
from urllib import request

if __name__ == '__main__':

    url = 'http://www.renren.com/973032462/profile'

    headers = {
        "Cookie": "anonymid=k3uz0kf23jb5r3; depovince=GW; _r01_=1; JSESSIONID=abcKvGdc2Xllm-ddToE7w; ick_login=2a757cd1-fefe-4f69-9790-4ac856690462; ick=83017be0-d222-45aa-bae6-ea7151118ef5; t=a63c18f6eed47a5452b217ff6ea273d62; societyguester=a63c18f6eed47a5452b217ff6ea273d62; id=973032462; xnsid=21c3a4fd; jebecookies=aa40a49f-15fd-47b9-9b58-b19809889a0e|||||; ver=7.0; loginfrom=null; jebe_key=bb859ebb-fab5-46d3-8e24-215c2f26fa56%7Cad9727aa4f4d14be27636a30b029523f%7C1575686651920%7C1%7C1575686647432; jebe_key=bb859ebb-fab5-46d3-8e24-215c2f26fa56%7Cad9727aa4f4d14be27636a30b029523f%7C1575686651920%7C1%7C1575686647434; wp_fold=0"
    }

    req = request.Request(url, headers=headers)

    rsp = request.urlopen(req)

    html = rsp.read().decode()

    with open("rsp2.html","w",encoding='utf-8') as f:
        f.write(html)
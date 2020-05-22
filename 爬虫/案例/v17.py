from urllib import request

# 导入python ssl模块来处理
import ssl

# 利用非认证上下文环境替换认证的上下文环境
# ssl._create_default_https_context = ssl._create_unverified_context

url = 'http://mxd.sdo.com/web6/index/index.asp'
rsp = request.urlopen(url)

html = rsp.read().decode()

print(html)
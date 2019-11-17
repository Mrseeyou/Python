import cgi,cgitb,json,time
cgitb.enable()

print("Content-Type: text/html")
print()

# 接受用户发送的数据
fs = cgi.FieldStorage()
# 数据重组
inputs = {}
for key in fs.keys():
    inputs[key] = fs[key].value

# 给用户返回数据
# print(inputs)

# time.sleep(3.控件)

# 转换成json格式的数据
print(json.dumps(inputs))
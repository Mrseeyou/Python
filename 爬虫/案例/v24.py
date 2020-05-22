import re

# 一下正则分成了两个组,以小括号为单位
s = r'([a-z]+) ([a-z]+)'

# s,I表示忽略大小写
pattern = re.compile(s, re.I)

m = pattern.match("Hello world wide web")

#goup(0)表示返回匹配成功的整个字符串
s = m.group(0)
print(s)

#span(0)表示返回成功的整个字符串的跨度
a = m.span(0)
print(a)

# 带参数则表示把第几个匹配到的打印出来 从1开始不是从0开始
s1 = m.group(2)
a1 = m.span(2)
print(s1)
print(a1)
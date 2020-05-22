import re

s = r'\d+'

pattern = re.compile(s)

m = pattern.search("one123two456three789")
print(m.group())

# 参数表示查找的起始位置,结束位置大于整个长度,等于后面的全部查找
m1 = pattern.search("one123two456three789",10,40)
print(m1.group())

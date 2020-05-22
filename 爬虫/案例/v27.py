import re

hello = u'你好 可可'

pattern = re.compile(r'[\u4e00-\u9fa5]+')

m = pattern.findall(hello)
print(m)
import re

pattern = re.compile(r'\d+')

s = pattern.findall("I am 18 years odl end 175 high")
print(s)

s = pattern.finditer("I am 18 years odl and 175 high")
print(s)
for i in s:
    print(i.group())

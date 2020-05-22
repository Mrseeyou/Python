from lxml import etree

# 只能读取xml格式内容,
html = etree.parse("./v29.html")

rst = etree.tostring(html, pretty_print=True)
print(rst)

rst = html.xpath("//book")
print(rst)

rst = html.xpath("//book/title[@lang='en']")
rst = rst[0]
print(rst.tag)
print(rst.text)
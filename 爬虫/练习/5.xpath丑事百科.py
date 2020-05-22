import requests
from lxml import etree

url = "https://www.qiushibaike.com/imgrank/"

headers = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "Accept-Language":"zh-CN,zh;q=0.9",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
}

# 下载页面
rsp = requests.get(url, headers=headers)
html = rsp.text

# 提取页面解析成html
html = etree.HTML(html)
# contains是一种不完全匹配，就是说相应属性值包含字段即可
rst = html.xpath('//div[contains(@id, "qiushi_tag")]')

# 筛选div
for r in rst:
    content = r.xpath('//div[@class="content"]')
# 提取标题部分
for i in content:
    print(i.xpath('./span')[0].text)


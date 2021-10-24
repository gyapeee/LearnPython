import requests
from lxml import html

page = requests.get(url='https://www.teletal.hu/etlap/45')
# decode bytes of page's content
content = html.fromstring(page.content.decode('utf-8'))

# find the index of the minimum in list https://www.kite.com/python/answers/how-to-find-the-index-of-the-minimum-value-of-a-list-in-python

prefix = "//div[contains(@class,'menu-card-5-day')]/div[contains(@class,'menu-cell-text')]"
csirkemell = "[contains(normalize-space(),'csirkemell')]/"
prices = content.xpath(prefix + csirkemell + "child::div[contains(@class,'menu-price-field')]/div/h6/strong/text()")
days = content.xpath(prefix + "/div" + csirkemell + "following-sibling::div/a/@nap")
contents = content.xpath(prefix + csirkemell + "div/text()")

print(prices)
print(days)
print(contents)

print("\n")

# packing
t = 123, 12323, 'sdfsfdsf'
print(t)
# unpacking
x, y, z = t
print(z)
print(x, y, z)

import requests
from lxml import html

page = requests.get(url = 'https://www.teletal.hu/etlap/45')
#decode bytes of page's content
content = html.fromstring(page.content.decode('utf-8'))

#find the index of the minimum in list https://www.kite.com/python/answers/how-to-find-the-index-of-the-minimum-value-of-a-list-in-python

prices = content.xpath("//div[contains(@class,'menu-card-5-day')]/div[contains(@class,'menu-cell-text')][contains(normalize-space(),'csirkemell')]/child::div[contains(@class,'menu-price-field')]/div/h6/strong/text()")
days = content.xpath("//div[contains(@class,'menu-card-5-day')]/div[contains(@class,'menu-cell-text')]/div[contains(normalize-space(),'csirkemell')]/following-sibling::div/a/@nap")
contents = content.xpath("//div[contains(@class,'menu-card-5-day')]/div[contains(@class,'menu-cell-text')][contains(normalize-space(),'csirkemell')]/div/text()")

print(prices)
print(days)
print(contents)

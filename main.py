import requests
from lxml import html
from lxml import etree

page = requests.get(url = 'https://www.teletal.hu/etlap/45')
content = html.fromstring(page.content)

prices = content.xpath("//div[contains(@class,'menu-card-5-day')]/div[contains(@class,'menu-cell-text')][contains(normalize-space(),'csirkemell')]/child::div[contains(@class,'menu-price-field')]/div/h6/strong/text()")
days = content.xpath("//div[contains(@class,'menu-card-5-day')]/div[contains(@class,'menu-cell-text')]/div[contains(normalize-space(),'csirkemell')]/following-sibling::div/a/@nap")
contents = content.xpath("//div[contains(@class,'menu-card-5-day')]/div[contains(@class,'menu-cell-text')][contains(normalize-space(),'csirkemell')]/div/text()")

prices_list = [i for i in prices]
days_list = [i for i in days]
contents_list = [type(i) for i in contents]

print(prices_list)
print(days_list)
print(contents_list)

# https://www.youtube.com/watch?v=CxeP1dQi9rg
print('Héjjmánő'.encode('UTF-8').decode("UTF-8"))
print(type('Héjjmánő'))
print(type('Héjjmánő'.encode('UTF-8')))
import requests
from lxml import html

page = requests.get(url = 'https://www.teletal.hu/etlap/45')
content = html.fromstring(page.content)

prices = content.xpath("//div[contains(@class,'menu-card-5-day')]/div[contains(@class,'menu-cell-text')][contains(normalize-space(),'csirkemell')]/child::div[contains(@class,'menu-price-field')]/div/h6/strong/text()")

prices_list = [i for i in prices]

print(prices_list)
from enum import Enum

import requests
from lxml import html


class Workdays(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5


# more days

page = requests.get(url='https://www.teletal.hu/etlap/45')
# decode bytes of page's content
content = html.fromstring(page.content.decode('utf-8'))

# find the index of the minimum in list https://www.kite.com/python/answers/how-to-find-the-index-of-the-minimum-value-of-a-list-in-python

prefix = "//div[contains(@class,'menu-card-5-day')]/div[contains(@class,'menu-cell-text')]"
csirkemell = "[contains(normalize-space(),'csirkemell')]/"

prices = content.xpath(prefix + csirkemell + "child::div[contains(@class,'menu-price-field')]/div/h6/strong/text()")
days = content.xpath(prefix + "/div" + csirkemell + "following-sibling::div/a/@nap")
contents = content.xpath(prefix + csirkemell + "div/text()")

meal_dict = [(Workdays(int(day)).name, content, price) for day, content, price in zip(days, contents, prices)]
print(meal_dict)

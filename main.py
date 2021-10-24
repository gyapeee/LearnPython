from enum import Enum

import requests
from lxml import html

PREFIX = "//div[contains(@class,'menu-card-5-day')]/div[contains(@class,'menu-cell-text')]"
CSIRKEMELL = "[contains(normalize-space(),'csirkemell')]/"


class Workdays(Enum):
    HÉTFŐ = 1
    KEDD = 2
    SZERDA = 3
    CSÜTÖRTÖK = 4
    PÉNTEK = 5


# get the menu from the url
page = requests.get(url='https://www.teletal.hu/etlap/45')
# decode bytes of page's content
document = html.fromstring(page.content.decode('utf-8'))

# extract days, meals and prices which contains csirkemell
days = document.xpath(PREFIX + "/div" + CSIRKEMELL + "following-sibling::div/a/@nap")
ingredients = document.xpath(PREFIX + CSIRKEMELL + "div/text()")
prices = document.xpath(PREFIX + CSIRKEMELL + "child::div[contains(@class,'menu-price-field')]/div/h6/strong/text()")

# initialize the output
cheapest_csirkmell_at_weekdays = {day.name: ['Nincs', 'Nincs'] for day in Workdays}
# create a generator for the merged days, meals and prices
meals = ((Workdays(int(day)).name, ingredient, price) for day, ingredient, price in zip(days, ingredients, prices))
# Add cheaper meal to each day
for meal in meals:
    # replace the initial data if the actual price is less
    if cheapest_csirkmell_at_weekdays[meal[0]][1] > meal[2]:
        cheapest_csirkmell_at_weekdays[meal[0]][0] = meal[1]
        cheapest_csirkmell_at_weekdays[meal[0]][1] = meal[2]

print(cheapest_csirkmell_at_weekdays)

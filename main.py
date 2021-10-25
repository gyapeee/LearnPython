import time
from enum import Enum

from lxml import html
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

TELETAL_URL = "https://www.teletal.hu/etlap/45"
PREFIX = "//div[contains(@class,'menu-card-5-day')]/div[contains(@class,'menu-cell-text')]"
CSIRKEMELL = "[contains(normalize-space(),'csirkemell')]/"


class Workdays(Enum):
    HÉTFŐ = 1
    KEDD = 2
    SZERDA = 3
    CSÜTÖRTÖK = 4
    PÉNTEK = 5


def get_browser():
    options = Options()
    options.headless = True
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    browser.get(TELETAL_URL)
    return browser


def scroll_down_to_end():
    for i in range(17):
        time.sleep(0.1)
        body.send_keys(Keys.PAGE_DOWN)


def extract_data():
    # extract days, meals and prices which contains csirkemell
    days = document.xpath(PREFIX + "/div" + CSIRKEMELL + "following-sibling::div/a/@nap")
    ingredients = document.xpath(PREFIX + CSIRKEMELL + "div/text()")
    prices = document.xpath(
        PREFIX + CSIRKEMELL + "child::div[contains(@class,'menu-price-field')]/div/h6/strong/text()")

    # fullday menu : /html/body/form/main/div/section[23]/div/table/tbody/tr[7]/td[2]/div/div[6]
    # causes the difference between input data days, ingredients and prices
    print(len(days))
    print(days)
    print(len(ingredients))
    print(ingredients)
    print(len(prices))
    print(prices)
    return days, ingredients, prices


def print_minimums(days, ingredients, prices):
    if len(days) == len(ingredients) and len(ingredients) == len(prices):
        # initialize the output
        cheapest_csirkmell_at_weekdays = {day.name: ['Nincs', 999999] for day in Workdays}
        # create a generator for the merged days, meals and prices
        meals = [(Workdays(int(day)).name, ingredient, price.replace('.', '').replace(' Ft', '')) for
                 day, ingredient, price
                 in
                 zip(days, ingredients, prices)]

        # Add cheaper meal to each day
        for meal in meals:
            # replace the initial data if the actual price is less
            if cheapest_csirkmell_at_weekdays[meal[0]][1] > int(meal[2]):
                cheapest_csirkmell_at_weekdays[meal[0]][0] = meal[1]
                cheapest_csirkmell_at_weekdays[meal[0]][1] = int(meal[2])

        print(cheapest_csirkmell_at_weekdays)
        # getting the mininum is not fine
        print('520 Ft' > '1.290 Ft')
    else:
        raise Exception('Cannot print cheapest for all day',
                        'different length in days, ingredients, prices lists: ' + str(len(days)) + ', ' + str(len(
                            ingredients)) + ', ' + str(len(prices)))


browser = get_browser()
body = browser.find_element(By.TAG_NAME, 'html')
# get end pos
scroll_down_to_end()

html_page = browser.page_source
time.sleep(2)
document = html.fromstring(html_page)

days, ingredients, prices = extract_data()
print_minimums(days, ingredients, prices)

browser.quit()

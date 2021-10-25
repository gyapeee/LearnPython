import time
from enum import Enum

from lxml import html
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

TELETAL_URL = "https://www.teletal.hu/etlap/45"
PREFIX = "//div[contains(@class,'menu-card-5-day')]/div[contains(@class,'menu-cell-text')]"
# translate is needed toi have lowercase input
CSIRKEMELL = "[contains(translate(normalize-space(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz')," \
             "'csirkemell')]/ "
_100MS = 0.1
SCROLL_STEPS = 17
HIGH_PRICE = 999999


class Workdays(Enum):
    HÉTFŐ = 1
    KEDD = 2
    SZERDA = 3
    CSÜTÖRTÖK = 4
    PÉNTEK = 5


def get_browser():
    # get the webdriver in headless mode
    options = Options()
    options.headless = True
    service = Service(ChromeDriverManager().install())
    chrome = webdriver.Chrome(service=service, options=options)
    chrome.get(TELETAL_URL)
    return chrome


def scroll_down_to_end():
    # scrolls down to the end of the page
    for i in range(SCROLL_STEPS):
        time.sleep(_100MS)
        body.send_keys(Keys.PAGE_DOWN)


def extract_data():
    # extract days, meals and prices which contains csirkemell
    days = document.xpath(PREFIX + "/div" + CSIRKEMELL + "following-sibling::div/a/@nap")
    ingredients = document.xpath(PREFIX + CSIRKEMELL + "div/text()")
    prices = document.xpath(
        PREFIX + CSIRKEMELL + "child::div[contains(@class,'menu-price-field')]/div/h6/strong/text()")
    return days, ingredients, prices


def print_minimums(days, ingredients, prices):
    # count when the length are the same for days, ingredients annd prices
    if len(days) == len(ingredients) and len(ingredients) == len(prices):
        # initialize the output
        cheapest_csirkmell_at_weekdays = {day.name: ['Nincs', HIGH_PRICE] for day in Workdays}
        # remove the . and Ft from prices to be able to convert as integer
        meals = ((Workdays(int(day)).name, ingredient, price.replace('.', '').replace(' Ft', '')) for
                 day, ingredient, price
                 in
                 zip(days, ingredients, prices))

        # Add cheaper meal to each day
        for meal in meals:
            # replace the initial data if the actual price is less
            if cheapest_csirkmell_at_weekdays[meal[0]][1] > int(meal[2]):
                cheapest_csirkmell_at_weekdays[meal[0]][0] = meal[1]
                cheapest_csirkmell_at_weekdays[meal[0]][1] = int(meal[2])

        print(cheapest_csirkmell_at_weekdays)
    else:
        raise Exception('Cannot print cheapest for all day',
                        'different length in days, ingredients, prices lists: ' + str(len(days)) + ', ' + str(len(
                            ingredients)) + ', ' + str(len(prices)))


# fetch the whole html
browser = get_browser()
body = browser.find_element(By.TAG_NAME, 'html')
scroll_down_to_end()

# get the whole html
html_page = browser.page_source
time.sleep(2)
# replacing <br> is required to avoid counting multiple times the csirkemell text in case of ingredients
document = html.fromstring(html_page.replace('<br>', ''))

# get data from html and print output
days, ingredients, prices = extract_data()
print_minimums(days, ingredients, prices)

browser.quit()

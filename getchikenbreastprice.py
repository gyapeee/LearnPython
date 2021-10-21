import scrapy
import sys

# Test Results - C__git_tms-4_selenium_testng-local_xml.html
#//em[@class='status'][text()='error']/..

class GetChickenBreastPrice(scrapy.Spider):
    name = 'get_chickenbrest_price_spider'
    #start_urls = [arg for arg in sys.argv]
    start_urls = [r"https://www.teletal.hu/etlap/45 "]
    print(start_urls)

    def parse(self, response):
        for price in response.xpath("//div[contains(@class,'menu-card-5-day')]/div[contains(@class,'menu-cell-text')][contains(normalize-space(),'csirkemell')]/child::div[contains(@class,'menu-price-field')]/div/h6/strong/text()"):
            yield {'price': price}
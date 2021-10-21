import scrapy


# //div[contains(@class,'menu-card-5-day')]/div[contains(@class,'menu-cell-text')][contains(normalize-space(),'csirkemell')]/child::div[contains(@class,'menu-price-field')]/div/h6/strong/text()

class GetChickenBreastPrice(scrapy.Spider):
    name = 'get_chickenbrest_price_spider'
    #start_urls = [arg for arg in sys.argv]
    start_urls = [r"https://www.teletal.hu/etlap/45 "]
    print(start_urls)

    def parse(self, response):
        for price in response.xpath("/html").extract():
            yield {'price': price}
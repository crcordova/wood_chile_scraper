import scrapy
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from wood_chile_scraper.items import WoodChileScraperItem
from bs4 import BeautifulSoup

class SodimacSpider1(scrapy.Spider):
    name = "sodimac1"
    start_urls = [
        'https://sodimac.falabella.com/sodimac-cl/search?Ntt=pino+cepillado&facetSelected=true&f.product.brandName=generico&store=sodimac&subdomain=sodimac',
    ]

    rules = {
        # Rule(LinkExtractor(allow=(), restrict_xpaths=('//div[@class="jsx-4001457643 search-results-4-grid-pod"')),callback= 'parse', follow=False)
        Rule(LinkExtractor(allow=(), restrict_xpaths=('//*[@id="testId-searchResults-products"]')),callback= 'parse', follow=True)
    }
    def parse(self, response):
        products = response.xpath('//*[@id="testId-searchResults-products"]//a/@href').getall()
        # products = response.xpath("//a/@href").getall()
        # item = WoodChileScraperItem()
        # print(f"Type: {type(products)}")
        print(f"LEN: {len(products)}")
        for product in products:
            # item['nombre'] = product
            if product=="":
                pass
            else:
                yield scrapy.Request(product, callback = self.parse_product)
        # print(f"ACA LOS PRODUCSTS XPATH: {products}")
        # yield item

    def parse_product(self, response):
        item = WoodChileScraperItem()
        item['nombre'] = response.xpath("/html/body/div[1]/div/section/div[1]/div[1]/div[2]/section[2]/div[1]/div[2]/h1/div/text()").extract()[0]
        item['precio'] = response.xpath("/html/body/div[1]/div/section/div[1]/div[1]/div[2]/section[2]/div[2]/div/div[2]/div[1]/div[1]/ol/li/div/span/text()").extract()[0]
        item['id'] = response.xpath("/html/body/div[1]/div/section/div[1]/div[1]/div[2]/section[2]/div[1]/div[1]/div[2]/span/text()").extract()[0]
        item['peso'] = response.xpath("/html/body/div[1]/div/section/div[1]/div[8]/div/div/div[1]/section/div[2]/table/tbody/tr[5]/td[2]/text()").extract()[0]
        yield (item)


class SodimacSpider(scrapy.Spider):
    name = "sodimac"
    start_urls = [
        "https://sodimac.falabella.com/sodimac-cl/product/110326673/2-x-3-x-3,20-m-Pino-cepillado-seco/110326676?exp=sodimac",
        "https://sodimac.falabella.com/sodimac-cl/product/110282397/2-x-4-x3,20-m-Pino-cepillado-seco/110282401?exp=sodimac",
        "https://sodimac.falabella.com/sodimac-cl/product/110284602/1-x-5-x-3,20-m-Pino-cepillado-seco/110284604?exp=sodimac",
        "https://sodimac.falabella.com/sodimac-cl/product/110327420/1-x-2-x-3,20-m-Pino-cepillado-seco/110327424?exp=sodimac",
        "https://sodimac.falabella.com/sodimac-cl/product/110285532/1-x-4-x-3,20-m-Pino-cepillado-seco/110285534?exp=sodimac",
        "https://sodimac.falabella.com/sodimac-cl/product/110293067/2-x-2-x-3,20-m-Pino-cepillado-seco/110293071?exp=sodimac",
        "https://sodimac.falabella.com/sodimac-cl/product/110288271/2-x-5-x-3,20-m-Pino-cepillado-seco/110288296?exp=sodimac",
        "https://sodimac.falabella.com/sodimac-cl/product/110330352/1-x-10-x-3,20-m-Pino-cepillado-seco/110330367?exp=sodimac",
        "https://sodimac.falabella.com/sodimac-cl/product/110322002/2-x-10-x-3,20-m-Pino-cepillado-seco/110322007?exp=sodimac",
        "https://sodimac.falabella.com/sodimac-cl/product/110314701/1-x-8-x-3,20-m-Pino-cepillado-seco/110314729?exp=sodimac",
        "https://sodimac.falabella.com/sodimac-cl/product/110300404/1-x-6-x-3,20-m-Pino-cepillado-seco/110300409?exp=sodimac",
        "https://sodimac.falabella.com/sodimac-cl/product/110290622/2-x-6-x-3,20-m-Pino-cepillado-seco/110290652?exp=sodimac",
        "https://sodimac.falabella.com/sodimac-cl/product/110319423/2-x-8-x-3,20-m-Pino-cepillado-seco/110319437?exp=sodimac",
    ]

    def parse(self, response):
        item = WoodChileScraperItem()
        item['nombre'] = response.xpath("/html/body/div[1]/div/section/div[1]/div[1]/div[2]/section[2]/div[1]/div[2]/h1/div/text()").extract()[0]
        item['precio'] = response.xpath("/html/body/div[1]/div/section/div[1]/div[1]/div[2]/section[2]/div[2]/div/div[2]/div[1]/div[1]/ol/li/div/span/text()").extract()[0]
        item['id'] = response.xpath("/html/body/div[1]/div/section/div[1]/div[1]/div[2]/section[2]/div[1]/div[1]/div[2]/span/text()").extract()[0]
        item['peso'] = response.xpath("/html/body/div[1]/div/section/div[1]/div[8]/div/div/div[1]/section/div[2]/table/tbody/tr[5]/td[2]/text()").extract()[0]
        yield (item)

class EasySpider(scrapy.Spider):
    name = "easy"
    start_urls = ["https://www.easy.cl/pino%20cepillado?_q=pino%20cepillado&map=ft"]
    # rules = {
    #     Rule(LinkExtractor(allow=(), restrict_xpaths=('//*[@id="gallery-layout-container"]')),callback= 'parse', follow=False)
    # }

    def parse(self, response):
        products = response.selector.xpath('/html/body/div[2]/div/div[1]/div/div[4]/div/div/section/div[2]/div/div[4]/div/div[2]/div/div[3]')
        # response.xpath("//a[@class='au-target']/@href")
        item = WoodChileScraperItem()
        # item['nombre'] = response.xpath('/html/body/div[2]/div/div[1]/div/div/div/div[5]/div/div[3]/div/section/div/div[3]/div/div[2]/div/div/div/h1/span').extract()
        print(f"ACA :{(len(products))}")

        yield item

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WoodChileScraperItem(scrapy.Item):
    # define the fields for your item here like:
    nombre = scrapy.Field()
    precio = scrapy.Field()
    id = scrapy.Field()
    peso = scrapy.Field()
    # pass

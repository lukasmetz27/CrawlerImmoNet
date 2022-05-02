# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ImmonetItem(scrapy.Item):
    # define the fields for your item here like:
    typ = scrapy.Field()
    ort = scrapy.Field()
    price = scrapy.Field()
    sqm = scrapy.Field()
    rooms = scrapy.Field()
pass

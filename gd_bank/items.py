# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GdBankItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    name = scrapy.Field()
    around = scrapy.Field()
    address = scrapy.Field()
    service_time = scrapy.Field()
    phone_number = scrapy.Field()
    province = scrapy.Field()
    type = scrapy.Field()
    created_time = scrapy.Field()
    pass




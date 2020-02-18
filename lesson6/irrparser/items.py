# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst, MapCompose
import re

def getFeatures(values):
    for value in values:
        match = re.findall('[0-9]]',value)
        return match

class IrrparserItem(scrapy.Item):
    # define the fields for your item here like:
    _id = scrapy.Field()
    name = scrapy.Field(output_processor=TakeFirst())
    features = scrapy.Field(input_proccessor=MapCompose(getFeatures))
    description = scrapy.Field()
    images = scrapy.Field()
    pass

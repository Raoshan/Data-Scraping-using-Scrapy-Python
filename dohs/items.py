# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
    
class DohsItem(scrapy.Item):
    # define the fields for your item here like:
    lastName = scrapy.Field()
    firstName = scrapy.Field()
    middleName = scrapy.Field()
    listedOn = scrapy.Field()
    address1 = scrapy.Field()
    address2 = scrapy.Field()
    city = scrapy.Field()
    stateProvince = scrapy.Field()
    postalCode = scrapy.Field()
    country  = scrapy.Field()
    externalSources= scrapy.Field()
    type = scrapy.Field()




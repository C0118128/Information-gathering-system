# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyProjectItem(scrapy.Item):
    a_url = scrapy.Field()
    name = scrapy.Field()
    url = scrapy.Field()
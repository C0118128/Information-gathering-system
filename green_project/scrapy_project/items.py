# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyProjectItem(scrapy.Item):
    s1_name = scrapy.Field()
    s2_a_url = scrapy.Field()
    s3_location = scrapy.Field()
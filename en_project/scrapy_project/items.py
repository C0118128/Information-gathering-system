# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyProjectItem(scrapy.Item):
    企業情報_1_名前 = scrapy.Field()
    企業情報_2_サイト = scrapy.Field()
    企業情報_3_求人サイト企業情報 = scrapy.Field()
    連絡先_1_住所 = scrapy.Field()
    連絡先_2_担当者 = scrapy.Field()
    連絡先_3_電話番号 = scrapy.Field()
    連絡先_4_メールアドレス = scrapy.Field()
    
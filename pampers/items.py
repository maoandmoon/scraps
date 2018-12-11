# coding: utf-8
""" Define here the models for your scraped items.
See documentation in:
https://doc.scrapy.org/en/latest/topics/items.html """
import scrapy


class PampersItem(scrapy.Item):
    title = scrapy.Field()
    category = scrapy.Field()
    description = scrapy.Field()
    price = scrapy.Field()

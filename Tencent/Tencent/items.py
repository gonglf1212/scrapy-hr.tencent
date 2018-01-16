# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    # define the fields for your item here like:
    # 岗位名称
    title = scrapy.Field()
    time = scrapy.Field()
    url = scrapy.Field()
    category = scrapy.Field()
    num = scrapy.Field()
    area = scrapy.Field()

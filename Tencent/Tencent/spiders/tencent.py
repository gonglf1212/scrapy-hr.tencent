# -*- coding: utf-8 -*-
import scrapy
from Tencent.items import TencentItem

class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['tencent.com']
    baseURL = "http://hr.tencent.com/"
    start_urls = [baseURL + "/position.php?start=0"]
    def parse(self, response):
        node_list = response.xpath("//tr[@class='odd' or @class='even']")
        for index, node in enumerate(node_list):
            items = TencentItem()
            title = node.xpath("./td[1]/a/text()").extract()[0]
            url = node.xpath("./td[1]/a/@href").extract()[0]
            if len(node.xpath("./td[2]/text()")):
                category = node.xpath("./td[2]/text()").extract()[0]
            else:
                category = ""
            num = node.xpath("./td[3]/text()").extract()[0]
            area = node.xpath("./td[4]/text()").extract()[0]
            time = node.xpath("./td[5]/text()").extract()[0]
            items['title'] = title
            items['url'] = url
            items['category'] = category
            items['num'] = num
            items['area'] = area
            items['time'] = time
            yield items
        is_next = response.xpath("//a[@id='next' and @class='noactive']").extract()
        if not len(is_next):
            node_next = response.xpath("//a[@id='next']/@href").extract()[0]
            url = self.baseURL + node_next
            print(url)
            yield scrapy.Request(url, callback=self.parse)
            


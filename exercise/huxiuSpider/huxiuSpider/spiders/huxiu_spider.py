#!/anaconda3/bin/env python27
# -*- encoding: utf-8 -*-

"""
Topic: sample
Dsec:
"""
import scrapy
from ..items import HuxiuItem

class HuxiuSpider(scrapy.Spider):
    name = "huxiu"
    allowed_domains = ["huxiu.com"]
    start_url = [
        "http://www.huxiu.com/index.php"
    ]

    def parse(self, response):
        for sel in response.xpath('//div[@class="mod-info-flow"]/div/div[@class="mob-ctt"]'):
            item = HuxiuItem()

            item["title"] = sel.xpath('h2/a/text()')[0].extract()
            item["link"] = sel.xpath('h2/a/@href')[0].extract()
            url = response.urljoin(item["link"])
            item["desc"] = sel.xpath('div[@class="mob-sub"]/text()')[0].extract()
            print item["title"], item["link"], item["desc"]
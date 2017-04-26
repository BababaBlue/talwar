#!/usr/bin/env python
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class MachineSpider(CrawlSpider):
    name = 'weedmaps'
    allowed_domains = ['weedmaps.com']
    start_urls = ['https://weedmaps.com/dispensaries/shakeandbake']

    rules = [
        Rule(LinkExtractor(allow=r'/dispensaries/'), callback='parse_hours')
    ]

    def parse_hours(self, response):
        print response.url

        for hours in response.css('span[itemid="#store"] div.row.hours-row div.col-md-9'):
            print hours.xpath('text()').extract()

a=MachineSpider()
a.parse_hours

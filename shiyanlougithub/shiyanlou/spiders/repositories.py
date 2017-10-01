# -*- coding: utf-8 -*-
import scrapy
import requests
from datetime import datetime
from shiyanlou.items import RepositoryItem

class RepositoriesSpider(scrapy.Spider):
    name = 'repositories'
    start_urls=['']
    @property
    def start_urls(self):
        url_tmpl = ('https://github.com/shiyanlou?page={}&tab=repositories')
        return (url_tmpl.format(i) for i in range(1, 5))

    def parse(self, response):
        for house in response.xpath('//*[@id="user-repositories-list"]/ul/li'):
            namelist = house.xpath('.//div[1]/h3/a/text()').re('\n        (.+)')
            name = "".join(namelist)
            str1 = (str(house.xpath('.//div[3]/relative-time').extract()))
            time1 = str1.split("\"")

            item = RepositoryItem()
            item['name'] = name
            item['update_time'] = time1[1]
            repository_url = response.urljoin(house.xpath('.//div[1]/h3/a/@href').extract()[0])
            request = scrapy.Request(repository_url, callback=self.parse_content)
            request.meta['item'] = item
            yield request

    def parse_content(self, response):
        item = response.meta['item']
        collection = response.xpath('(//span[@class="num text-emphasized"])/text()').re('\d')
        item['commits'] = collection[0]
        item['branches'] = collection[1]
        item['releases'] = collection[2]
        yield item

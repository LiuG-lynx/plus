import scrapy

class githubSpider(scrapy.Spider):
    name = 'warehouse-spider'

    def start_requests(self):
        url_tmpl = 'https://github.com/shiyanlou?page={}&tab=repositories'
        urls = (url_tmpl.format(i) for i in range(1,4))
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self,response):
        for house in response.xpath('//*[@id="user-repositories-list"]/ul/li'):
            namelist = house.xpath('.//div[1]/h3/a/text()').re('\n        (.+)')
            name = "".join(namelist)

            str1 = (str(house.xpath('.//div[3]/relative-time').extract()))
            time1 = str1.split("\"")
            yield {
                "name" : name,
                "update_time" : time1[1]
                }

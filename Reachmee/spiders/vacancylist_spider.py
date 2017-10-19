import scrapy
from Reachmee.items import ReachmeeItem


class VacancyTitleSpider(scrapy.Spider):
    name = "vacancylist"
    start_urls = {'https://www.monster.se/jobb/sok/'}

    def parse(self, response):
        #for href in response.xpath('//link[re:test(@rel, "next")]//@href'):
         #   yield response.follow(href, self.parse)
        for role in response.css("article.js_result_row"):
            item = ReachmeeItem()
            #item['jobTitle'] = role.css('.jobTitle a::attr(title)').extract()
            item['company'] = role.css('.company a::attr(title)').extract()
            item['location'] = role.css('//div[@class=$val]/a/text()', val='location').extract()
            yield item

import scrapy
from Reachmee.items import ReachmeeItem


class VacancyTitleSpider(scrapy.Spider):
    name = "stepstones"
    start_urls = {'https://www.stepstone.se/lediga-jobb-i-hela-sverige/'}

    def parse(self, response):
        #for href in response.xpath('//link[re:test(@rel, "next")]//@href'):
        #    yield response.follow(href, self.parse)
        for role in response.xpath('//section[@id=$val]', val='list-style-foongus'):
            item = ReachmeeItem()
            #item['jobTitle'] = role.css('.description a::attr(title)').extract()
            item['company'] = role.xpath('//span[@class=$val]/a/text()', val='text-bold').extract()
            #item['location'] = role.xpath('//div[@class=$val]/a/text()', val='location').extract_first().strip()
            yield item

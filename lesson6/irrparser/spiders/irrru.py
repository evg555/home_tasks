# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import HtmlResponse
from lesson6.irrparser.items import IrrparserItem
from scrapy.loader import ItemLoader


class IrrruSpider(scrapy.Spider):
    name = 'irrru'
    allowed_domains = ['irr.ru']
    start_urls = ['https://irr.ru/real-estate/rent/search/tab=users/rent_period=3674653711/']



    def parse(self, response: HtmlResponse):
        page = response.css("a.pagination__pagesLink::text").extract()
        last_number = int(page[-1]) + 1

        for i in range(1, last_number):
            next_link = response.url + f"page{i}/"
            yield response.follow(next_link,callback=self.parse_page)

    def parse_page(self,response: HtmlResponse):
        items = response.css('a.listing__itemTitle::attr(href)').extract()

        for link in items:
            yield response.follow(link, callback=self.parse_item)

    def parse_item(self, response: HtmlResponse):
        # name = response.css("h1.productPage__title::text").extract_first()
        # features = response.css("span.productPage__characteristicsItemValue::text").extract()
        # description = response.css("p.productPage__descriptionText::text").extract()
        # images = response.css("img.lineGallery__image::attr(src)").extract()

        loader = ItemLoader(item=IrrparserItem(), response=response)
        loader.add_css('name',"h1.productPage__title::text")
        loader.add_css('features', "span.resproductPage__characteristicsItemValue::text")
        loader.add_css('description', "p.productPage__descriptionText::text")
        loader.add_css('images', "img.lineGallery__image::attr(src)")
        yield loader.load_item()
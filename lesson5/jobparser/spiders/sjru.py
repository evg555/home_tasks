# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import HtmlResponse
from lesson5.jobparser.items import JobparserItem

class SjruSpider(scrapy.Spider):
    name = 'sjru'
    allowed_domains = ['superjob.ru']
    start_urls = [f'https://superjob.ru/vacancy/search?keywords=python']

    def parse(self, response: HtmlResponse):
        next_page = response.css('a.f-test-button-dalshe::attr(href)').extract_first()
        yield response.follow(next_page, callback=self.parse)

        vacancy = response.css(
            'div.f-test-vacancy-item a.icMQ_::attr(href)'
        ).extract()

        for link in vacancy:
            yield response.follow(link, callback=self.vacancy_parse)

    def vacancy_parse(self, response: HtmlResponse):
        source = 'sj.ru'
        title = response.css('div.f-test-vacancy-base-info h1.s1nFK::text').extract_first()
        salary = response.xpath("//span[@class='_3mfro _2Wp8I ZON4b PlM3e _2JVkc']/text() | //span[@class='_3mfro _2Wp8I ZON4b PlM3e _2JVkc']//span/text()").extract()
        salary_parse = self.salary_parse(salary)

        yield JobparserItem(
            source=source,
            title=title,
            link=response.url,
            salary_min=salary_parse['min_salary'],
            salary_max=salary_parse['max_salary'],
            currency=salary_parse['currency']
        )

    def salary_parse(self, salary):
        item = {}

        if not salary:
            item['min_salary'] = False
            item['max_salary'] = False
            item['currency'] = False
        else:
            if len(salary) > 2:
                if salary[0].lower().strip() == 'от':
                    item['min_salary'] = int(salary[2].replace(u'\xa0', u''))
                    item['max_salary'] = 999999999999
                    item['currency'] = salary[4]
                elif salary[0].lower() == 'до':
                    item['min_salary'] = 0
                    item['max_salary'] = int(salary[2].replace(u'\xa0', u''))
                    item['currency'] = salary[4]
                else:
                    item['min_salary'] = int(salary[0].replace(u'\xa0', u''))
                    item['max_salary'] = int(salary[4].replace(u'\xa0', u''))
                    item['currency'] = salary[6]
            else:
                item['min_salary'] = False
                item['max_salary'] = False
                item['currency'] = False

        return item

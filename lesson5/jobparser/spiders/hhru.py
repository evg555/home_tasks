# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import HtmlResponse
from lesson5.jobparser.items import JobparserItem

class HhruSpider(scrapy.Spider):
    name = 'hhru'
    allowed_domains = ['hh.ru']
    start_urls = [f'https://hh.ru/search/vacancy?area=&st=searchVacancy&text=python']

    def parse(self, response: HtmlResponse):
        next_page = response.css('a.HH-Pager-Controls-Next::attr(href)').extract_first()
        yield response.follow(next_page, callback=self.parse)

        vacancy = response.css(
            'div.vacancy-serp div.vacancy-serp-item div.vacancy-serp-item__row_header a.bloko-link::attr(href)'
        ).extract()

        for link in vacancy:
            yield response.follow(link, callback=self.vacancy_parse)

    def vacancy_parse(self, response: HtmlResponse):
        title = response.css('div.vacancy-title h1.header::text').extract_first()
        employer = response.css('div.vacancy-company a.vacancy-company-name span::text').extract()
        employer = "".join(employer)
        city = response.css('div.vacancy-company p[data-qa=vacancy-view-location]::text').extract_first()
        salary = response.css('div.vacancy-title p.vacancy-salary::text').extract()
        salary_parse = self.salary_parse(salary)

        yield JobparserItem(
            title=title,
            link=response.url,
            employer=employer,
            city=city,
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
                    item['min_salary'] = int(salary[1].replace(u'\xa0', u''))

                    if salary[2].lower().strip() == 'до':
                        item['max_salary'] = int(salary[3].replace(u'\xa0', u''))
                        item['currency'] = salary[5]
                    else:
                        item['max_salary'] = 999999999999
                        item['currency'] = salary[3]
                if salary[0].lower() == 'до':
                    item['min_salary'] = 0
                    item['max_salary'] = int(salary[1].replace(u'\xa0', u''))
                    item['currency'] = salary[3]
            else:
                item['min_salary'] = False
                item['max_salary'] = False
                item['currency'] = False

        return item

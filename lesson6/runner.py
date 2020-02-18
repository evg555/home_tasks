# Я буду использовать объявления с сайта Из рук в руки https://irr.ru/
# Буду собирать данные по аренде квартир от частников в Москве за месяц
# Данные для парсинга:
# - количество комнат
# - общая площадь
# - жилая площадь
# - этаж и количество этажей
# - цена за месяц
# - описание
# - фото

from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from lesson6.irrparser.spiders.irrru import IrrruSpider
from lesson6.irrparser import settings

if __name__ == '__main__':
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)
    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(IrrruSpider)
    process.start()




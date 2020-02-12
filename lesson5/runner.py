from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from lesson5.jobparser import settings
from lesson5.jobparser.spiders.hhru import HhruSpider
# from jobparser.spiders.hhru import SjruSpider


if __name__ == '__main__':
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)
    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(HhruSpider)
    # process.crawl(SjruSpider)
    process.start()
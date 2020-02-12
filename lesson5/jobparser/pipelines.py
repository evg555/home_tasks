# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient

class JobparserPipeline(object):
    def __init__(self):
        client = MongoClient('localhost',27017)
        self.mongobase = client.jobs

    def process_item(self, item, spider):
        collection = self.mongobase[spider.name]
        collection.update_one({'link': item['link']},{'$set': item},upsert=True)

        return item

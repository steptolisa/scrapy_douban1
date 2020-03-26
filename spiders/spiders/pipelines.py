# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from . import settings
import pymongo

class SpidersPipeline(object):

    def __init__(self):
        # 获取setting主机名、端口号和数据库名
        host = settings.MONGODB_HOST
        port = settings.MONGODB_PORT
        dbname = settings.MONGODB_DBNAME
        docname = settings.MONGODB_DOCNAME

        # pymongo.MongoClient(host, port) 创建MongoDB链接
        client = pymongo.MongoClient(host=host, port=port)

        # 数据库
        mdb = client[dbname]
        # 数据的表名
        self.post = mdb[docname]

    def process_item(self, item, spider):
        data = dict(item)
        self.post.insert(data)
        return item
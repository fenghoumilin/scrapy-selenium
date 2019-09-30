# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import time

class GdBankPipeline(object):
    def __init__(self):
        dbparams = {
            'host': '127.0.0.1',
            'port': 3306,
            'user': 'root',
            'password': 'root',
            'database': 'gdjs',
            'charset': 'utf8'
        }
        self.conn = pymysql.connect(**dbparams)
        self.cursor = self.conn.cursor()
        self._sql = None
    def process_item(self, item, spider):
        self.cursor.execute(self.sql, (item['url'], item['network'], item['address'], item['service_time'], item['phone_number'], item['province'], item['type'], item['created_time']))
        self.conn.commit()
        return item
    @property
    def sql(self):
        if not self._sql:
            self._sql = """
            insert into network(id, url, network, address, service_time, phone_number, province, `type`, created_time) 
            values (null, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            return self._sql
        return self._sql

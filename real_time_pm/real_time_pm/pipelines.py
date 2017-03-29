# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
# import MySQLdb.cursors
from twisted.enterprise import adbapi
from scrapy.utils.project import get_project_settings  # from scrapy.conf import settings
from real_time_pm.items import ExecuteSql

import sys
reload(sys)
sys.setdefaultencoding('utf8')

class RealTimePmPipeline(object):
    def __init__(self):
        DBKWARGS = get_project_settings().get('DBKWARGS')
        self.dbpool = adbapi.ConnectionPool('MySQLdb', **DBKWARGS)

    pass
    # def _conditional_insert(self,tx,item):
    #     # self.sql = 'insert into real_time_pm(`run_time`,`real_time`,`city`,`monitor_station`,`AQI`,`lev`,`top_pm`,`pm25`,`pm10`,`CO`,`NO2`,`O3_1h`,`O3_8h`,`SO2`) ' \
    #     #       'values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    #     # parems = (item['run_time'],item['run_time'],item['city'],item['monitor_station'],item['AQI'],item['lev'],item['top_pm'],item['pm25'],item['pm10'],item['CO'],item['NO2'],item['O3_1h'],item['O3_8h'],item['SO2'])
    #     tx.execute(self.sql,(item['run_time'],item['real_time'],item['city'],item['monitor_station'],item['AQI'],item['lev'],item['top_pm'],item['pm25'],item['pm10'],item['CO'],item['NO2'],item['O3_1h'],item['O3_8h'],item['SO2']))
    #
    # def process_item(self,item,spider):
    #     if isinstance(item,ExecuteSql):
    #         self.dbpool.runInteraction(self._conditional_insert,item)
    #     else:
    #         self._conditional_insert(item)

class RealTimePmPipelines(object):
    def process_item(self, item, spider):
        print '--------------------->',item
        return item


class SqlPipline(object):
    def __init__(self):
        DBKWARGS = get_project_settings().get('DBKWARGS')
        self.conn = MySQLdb.connect(**DBKWARGS)
        self.cur = self.conn.cursor()
        self.sql = "insert into real_time_pm(`run_time`,`real_time`,`city`,`monitor_station`,`AQI`,`lev`,`top_pm`,`pm25`,`pm10`,`CO`,`NO2`,`O3_1h`,`O3_8h`,`SO2`) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    def process_item(self, item, spider):
        # if isinstance(item,ExecuteSql):
        #     self.conn.commit()
        # else:
        #     self.cur.execute(self.sql,(item['run_time'],item['run_time'],item['city'],item['monitor_station'],item['AQI'],item['lev'],item['top_pm'],item['pm25'],item['pm10'],item['CO'],item['NO2'],item['O3_1h'],item['O3_8h'],item['SO2']))


        self.cur.execute(self.sql,(item['run_time'],item['run_time'],item['city'],item['monitor_station'],item['AQI'],item['lev'],item['top_pm'],item['pm25'],item['pm10'],item['CO'],item['NO2'],item['O3_1h'],item['O3_8h'],item['SO2']))
        self.conn.commit()

# -*- coding:utf-8 -*-

import os
import sys
import time
import datetime

import pymysql.cursors

project_path = os.path.dirname(os.path.abspath(__file__ + "/.."))
sys.path.insert(0, project_path)


# import the spiders you want to run
from spiders.stations import StationsSpider


# scrapy api imports
from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from scrapy.utils.project import get_project_settings


settings = get_project_settings()
crawler = CrawlerProcess(settings)


def sleep(secs):
    d = defer.Deferred()
    reactor.callLater(secs, d.callback, None)
    return d


@defer.inlineCallbacks
def crawl():
    conn = pymysql.connect(host='localhost', port=3306,
                           user='12306_test',
                           password='12306_test',
                           db='12306-test',
                           charset='utf8')


    station_count = 30

    first = True

    last_turn = -1
    while True:
        n = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        s = time.time()
        turn = int(s / 86400)
        if turn == last_turn:
            sleep(5)
            continue

        print "new turn", turn, n
        last_turn = turn


        with conn.cursor() as cursor:
            cursor.execute("INSERT IGNORE INTO `turns` VALUES (%s, %s)", (turn, n))
        conn.commit()


        if first or turn % station_count == 0:
            yield crawler.crawl(StationsSpider, turn)


        first = False
        e = time.time()
        left = int(86400 - e + s)

        if left > 0:
            print "sleep", left
            sleep(left)


    print "crawler over"

crawl()
crawler.start()


















# -*- coding:utf-8 -*-
import time
import datetime
import json
import urllib

import pymysql.cursors

import scrapy
from scrapy.http.request import Request
from project34.items import BriefDeltaItem
from project34.items import CodeItem
from project34.items import TicketItem
from project34.items import CommitItem

class TicketsSpider(scrapy.Spider):
    name = 'TicketsSpider'

    custom_settings = {
        'ITEM_PIPELINES': {
            'project34.pipelines.TicketSQLPipeline': 300,
        },
        'DOWNLOADER_MIDDLEWARES':{
            'project34.middle.DownloaderMiddleware': 500,
        },
        'DUPEFILTER_CLASS': "project34.filter.URLTurnFilter",
        'JOBDIR': "s/tickets",

    }

    def __init__(self, *a, **kw):
        super(TicketsSpider, self).__init__(self.name, **kw)
        self.turn = a[0]
        self.logger.info("%s. this turn %d" % (self.name, self.turn))

    def start_requests(self):
        yield Request("https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.8936", callback=self.parse, meta={"turn": self.turn})

    @staticmethod
    def fetch_routes():
        conn = pymysql.connect(host='localhost', port=3306,
                               user='12306_test', password='12306_test',
                               db='12306-test', charset='utf8')

        select = "select * from train_infos"

        schedules = {}
        with conn.cursor() as cursor:
            cursor.execute(select)
            for results in cursor.fetchall():
                if results[0] not in schedules:
                    schedules[results[0]] = {results[1]: results[2]}
                else:
                    schedules[results[0]][results[1]] = results[2]

        routes = {}
        for key in schedules:
            route = schedules[key]
            seq = sorted(route)
            len1 = len(seq)

            for i in range(0, len1):
                if route[seq[i]] not in routes:
                    tmp = set()
                    routes[route[seq[i]]] = tmp
                else:
                    tmp = routes[route[seq[i]]]
                for j in range(i+1, len1):
                    tmp.add(route[seq[j]])
        return routes

    def parse(self, response):
        station_str = response.body.decode("utf-8")
        stations = station_str.split(u"@")
        results = {}

        for i in range(1, len(stations)):
            station = stations[i].split(u"|")
            results[station[1]] = station[2]
            item = CodeItem()
            item["name"] = station[1]
            item["code"] = station[2]
            item["turn"] = response.meta["turn"]
            yield item

        yield CommitItem()

        routes = TicketsSpider.fetch_routes()

        url = "https://kyfw.12306.cn/otn/leftTicket/queryZ?"
        t = (datetime.datetime.now() + datetime.timedelta(days=3)).strftime("%Y-%m-%d")
        for s in routes:
            if s in results:
                code_s = results[s]
            else:
                self.logger.warning("code miss" + s)
                continue
            for e in routes[s]:
                if e in results:
                    code_e = results[e]
                else:
                    self.logger.warning("code miss" + e)
                    continue

            params = u"leftTicketDTO.train_date=" + t + u"&leftTicketDTO.from_station=" + code_s + u"&leftTicketDTO.to_station=" + code_e + u"&purpose_codes=ADULT"
            s_url = url + params

            yield scrapy.Request(url=s_url, callback=self.parse_ticket, meta={"s": s, "e": e, "turn": response.meta["turn"]})

    def parse_ticket(self, response):
        j = json.loads(response.body)

        if "data" not in j:
            self.logger.info("there is no data" + response.meta["s"] + " " + response.meta["e"])
            return

        datas = j["data"]

        for data in datas:
            try:
                info = data["queryLeftNewDTO"]
            except:
                continue

            deltaItem = BriefDeltaItem()
            deltaItem["code"] = info["station_train_code"]
            deltaItem["seat_type"] = info["seat_types"]
            deltaItem["turn"] = response.meta["turn"]
            yield deltaItem

            item = TicketItem()
            item["train_no"] = info["train_no"]
            item["start"] = info["from_station_name"]
            item["end"] = info["to_station_name"]
            item["turn"] = response.meta["turn"]

            item["swz"] = info["swz_num"]
            if item["swz"] == '--' or item["swz"] == '无':
                item["swz"] = -1

            item["tz"] = info["tz_num"]
            if item["tz"] == '--' or item["tz"] == '无':
                item["tz"] = -1

            item["zy"] = info["zy_num"]
            if item["zy"] == '--' or item["zy"] == '无':
                item["zy"] = -1

            item["ze"] = info["ze_num"]
            if item["ze"] == '--' or item["ze"] == '无':
                item["ze"] = -1

            item["gr"] = info["gr_num"]
            if item["gr"] == '--' or item["gr"] == '无':
                item["gr"] = -1

            item["rw"] = info["rw_num"]
            if item["rw"] == '--' or item["rw"] == '无':
                item["rw"] = -1

            item["yw"] = info["yw_num"]
            if item["yw"] == '--' or item["yw"] == '无':
                item["yw"] = -1

            item["rz"] = info["rz_num"]
            if item["rz"] == '--' or item["rz"] == '无':
                item["rz"] = -1

            item["yz"] = info["yz_num"]
            if item["yz"] == '--' or item["yz"] == '无':
                item["yz"] = -1

            item["wz"] = info["wz_num"]
            if item["wz"] == '--' or item["wz"] == '无':
                item["wz"] = -1

            item["qt"] = info["qt_num"]
            if item["qt"] == '--' or item["qt"] == '无':
                item["qt"] = -1

            # print item["train_no"], item["start"], item["end"], item["swz"]
            yield item
        yield CommitItem()





























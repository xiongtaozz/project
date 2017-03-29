# -*- coding:utf-8 -*-
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define,options
define('port',default=8000, help='run on given port',type=int)


class IndexHadler(tornado.web.RequestHandler):
    def get(self):
        greeting = self.get_argument('greeting','Hello')
        self.write(greeting+',friendly user!')


if __name__=='__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r'/', IndexHadler)])
    http_server = tornado.httpserver.HTTPServer(app)
    tornado.ioloop.IOLoop().instance().start()
# coding: utf-8
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.httpclient

import json

# 异步的方式去处理http的请求。
# 当去请求一个地址的时候，先建立一个长连接，处理页面，业务处理之后，通过finish关闭长连接。

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)


class IndexHandler(tornado.web.RequestHandler):
    # @tornado.web.asynchronous装饰器让Tornado保持连接开启
    @tornado.web.asynchronous
    def get(self):
        query = self.get_argument('q')
        # 实例化异步AsyncHTTPClient对象
        client = tornado.httpclient.AsyncHTTPClient()
        client.fetch("http://int.dpool.sina.com.cn/iplookup/iplookup.php?format=json&ip=" + query,
                     callback=self.on_response)
    
    # 异步AsyncHTTPClient对象的回调函数
    def on_response(self, response):
        body = json.loads(response.body)
        self.write("""
                    <div style="text-align: center">
                    <div style="font-size: 72px">%s</div>
                    <div style="font-size: 144px">%s-%s-%s</div>
                    </div>""" % (self.get_argument('q'), body['country'], body['province'], body['city']))
        # finish方法来显式地告诉Tornado关闭连接。
        self.finish()

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r"/", IndexHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

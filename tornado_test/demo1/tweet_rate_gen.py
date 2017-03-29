# coding: utf-8
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.httpclient
import tornado.gen

import json

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)


class IndexHandler(tornado.web.RequestHandler):
    # @tornado.web.asynchronous装饰器让Tornado保持连接开启
    @tornado.web.asynchronous
    # @tornado.gen.engine装饰器定义在get方法的之前,
    # 这将提醒Tornado这个方法将使用tornado.gen.Task类
    @tornado.gen.engine
    def get(self):
        query = self.get_argument('q')
        # 实例化异步AsyncHTTPClient对象
        client = tornado.httpclient.AsyncHTTPClient()
        # 使用Python的yield关键字以及tornado.gen.Task对象的一个实例，
        # 将我们想要的调用和传给该调用函数的参数传递给那个函数.
        # yield的使用返回程序对Tornado的控制，允许在HTTP请求进行中执行其他任务。
        # 当HTTP请求完成时，RequestHandler方法在其停止的地方恢复
        response = yield tornado.gen.Task(client.fetch,
                                          "http://int.dpool.sina.com.cn/iplookup/iplookup.php?format=json&ip=" + query)
        body = json.loads(response.body)
        self.write("""
                    <div style="text-align: center">
                    <div style="font-size: 72px">%s</div>
                    <div style="font-size: 144px">%s-%s-%s</div>
                    </div>""" % (self.get_argument('q'), body['country'], body['province'], body['city']))
        self.finish()

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r"/", IndexHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

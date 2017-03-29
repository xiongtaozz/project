# -*- coding:utf-8
import tornado.web
import tornado.httpclient
import tornado.httpserver
import tornado.options
import tornado.ioloop
import json
from tornado.options import options, define

define('port', default=8000, help='run on the given', type=int)


# 异步的方式去处理http的请求。
# 当去请求一个地址的时候，先建立一个长连接，处理页面，业务处理之后，通过finish关闭长连接
# 定义相应页面http的Herder
class IndexHander(tornado.web.RequestHandler):

    # @tornado.web.asynchronous装饰器让Tornado保持连接开启 (闭包)
    @tornado.web.asynchronous
    def get(self):
        # 接收传入参数
        query = self.get_argument('q')
        # 创建实例异步 Asynchronous对象
        client = tornado.httpclient.AsyncHTTPClient()
        client.fetch("http://int.dpool.sina.com.cn/iplookup/iplookup.php?format=json&ip=" + query,
                     callback=self.no_response)

    # 异步AsyncHTTPClient对象的回调函数
    def no_response(self, response):
        body = json.loads(response.body)
        self.write('''
                <div style="text-align: center">
                <div style="font-size: 72px">%s
                </div><div style="font-size: 144px">
                %s-%s-%s
                </div>
                </div>
                ''' % (self.get_argument('q'), body['country'], body['province'], body['city'])
        )
        # finish方法来显式地告诉Tornado关闭连接。
        self.finish()

# 创建 Application 类型实例
application = tornado.web.Application([
    (r'/', IndexHander)
])

if __name__ == '__main__':
    # 读取命令行参数并将处理结果显示到命令行
    tornado.options.parse_command_line()
    # 创建httpserver 实例
    http_server = tornado.httpserver.HTTPServer(application)
    # 设置监听
    http_server.listen(options.port)
    # 启动服务
    tornado.ioloop.IOLoop.instance().start()
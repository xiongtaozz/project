# coding: utf-8
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.httpclient
import json

from tornado.options import define, options


# 同步的方式去处理http的请求。
# 当去请求一个地址的时候，先建立连接，关闭连接。
# 定义服务启动端口
define("port", default=8000, help="run on the given port", type=int)


# 定义响应页面http请求的Handler
class IndexHandler(tornado.web.RequestHandler):
    # 处理Get请求
    def get(self):
        # 接	收传入参数
        query = self.get_argument('q')
        # 实例化同步httpclient对象
        client = tornado.httpclient.HTTPClient()
        # 访问远程接口  业务:判断IP地址输入那个地方
        response = client.fetch("http://int.dpool.sina.com.cn/iplookup/iplookup.php?format=json&ip=" + query)
        # 转换为json对象
        body = json.loads(response.body)
        # 将处理的结果写入到HTTP响应中
        self.write("""
            <div style="text-align: center">
            <div style="font-size: 72px">%s</div>
            <div style="font-size: 144px">%s-%s-%s</div>
            </div>""" % (query, body['country'], body['province'], body['city']))

if __name__ == "__main__":
    # 读取命令行参数并将处理结果显示到命令行
    tornado.options.parse_command_line()
    # 创建Application类的实例，定义url特定的url由哪个Handler来处理
    app = tornado.web.Application(handlers=[(r"/", IndexHandler)])
    # 创建httpserver实例
    http_server = tornado.httpserver.HTTPServer(app)
    # 设置监听
    http_server.listen(options.port)
    # 启动服务
    tornado.ioloop.IOLoop.instance().start()

# -*- coding:utf-8 -*-
import tornado.web
import tornado.httpclient
import tornado.httpserver
import tornado.options
import tornado.ioloop
import json
from tornado.options import define, options

# 同步的方式去处理http请求
# 当去请求一个地址的时候,先建立连接,关闭连接
# 定义服务器启动端口
define('port', default=8000, help='run on the given', type=int)


# 定义相应页面http的Hander
class IndexHander(tornado.web.RequestHandler):

    # 处理get请求
    def get(self):
        # 接收传入参数 get post
        query = self.get_argument('q')  # req.GET.get()
        # 实例化同步httpclient对象
        client = tornado.httpclient.HTTPClient()
        # 访问远程接口
        response = client.fetch('http://int.dpool.sina.com.cn/iplookup/iplookup.php?format=json&ip=' + query)
        # 转换为json对象
        body = json.loads(response.body)
        # 将处理的结果写入到HTTP相应中
        self.write('''
            <div style="text-align: center">
            <div style="font-size: 72px">%s
            </div><div style="font-size: 144px">
            %s-%s-%s
            </div>
            </div>
            ''' % (query, body['country'], body['province'], body['city'])
        )
# 创建Application类型的实例
application = tornado.web.Application([
    (r'/', IndexHander),
])

if __name__ == '__main__':
    # 读取命令行参数并将处理结果显示到命令行
    tornado.options.parse_command_line()
    # 创建httpserver实例
    http_server = tornado.httpserver.HTTPServer(application)
    # 设置监听
    http_server.listen(options.port)
    # 启动服务
    tornado.ioloop.IOLoop.instance().start()

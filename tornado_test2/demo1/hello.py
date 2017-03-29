# coding:utf-8

import tornado.httpclient
import tornado.ioloop
import tornado.web


# views
class MainHander(tornado.web.RequestHandler):

    def get(self):
        self.write('Hello word')

# urls
application = tornado.web.Application([
    (r'/', MainHander),
])

if __name__ == '__main__':
    # 监听
    application.listen(8888)
    # 启动服务
    tornado.ioloop.IOLoop.instance().start()

# -*- coding: utf-8 -*-
import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options
from uuid import uuid4


# ShoppingCart类来维护我们的库存中商品的数量，以及把商品加入购物车的购物者列表
class ShoppingCart(object):
        # 库存总数
        totalInventory = 10
        callbacks = []
        carts = {}

        # 注册回调函数到回调函数列表
        def register(self, callback):
            self.callbacks.append(callback)

        # 添加到购物车，并通知回调函数
        def moveItemToCart(self, session):
            if session in self.carts:
                return
            self.carts[session] = True
            self.notifyCallbacks()

        # 移除购物车，并更新回调函数列表
        def removeItemFromCart(self, session):
            if session not in self.carts:
                return
            del(self.carts[session])
            self.notifyCallbacks()

        # 更新回调函数列表
        def notifyCallbacks(self):
            self.callbacks = [c for c in self.callbacks if self.callbackHelper(c)]

        # 执行回调函数
        def callbackHelper(self, callback):
            callback(self.getInventoryCount())
            return False

        # 得到库存数量
        def getInventoryCount(self):
            return self.totalInventory - len(self.carts)


# DetailHandler为每个页面请求产生一个唯一标识符，
# 在每次请求时提供库存数量，并向浏览器渲染index.html模板
class DetailHandler(tornado.web.RequestHandler):
        def get(self):
            session = uuid4()
            count = self.application.shoppingCart.getInventoryCount()
            self.render("index.html", session=session, count=count)


# CartHandler为浏览器提供了一个API来请求从访客的购物车中添加或删除物品。
# 浏览器中运行的JavaScript提交POST请求来操作访客的购物车。
class CartHandler(tornado.web.RequestHandler):
        def post(self):
            action = self.get_argument('action')
            session = self.get_argument('session')

            if not session:
                self.set_status(400)
                return

            if action == 'add':
                self.application.shoppingCart.moveItemToCart(session)
            elif action == 'remove':
                self.application.shoppingCart.removeItemFromCart(session)
            else:
                self.set_status(400)


# StatusHandler用于查询全局库存变化的通知
class StatusHandler(tornado.web.RequestHandler):
        # 在get方法返回时不会关闭连接
        @tornado.web.asynchronous
        def get(self):
            self.application.shoppingCart.register(callback=self.on_message)

        # 回调函数，将当前库存数量写入客户端并关闭连接
        def on_message(self, count):
            self.write('{"inventoryCount":"%d"}' % count)
            self.finish()


class Application(tornado.web.Application):
        def __init__(self):
            self.shoppingCart = ShoppingCart()

            # 定义url
            handlers = [
                (r'/', DetailHandler),
                (r'/cart', CartHandler),
                (r'/cart/status', StatusHandler)
            ]

            # 定义模板和静态文件路径
            settings = {
                'template_path': 'templates',
                'static_path': 'static'
            }

            tornado.web.Application.__init__(self, handlers, **settings)

if __name__ == '__main__':
        tornado.options.parse_command_line()
        app = Application()
        server = tornado.httpserver.HTTPServer(app)
        server.listen(8000)
        tornado.ioloop.IOLoop.instance().start()

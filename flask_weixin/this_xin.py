# -*- coding:utf-8 -*-
from flask import Flask, request, make_response, render_template
from xml.etree import cElementTree as ET
import hashlib
import time


app = Flask(__name__)

tips = "查理歌词 v1.0\n请输入'歌曲名@歌手名'进行查找(中间是@的说.)"
error_msg = "查理没用...查不到...\nbtw,您听歌的品味真独特.\n您确认格式正确?(歌名@歌手名)\n好啦还是人家太弱了啦...TAT"


@app.route('/')
def hello_world():
    return 'Hello World!'


# 点击“我的冰箱”响应
@app.route('/fridge', methods=['GET', 'POST'])
def fridge_click():
    # 具体实现，自由发挥
    pass


# # 点击“定制早餐”响应
# @app.route('/breakfast', methods=['GET', 'POST'])
# def breakfast_click():
#     # 具体实现，自由发挥
#     pass
#
#
# # 点击“定制午餐”响应
# @app.route('/dinner',methods=['GET', 'POST'])
# def dinner_click():
#     # 具体实现，自由发挥
#     pass
#
#
# # 点击“定制晚餐”响应
# @app.route('/fridge',methods=['GET', 'POST'])
# def wechat_auth():
#     # 具体实现，自由发挥
#     pass
#
#
# # 点击“结伴购物”响应
# @app.route('/shoptogether',methods=['GET', 'POST'])
# def shoptogether_click():
#     # 具体实现，自由发挥
#     pass
#
#
# # 对于用户发来的消息，自动回复auto response
# @app.route('/wechat_auth', methods=['GET', 'POST'])
# def wechat_auth():
#     # 微信认证token
#     if request.method == 'GET':
#         token = 'liusicong'
#         data = request.args
#         signature = data.get('signature', '')
#         timestamp = data.get('timestamp', '')
#         nonce = data.get('nonce', '')
#         echostr = data.get('echostr', '')
#         s = [timestamp, nonce, token]
#         s.sort()
#         s = ''.join(s)
#         if (hashlib.sha1(s).hexdigest() == signature):
#             return make_response(echostr)
#     # 与用户的对话
#     else:
#         rec = request.stream.read()
#         xml_rec = ET.fromstring(rec)
#         msgtype = xml_rec.find('MsgType').text
#         tou = xml_rec.find('ToUserName').text
#         fromu = xml_rec.find('FromUserName').text
#         xml_rep_img = "<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName>" \
#                       "<![CDATA[%s]]></FromUserName><CreateTime>%s</CreateTime><MsgType>" \
#                       "<![CDATA[news]]></MsgType><ArticleCount>1</ArticleCount><Articles>" \
#                       "<item><Title><![CDATA[%s]]></Title><Description><![CDATA[%s]]>" \
#                       "</Description><PicUrl><![CDATA[%s]]></PicUrl></item></Articles><FuncFlag>1</FuncFlag></xml>"
#
#         # 如效果.png中所示的图文消息
#         xml_rep_mutiimg = "<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName>" \
#                           "<![CDATA[%s]]></FromUserName><CreateTime>%s</CreateTime><MsgType>" \
#                           "<![CDATA[news]]></MsgType><ArticleCount>6</ArticleCount><Articles><item>" \
#                           "<Title><![CDATA[%s]]></Title><PicUrl><![CDATA[%s]]></PicUrl></item><item><Title>" \
#                           "<![CDATA[我的冰箱]]></Title><Url><![CDATA[%s]]></Url></item><item><Title><![CDATA[定制早餐]]>" \
#                           "</Title><Url><![CDATA[%s]]></Url></item><item><Title><![CDATA[定制午餐]]>" \
#                           "</Title><Url><![CDATA[%s]]></Url></item><item><Title><![CDATA[定制晚餐]]></Title><Url>" \
#                           "<![CDATA[%s]]></Url></item><item><Title><![CDATA[结伴购物]]></Title><Url><![CDATA[%s]]>" \
#                           "</Url></item></Articles></xml>"
#
#         # 用户一旦关注改公众账号，自动回复以下图文消息
#         if msgtype == "event":
#             msgcontent = xml_rec.find('Event').text
#             if msgcontent == "subscribe":
#                 msgcontent = tips
#             else:
#                 msgcontent = error_msg
#             msg_title = u"美食助手，您的私人定制"
#             msg_imag_url = "http://gourmetmaster.sinaapp.com/static/main_meitu_3.jpg"
#             response = make_response(xml_rep_img % (fromu, tou, str(int(time.time())),
#                                                     msg_title, msgcontent, msg_imag_url))
#             response.content_type = 'application/xml'
#             return response
#         # 用户任意发消息，自动回复
#         else:
#             content = xml_rec.find('Content').text
#             home_title = "主人好，我是一只满血满蓝的营养师 && 厨师，今天起我将是您的私人美食助手~"
#             my_imag_url = "http://gourmetmaster.sinaapp.com/static/main_meitu_3.jpg"
#             # 以下5个url,在该文件中分别有实现其具体响应的部分，见本文件开头的五个@app.route
#             fridgeurl = "http://gourmetmaster.sinaapp.com/fridge"
#             breakfasturl = "http://gourmetmaster.sinaapp.com/breakfast"
#             dinnerurl = "http://gourmetmaster.sinaapp.com/dinner"
#             supperurl = "http://gourmetmaster.sinaapp.com/supper"
#             shoptogether = "http://gourmetmaster.sinaapp.com/shoptogether"
#             # 点击每项，转到相应的url
#             response = make_response(xml_rep_mutiimg % (fromu, tou, str(int(time.time())), fromu, my_imag_url, fridgeurl,
#                                                         breakfasturl, dinnerurl, supperurl, shoptogether))
#             response.content_type = 'application/xml'
#             return response
#     return render_template("helper_parent.html", messages='xxxx', comments='xxxxx')


if __name__ == '__main__':
    app.run()

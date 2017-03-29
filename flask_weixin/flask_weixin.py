# -*- coding:utf-8 -*-
from flask import Flask, request, make_response, render_template
from xml.etree import cElementTree as ET
from shark import SharkSearcher
import hashlib
import time


app = Flask(__name__)

tips = "查理歌词 v1.0\n请输入'歌曲名@歌手名'进行查找(中间是@的说.)"
error_msg = "查理没用...查不到...\nbtw,您听歌的品味真独特.\n您确认格式正确?(歌名@歌手名)\n好啦还是人家太弱了啦...TAT"


# @app.route('/')
# def hello_world():
#     user = 'tom'
#     return render_template('index.html', tips=tips)

@app.route('/py-code', methods=['GET', 'POST'])
def py_code():
    xml_recv = ET.fromstring(request.data)
    ToUserName = xml_recv.find("ToUserName").text
    FromUserName = xml_recv.find("FromUserName").text
    # Content = xml_recv.find("Content").text
    msgtype = xml_recv.find('MsgType').text
    reply = "<xml>" \
            "<ToUserName><![CDATA[%s]]></ToUserName>" \
            "<FromUserName><![CDATA[%s]]></FromUserName>" \
            "<CreateTime>%s</CreateTime>" \
            "<MsgType><![CDATA[news]]></MsgType>" \
            "<ArticleCount>1</ArticleCount>" \
            "<Articles>" \
            "<item>" \
            "<Title><![CDATA[%s]]></Title>" \
            "<Description><![CDATA[%s]]></Description>" \
            "<Title><![CDATA[密码]]></Title>" \
            "<Description><![CDATA[%s]]></Description>" \
            "</item>" \
            "</Articles>" \
            "<FuncFlag>1</FuncFlag>" \
            "</xml>"
    msg_title = 'Python基础资料'
    msgcontent = tips
    msgcontent_url = 'http://pan.baidu.com/s/1nuJZfct'
    password = 'jv59'
    # descp = '0.0.0.0'
    response = make_response(reply % (FromUserName, ToUserName, int(time.time()), msg_title, msgcontent_url, password))
    response.content_type = 'application/xml'
    return response


@app.route('/', methods=['GET', 'POST'])
def wechat_auth():
    if request.method == 'GET':
        token = 'xtxin'
        query = request.args
        signature = query.get('signature', '')
        timestamp = query.get('timestamp', '')
        nonce = query.get('nonce', '')
        echostr = query.get('echostr', '')
        s = [timestamp, nonce, token]
        s.sort()
        s = ''.join(s)
        if hashlib.sha1(s).hexdigest() == signature:
            return make_response(echostr)
    # Get the infomations from the recv_xml.
    # else 这判断如下
    else:
        xml_recv = ET.fromstring(request.data)  # xml
        ToUserName = xml_recv.find("ToUserName").text
        FromUserName = xml_recv.find("FromUserName").text
        # Content = xml_recv.find("Content").text
        msgtype = xml_recv.find('MsgType').text
        # 订阅XML
        reply = "<xml>" \
                "<ToUserName><![CDATA[%s]]></ToUserName>" \
                "<FromUserName><![CDATA[%s]]></FromUserName>" \
                "<CreateTime>%s</CreateTime>" \
                "<MsgType><![CDATA[news]]></MsgType>" \
                "<ArticleCount>1</ArticleCount>" \
                "<Articles>" \
                "<item>" \
                "<Title><![CDATA[%s]]></Title>" \
                "<Description><![CDATA[%s]]></Description>" \
                "</item>" \
                "</Articles>" \
                "<FuncFlag>1</FuncFlag>" \
                "</xml>"
        # 使用xml
        xml_rep_mutiimg = "<xml>" \
                          "<ToUserName><![CDATA[%s]]></ToUserName>" \
                          "<FromUserName><![CDATA[%s]]></FromUserName>" \
                          "<CreateTime>%s</CreateTime>" \
                          "<MsgType><![CDATA[news]]></MsgType>" \
                          "<ArticleCount>6</ArticleCount>" \
                          "<Articles>" \
                          "<item>" \
                          "<Title><![CDATA[%s]]></Title>" \
                          "</item>" \
                          "<item>" \
                          "<Title><![CDATA[1.语言基础]]></Title>" \
                          "<Url><![CDATA[%s]]></Url>" \
                          "</item>" \
                          "<item>" \
                          "<Title><![CDATA[2.面向对象]]></Title>" \
                          "<Url><![CDATA[%s]]></Url>" \
                          "</item>" \
                          "<item>" \
                          "<Title><![CDATA[3.Django基础]]></Title>" \
                          "<Url><![CDATA[%s]]></Url></item>" \
                          "<item>" \
                          "<Title><![CDATA[4.Flask基础]]></Title>" \
                          "<Url><![CDATA[%s]]></Url>" \
                          "</item>" \
                          "<item>" \
                          "<Title><![CDATA[5.爬虫基础]]></Title>" \
                          "<Url><![CDATA[%s]]></Url>" \
                          "</item>" \
                          "</Articles>" \
                          "</xml>"

        if msgtype == 'event':  # 订阅
            msgcontent = xml_recv.find('Event').text
            if msgcontent == "subscribe":
                msgcontent = tips
            else:
                msgcontent = error_msg
            msg_title = 'Python相关资料'
            # descp = '0.0.0.0'
            response = make_response(reply % (FromUserName, ToUserName, int(time.time()), msg_title, msgcontent))
            response.content_type = 'application/xml'
            return response
        else:
            xml_rep = "<xml>" \
                      "<ToUserName><![CDATA[%s]]></ToUserName>" \
                      "<FromUserName><![CDATA[%s]]></FromUserName>" \
                      "<CreateTime>%s</CreateTime>" \
                      "<MsgType><![CDATA[text]]></MsgType>" \
                      "<Content><![CDATA[%s\n%s\n%s]]></Content>" \
                      "<FuncFlag>0</FuncFlag></xml>"
            content = xml_recv.find('Content').text
            if content == u'爬虫基础':
                msg_title = '爬虫基础相关资料:'
                msgcontent_url = '资料链接:http://pan.baidu.com/s/1nuJZfct'
                password = '密码:jv59'
                response = make_response(xml_rep % (FromUserName, ToUserName, int(time.time()), msg_title,
                                                    msgcontent_url, password))
                response.content_type = 'application/xml'
            elif content == '音乐':
                pass
            elif content == u'语言基础':
                msg_title = 'Python基础相关资料:'
                msgcontent_url = '资料链接:http://pan.baidu.com/s/1nuJZfct'
                password = '密码:jv59'
                response = make_response(xml_rep % (FromUserName, ToUserName, int(time.time()), msg_title,
                                                    msgcontent_url, password))
                response.content_type = 'application/xml'
            elif content == u'Django基础':
                msg_title = 'Django基础相关资料:'
                msgcontent_url = '资料链接:http://pan.baidu.com/s/1nuJZfct'
                password = '密码:jv59'
                response = make_response(xml_rep % (FromUserName, ToUserName, int(time.time()), msg_title,
                                                    msgcontent_url, password))
                response.content_type = 'application/xml'
            elif content == u'Flask基础':
                msg_title = 'Flask基础相关资料:'
                msgcontent_url = '资料链接:http://pan.baidu.com/s/1nuJZfct'
                password = '密码:jv59'
                response = make_response(xml_rep % (FromUserName, ToUserName, int(time.time()), msg_title,
                                                    msgcontent_url, password))
                response.content_type = 'application/xml'
            elif content == u'面向对象':
                msg_title = '面向对象相关资料:'
                msgcontent_url = '资料链接:http://pan.baidu.com/s/1nuJZfct'
                password = '密码:jv59'
                response = make_response(xml_rep % (FromUserName, ToUserName, int(time.time()), msg_title,
                                                    msgcontent_url, password))
                response.content_type = 'application/xml'
            else:
                home_title = '你好,欢迎来到python相关资料查询,可回复以下文字得来相应资料:'
                # 以下5个url,在该文件中分别有实现其具体响应的部分，见本文件开头的五个@app.route
                jichu_url = 'http://120.24.158.133/py-code'
                duix_url = 'http://120.24.158.133'
                django_url = 'http://120.24.158.133'
                flask_url = 'http://120.24.158.133'
                pac_url = 'http://120.24.158.133'
                response = make_response(xml_rep_mutiimg % (FromUserName, ToUserName, int(time.time()), home_title, jichu_url,
                                                        duix_url, django_url, flask_url, pac_url))
                response.content_type = 'application/xml'
            return response


while True:
    break
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

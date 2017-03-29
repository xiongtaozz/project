# -*- coding:utf-8 -*-

from flask import Flask, request, make_response
import hashlib
from xml.etree import cElementTree as ET
import time
import spider
app = Flask(__name__)


# @app.route('/')
# def index():
#     return 'hello word'
'''
    1）将token、timestamp、nonce三个参数进行字典序排序
    2）将三个参数字符串拼接成一个字符串进行sha1加密
    3）开发者获得加密后的字符串可与signature对比，标识该请求来源于微信
'''


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
        '''
        用户未关注:
        <xml>
        <ToUserName><![CDATA[toUser]]></ToUserName>
        <FromUserName><![CDATA[FromUser]]></FromUserName>
        <CreateTime>123456789</CreateTime>
        <MsgType><![CDATA[event]]></MsgType>
        <Event><![CDATA[subscribe]]></Event>
        <EventKey><![CDATA[qrscene_123123]]></EventKey>
        <Ticket><![CDATA[TICKET]]></Ticket>
        </xml>
        用户关注成功后返回xml:
        '''
    else:
        xml_recv = ET.fromstring(request.data)
        toUserName = xml_recv.find('ToUserName').text
        fromUserName = xml_recv.find('FromUserName').text
        # createTime = xml_recv.find('CreateTime').text
        msgType = xml_recv.find('MsgType').text
        if msgType == 'event':
            event = xml_recv.find('Event').text
            if event == 'subscribe':
                msgcontent = '恭喜你,关注成功'
            else:
                msgcontent = '关注失败'
            rexpy = """
                    <xml>
                    <ToUserName><![CDATA[%s]]></ToUserName>
                    <FromUserName><![CDATA[%s]]></FromUserName>
                    <CreateTime>%s</CreateTime>
                    <MsgType><![CDATA[text]]></MsgType>
                    <Content><![CDATA[%s]]></Content>
                    </xml>
                    """
            response = make_response(rexpy % (fromUserName, toUserName, int(time.time()), msgcontent))
            response.content_type = 'application/xml'
            return response
        '''
         <xml>
         <ToUserName><![CDATA[toUser]]></ToUserName>
         <FromUserName><![CDATA[fromUser]]></FromUserName>
         <CreateTime>1348831860</CreateTime>
         <MsgType><![CDATA[text]]></MsgType>
         <Content><![CDATA[this is a test]]></Content>
         <MsgId>1234567890123456</MsgId>
         </xml>
        '''
        # 基本对话操作
        repx_error = """
                    <xml>
                    <ToUserName><![CDATA[%s]]></ToUserName>
                    <FromUserName><![CDATA[%s]]></FromUserName>
                    <CreateTime>%s</CreateTime>
                    <MsgType><![CDATA[text]]></MsgType>
                    <Content><![CDATA[%s]]></Content>
                    </xml>
                    """
        if msgType == 'text':
            content = xml_recv.find('Content').text
            if content == 'python':
                rexp = """
                        <xml>
                        <ToUserName><![CDATA[%s]]></ToUserName>
                        <FromUserName><![CDATA[%s]]></FromUserName>
                        <CreateTime>%s</CreateTime>
                        <MsgType><![CDATA[text]]></MsgType>
                        <Content><![CDATA[百度云盘地址:%s\n提取密码:%s]]></Content>
                        </xml>
                        """
                response = make_response(rexp % (fromUserName, toUserName, int(time.time()),
                                                 'http://pan.baidu.com/s/1nuJZfct', 'jv59'))
                response.content_type = 'application/xml'
                return response
            elif content == u'笑话':
                try:
                    msgcontent = spider.Spider().run()
                    print msgcontent
                    response = make_response(repx_error % (fromUserName, toUserName, int(time.time()), msgcontent))
                    response.content_type = 'application/xml'
                    return response
                except Exception as e:
                    print e
            else:
                response = make_response(repx_error % (fromUserName, toUserName, int(time.time()),
                                                       '模块缺失,正在完善,敬请了解...'))
                response.content_type = 'application/xml'
                return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)





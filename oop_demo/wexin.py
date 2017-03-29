# -*- coding:utf-8 -*-

from wechat_sdk import WechatConf,WechatBasic

conf = WechatConf(
    token='weixin',
    appid='wxe58a6f5897a3ebf7',
    appsecret='739a0c03fa0ef07317f920ace7f80017',
    encrypt_mode='safe',  # 可选项：normal/compatible/safe，分别对应于 明文/兼容/安全 模式
    encoding_aes_key='hjvvPzCymBwKThrMEkMGXZ1AUd4JWwAoxK2XuixrP7T'  # 如果传入此值则必须保证同时传入 token, appid
)


wechat = WechatBasic(conf=conf)

if wechat.check_signature(signature='今天'):
    print 'Accept'
else:
    print 'Wring'


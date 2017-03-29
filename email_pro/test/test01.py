# -*- coding:utf-8 -*-

# import smtplib
# from email.mime.text import MIMEText
#
# msg = MIMEText('hello, send by Python..', 'plain', 'utf-8')
# # 输入Email地址和口令
# from_addr = '380784649@qq.com'    # raw_input('From:')
# password = 'scx1123'             # raw_input('Password:')
# smtp_server = 'smtp.qq.com'      # raw_input('SMTP server:')
# # 输入收件人地址
# to_address = '419592175@qq.com'   # raw_input('To:')
#
# server = smtplib.SMTP(smtp_server, 25)  # SMTP协议默认端口是25
# server.set_debuglevel(1)
# server.login(from_addr, password)
# server.sendmail(from_addr, [to_address], msg.as_string())
# server.quit()

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr.encode('utf-8') if isinstance(addr, unicode) else addr))

# 输入Email地址和口令
from_addr = 'xiongtaozz@163.com'    # raw_input('From:')
password = 'scx1123'             # raw_input('Password:')
smtp_server = 'smtp.163.com'      # raw_input('SMTP server:')
# 输入收件人地址
to_addr = '419592175@qq.com'   # raw_input('To:')

msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
msg['From'] = _format_addr(u'Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr(u'管理员 <%s>' % to_addr)
msg['Subject'] = Header(u'来自SMTP的问候……', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
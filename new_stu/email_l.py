# -*- coding:utf-8 -*-

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib


class em_cls(object):
    def __init__(self):
        # 输入Email地址和口令
        self.from_addr = 'xiongtaozz@163.com'    # raw_input('From:')
        self.password = 'scx1123'             # raw_input('Password:')
        self.smtp_server = 'smtp.163.com'      # raw_input('SMTP server:')
        # 输入收件人地址
        self.to_addr = '419592175@qq.com'   # raw_input('To:')

    def _format_addr(self, s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr.encode('utf-8') if isinstance(addr, unicode) else addr))

    def run(self, count):
        msg = MIMEText('你有%d条信息未查看,希望及时修改,小心事故...,'% count, 'plain', 'utf-8')
        msg['From'] = self._format_addr(u'发送人 <%s>' % self.from_addr)
        msg['To'] = self._format_addr(u'管理员 <%s>' % self.to_addr)
        msg['Subject'] = Header(u'事故事件已经触发,警告..警告...', 'utf-8').encode()

        server = smtplib.SMTP(self.smtp_server, 25)
        server.set_debuglevel(1)
        server.login(self.from_addr, self.password)
        server.sendmail(self.from_addr, [self.to_addr], msg.as_string())
        server.quit()

# if __name__ == "__main__":
#     em_cls().run(1)
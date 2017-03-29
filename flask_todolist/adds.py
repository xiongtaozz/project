# coding:utf-8

from models import Work
from config import db
from datetime import datetime


body_2 = Work(u'今天晚上和妹子吃饭', '2016-08-14 16:25:30')
body_3 = Work(detail='你好', time=datetime.utcnow())

db.session.add(body_3)

db.session.commit()


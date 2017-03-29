# coding:utf-8
from app import db
import datetime


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(80), unique=True)
    content = db.Column(db.String(100))
    pub_date = db.Column(db.DateTime, default=datetime.datetime.now())

    def __str__(self):
        return '%s' % self.title

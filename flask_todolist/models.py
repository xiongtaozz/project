# coding:utf-8

from config import db
from datetime import datetime
# from markdown import markdown


class Work(db.Model):
    __tablename__ = 'works'
    id = db.Column(db.Integer, primary_key=True)
    detail = db.Column(db.Text)
    time = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    #
    # @staticmethod
    # def on_body_changed(target, value, oldvalue, initiator):
    #     if value is None or (value is ''):
    #         target.body_html = ''
    #     else:
    #         target.body_html = markdown(value)

    def __init__(self, detail, time):
        self.detail = detail
        self.time = time

    def __repr__(self):
        return '<Work {}>'.format(self.detail)


if __name__ == '__main__':
    db.create_all()

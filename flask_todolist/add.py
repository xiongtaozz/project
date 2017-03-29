# coding:utf-8


from config import db
from form import PostForm

body = PostForm(detail='HELLO WORLD')
time = PostForm(time='2016-08-11 16:14:35')
db.session.add_all(body, time)

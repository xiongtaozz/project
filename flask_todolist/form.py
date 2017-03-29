# coding:utf-8

from flask_wtf import Form
from wtforms import BooleanField, SubmitField, DateTimeField,TextAreaField
# from flask_pagedown.fields import PageDownField
from wtforms.validators import DataRequired


class PostForm(Form):
    body = TextAreaField(u"还有什么事情需要做？", validators=[DataRequired()])
    submit = SubmitField(u'Add')

# coding:utf-8
from flask_wtf.form import Form
import wtforms


# 表单验证
class AddPostForm(Form):
    title = wtforms.StringField('title', [wtforms.validators.length
                                          (min=1, max=200)])
    content = wtforms.StringField('content', [wtforms.validators.length
                                          (min=1, max=200)])
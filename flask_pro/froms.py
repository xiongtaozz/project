# -*- coding:utf-8 -*-
from wtforms import StringField, TextAreaField, IntegerField, FloatField, SubmitField, validators
from flask_wtf.form import Form


class ProFrom(Form):
    name = StringField('产品名称', validators=[validators.DataRequired()])
    type = StringField('类型', validators=[validators.AnyOf('大', '中', '小')])
    style = StringField('型号')
    qty = IntegerField('数量')
    price = FloatField('价格')
    remark = TextAreaField('备注')
    submit = SubmitField('提交')
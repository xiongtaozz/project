# coding:utf-8
from app import app


# 自定义过滤器
@app.add_template_filter
def allen(s):
    return s[4]


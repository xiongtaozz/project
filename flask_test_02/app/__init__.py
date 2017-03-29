# coding: utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView  # 注册后台管理


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
admin = Admin(app)

from app import views, models, filter
admin.add_view(ModelView(models.Post, db.session))

from post_api import post_api
app.register_blueprint(post_api, url_prefix='/post')

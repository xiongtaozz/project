print('app called')

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
admin = Admin(app)


from app import views, models
admin.add_view(ModelView(models.Post, db.session))
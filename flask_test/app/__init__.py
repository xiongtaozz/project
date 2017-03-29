from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_wtf import CsrfProtect

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
# admin = Admin(app)
csrf = CsrfProtect(app)


from app import views
# admin.add_view(ModelView(all, db.session))

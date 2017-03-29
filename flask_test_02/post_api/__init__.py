from flask import Blueprint

post_api = Blueprint('post_api', __name__)

from . import views
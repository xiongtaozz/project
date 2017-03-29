import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + BASE_DIR + '/test.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = 'super key'
SESSION_TYPE = 'filesystem'


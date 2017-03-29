__author__ = 'xt'

from django.forms import *

class login_froms(Form):
    username=CharField(label='Username')
    password=CharField(label='Password',widget=PasswordInput())

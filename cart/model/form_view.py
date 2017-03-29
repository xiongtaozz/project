# -*- coding:GBK -*-
__author__ = 'xt'

from django import forms

class Login(forms.Form):
    username=forms.CharField(label='User')
    password=forms.CharField(label='Pwd',widget=forms.PasswordInput())

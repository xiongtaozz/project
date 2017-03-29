# -*- coding:utf-8 -*-

from django import forms


class login_form(forms.Form):
    username = forms.CharField(label=u'用户名称')
    password = forms.CharField(label=u'用户密码', widget=forms.PasswordInput)

    class Meta:
        pass
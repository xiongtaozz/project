# -*- coding:utf-8 -*-
from django import forms
from from_app.models import *


class loginFrom(forms.Form):

    username = forms.CharField(label='用户名称', widget=forms.TextInput(attrs={'placeholder': '请输入用户名'}))
    password = forms.CharField(label='用户密码',)

    '''
    给form类自定义验证规则，如果想要重用验证机制，可以单独创建新的字段类，重新写它的验证方法。
    一般的可以直接在form类加入clean_字段名的方法，Django会自动查找以clean_开头的函数名，并会在
    验证该字段的时候，运行这个函数。
    '''

    def clean_password(self):
        password = self.cleaned_data['password']
        num_words = len(password)
        if num_words > 8:
            raise forms.ValidationError('长度少于8')
        return password


class proFromModel(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['title', 'description', 'photo', 'price']
#coding:utf-8
from django import forms
from django_app.models import *
from django.conf import settings

#引用富文本编辑器
class Kindeditoe(forms.Textarea):
    class Media:
        js = (settings)

class LoginFrom(forms.Form):
    username = forms.CharField(label='用户名称')
    password = forms.CharField(label='用户密码', widget=forms.PasswordInput())
    class Meta:
        pass

class ProductForm(forms.ModelForm):

    # title = forms.CharField(max_length=30)
    # description = forms.Textarea()
    # photo = forms.ImageField()
    # price = forms.FloatField()

    class Meta:
        model = Product
        fields =['title','description','photo','price']

class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ['title','price','authors']

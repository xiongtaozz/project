
__author__ = 'wangbiao'

from django import forms

class Login(forms.Form):
    subject=forms.CharField()
    email=forms.EmailField(required=False)
    manage=forms.CharField()



# -*- coding:utf-8 -*-
from django import forms
from form_app.models import *


# 创建From模型
class ProductFrom(forms.Form):
    title = forms.CharField(label='标题')
    description = forms.CharField(label='描述', widget=forms.Textarea())
    email = forms.EmailField(label='邮箱', required=False)
    price = forms.FloatField(label='价格')

    '''
    给form类自定义验证规则，如果想要重用验证机制，可以单独创建新的字段类，重新写它的验证方法。
    一般的可以直接在form类加入clean_字段名的方法，Django会自动查找以clean_开头的函数名，并会在
    验证该字段的时候，运行这个函数。
    '''
    def clean_description(self):
        description = self.cleaned_data['description']
        num_words = len(description)
        if num_words < 4:
            raise forms.ValidationError('长度在4以上')
        # 在自定义的验证函数中，我们必须显示的返回字段名的内容，否则会带来表单数据丢失。
        return description


# FromModel 创建
class ProModel(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['title', 'description', 'photo', 'price']


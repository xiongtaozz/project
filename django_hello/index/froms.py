# coding:utf-8
from django import forms
from index.models import Product, Tag


class ProFr(forms.Form):
    CHENGDU = 'CD'
    SHANGHAO = 'SH'
    BEIJIN = 'BJ'
    SHENZHEN = 'SZ'

    CITY = (
        (CHENGDU, '成都'),
        (SHANGHAO, '上海'),
        (BEIJIN, '北京'),
        (SHENZHEN, '深圳'),
    )

    PROMODEL = (
        ('MIN', '小号'),
        ('MED', '中号'),
        ('MAX', '大号'),
    )
    PROSTYLE = (
        ('DQ', '电器'),
        ('SP', '食品'),
        ('KL', '   '),
    )
    pro_name = forms.CharField(label='产品名称', widget=forms.TextInput(attrs={'placeholder': '请输入用户名'}))
    city = forms.ChoiceField(label='城市', choices=CITY)
    password = forms.CharField(label='密码', widget=forms.TextInput(attrs={'placeholder': '请输入用户名'}))
    pro_model = forms.ChoiceField(label='型号', choices=PROMODEL)
    pro_style = forms.ChoiceField(label='类别', choices=PROSTYLE)
    pro_qty = forms.IntegerField(label='数量')
    pro_price = forms.FloatField(label='价格')
    pro_remark = forms.CharField(label='描述', widget=forms.Textarea())
    tags = forms.ModelChoiceField(label='关键字', queryset=Tag.objects.all(), required=False)


class ProFrom(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['pro_name', 'pro_model', 'pro_style', 'pro_qty', 'pro_price', 'tags', 'pro_remark']




from django.forms import ModelForm, Select, Form
from .models import *


class ProductForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['key'].queryset = Keyword.objects.all()
            self.fields['cate'].queryset = Category.objects.all()
            self.fields['spec'].queryset = Size.objects.all()

    class Meta:
        model = Product
        exclude = []
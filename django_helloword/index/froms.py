from django import forms
from index.models import Product


class proFromModel(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['pro_name', 'pro_model', 'pro_style', 'qty', 'price', 'tags', 'remake']
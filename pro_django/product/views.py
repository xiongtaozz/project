# coding: utf-8
from django.shortcuts import render, redirect
from product.models import Category, Keyword, Product,Size
from .forms import ProductForm
from django.http import HttpResponseForbidden
from django.http import HttpRequest


# Create your views here.
# 添加产品
# request/response
def add(request):
    if request.method == 'POST':
        post = request.POST
        # 创建对象并保存到数据库
        size_id = post.get('product_spec')
        try:
            size = Size.objects.get(pk=size_id)
        except Size.DoesNotExist:
            return HttpResponseForbidden

        product = Product.objects.create(name=post.get('product_name'),
                               spec=size,
                               cate_id=post.get('product_cate'),
                               stock=post.get('product_stock'),
                               price=post.get('product_price'),
                               desc=post.get('product_desc'))
        # 多对多的保存必须单独处理
        for key_id in post.getlist('product_key'):
            product.key.add(key_id)
        return redirect('list')
    categorys = Category.objects.all()
    keywords = Keyword.objects.all()
    sizes = Size.objects.all()
    return render(request, 'add.html', locals())


def add_form(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
        else:
            return HttpResponseForbidden
    return render(request, 'add_form.html', {'form':ProductForm()})


# 修改产品
def update(request, id):
    if request.method == 'POST':
        post = request.POST
        # 先得到要修改的对象
        product = Product.objects.get(pk=id)
        product.name=post.get('product_name')
        size_id = (post.get('product_spec'))
        size = Size.objects.get(pk=size_id)
        product.spec=size
        product.cate_id=post.get('product_cate')
        product.stock=post.get('product_stock')
        product.price=post.get('product_price')
        product.desc=post.get('product_desc')
        product.save()
        # 多对多的保存必须单独处理
        for key_id in post.getlist('product_key'):
            key = Keyword.objects.get(pk=key_id)
            if key not in product.key.all():
                product.key.add(key)
        for key in product.key.all():
            if str(key.id) not in post.getlist('product_key'):
                product.key.remove(key)
        return redirect('list')
    product = Product.objects.get(pk=id)
    categorys = Category.objects.all()
    keywords = Keyword.objects.all()
    sizes = Size.objects.all()
    return render(request, 'update.html', locals())

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
register = template.Library()
@register.filter()
def cut_filter(value, arg):
    return value.replace(arg, '')


# 删除产品
def delete(request, id):
    # 先得到要删除的对象
    try:
        product = Product.objects.get(pk=id)
    except Product.DoesNotExist:
        return HttpResponseForbidden
    product.delete()
    return redirect('list')


# 产品列表
def list(request):
    print(request, '1')
    products = Product.objects.all()
    return render(request, 'list.html', locals())
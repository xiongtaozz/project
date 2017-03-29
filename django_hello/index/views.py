# -*- coding:utf-8 -*-
from django.shortcuts import render,render_to_response, HttpResponse
from django.core.paginator import Paginator,EmptyPage,InvalidPage,PageNotAnInteger
from index.models import Product,Tag
from index.froms import ProFrom,ProFr

# Create your views here.


def index(req):
    products = Product.objects.all()
    pros = get_page(req, products, 10)
    return render(req, 'list.html', locals())


# def add(req):
#     profrom = ProFrom()
#     if req.method == 'POST':
#         profrom = ProFrom(req.POST or None, req.FILES)
#         if profrom.is_valid:
#             profrom.save()
#             return HttpResponse('添加成功')
#     else:
#         return render_to_response('add.html', locals())

def add(req):
    profrom = ProFr()
    if req.method == 'POST':
        profrom = ProFrom(req.POST or None, req.FILES)
        if profrom.is_valid:

            return HttpResponse('添加成功')
    else:
        return render_to_response('add.html', locals())


# 分页调用接口
def get_page(req, page_list, count_in_page):

    pator = Paginator(page_list, count_in_page)
    try:
        page = int(req.GET.get('page', 1))
        page_list = pator.page(page)
    except (EmptyPage, InvalidPage, PageNotAnInteger):
        page_list = pator.page(1)
    return page_list

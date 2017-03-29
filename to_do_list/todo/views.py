# - * - coding:utf8 - * -
from django.shortcuts import render,redirect
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger
from todo.models import Item
# Create your views here.
#添加待办事项的分页列表
def index(request):
    #捕获异常
    try:
        item_list1 = Item.objects.all().order_by('-pubdate')
        paginator = Paginator(item_list1,2)
        try:
            page = int(request.GET.get('page',1))
            item_list = paginator.page(page)
        except(EmptyPage,InvalidPage,PageNotAnInteger):
            item_list = paginator.page(1)
    except Exception as e:
        print e
    return render(request, 'index.html',locals())

#添加待办事项
def add(request):
    try:
        content = request.GET.get('item',None)
        if len(content) > 0:
            obj = Item.objects.create(content=content)
            if obj:
                return redirect('/index/')
    except Exception as e:
        print e
        return render(request,'404.html',{'404':u'待办事项添加失败'})

#修改待办事项
def edit(request):
    try:
        pass
    except Exception as e:
        print e

#删除待办事项
def delete(request):
    try:
        pass
    except Exception as e:
        print e

#标记待办事项
def done(request):
    try:
        pass
    except Exception as e:
        print e




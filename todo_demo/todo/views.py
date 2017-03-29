# coding: utf-8
from django.shortcuts import render, redirect, resolve_url
from todo.models import Item
from django.core.paginator import Paginator, PageNotAnInteger, InvalidPage, EmptyPage

# Create your views here.
# 待办事项列表,需要对列表进行分页
def index(request):
    try:
        item_list = Item.objects.all().order_by("-pub_date")
        paginator = Paginator(item_list, 2)
        try:
            page = int(request.GET.get("page",1))
            item_list = paginator.page(page)
        except (PageNotAnInteger, InvalidPage, EmptyPage):
            item_list = paginator.page(1)
    except Exception as e:
        print e
    return render(request, "index.html", locals())

# 增加待办事项
def add(request):
    try:
        content = request.GET.get("item", None)
        if len(content) > 0:
            obj = Item.objects.create(content=content)
            if obj:
                return redirect(resolve_url("index"))
    except Exception as e:
        print e
    return render(request, "message.html", {"message": u"待办事项添加失败"})

# 修改待办事项
def edit(request):
    try:
        item_id = request.GET.get("item_id", None)
        content = request.GET.get("item", None)
        if len(item_id) > 0 and len(content) > 0:
            obj = Item.objects.get(pk=item_id)
            obj.content = content
            obj.save()
        return redirect("/index/")
    except Exception as e:
        print e
    return render(request, "message.html", {"message": u"待办事项修改失败"})

# 删除待办事项
def delete(request):
    try:
        item_id = request.GET.get("item_id", None)
        if len(item_id) > 0:
            obj = Item.objects.get(pk=item_id)
            obj.delete()
        return redirect("/index/")
    except Exception as e:
        print e
    return render(request, "message.html", {"message": u"待办事项删除失败"})

# 标记事项完成
def done(request):
    try:
        item_id = request.GET.get("item_id", None)
        if len(item_id) > 0:
            obj = Item.objects.get(pk=item_id)
            obj.is_done = False if obj.is_done else True
            # if obj.is_done:
            #     obj.is_done = False
            # else:
            #     obj.is_done = True
            obj.save()
        return redirect("/index/")
    except Exception as e:
        print e
    return render(request, "message.html", {"message": u"待办事项状态修改失败"})

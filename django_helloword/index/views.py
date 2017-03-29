# coding:utf-8
from django.shortcuts import render,render_to_response,HttpResponse,HttpResponseRedirect
from index.models import Product
from index.froms import proFromModel
# Create your views here.


def index(request):
    pros = Product.objects.all()
    return render(request, 'list.html', locals())

def add(req):
    proFrom = proFromModel()
    if req.method == 'POST':
        proFrom = proFromModel(req.POST or None, req.FILES)
        if proFrom.is_valid:
            proFrom.save()
            return HttpResponseRedirect('/index/')
    else:
        return render_to_response('add.html', locals())
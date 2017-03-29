#coding=utf-8
from django.shortcuts import render,render_to_response
from blog.models import *
# Create your views here.

def index(request):
    ares=Artile.objects.all()
    return render_to_response('index.html',locals())

def detail(request, id):
    article = Artile.objects.get(id=id)
    return render_to_response('blog.html',locals())

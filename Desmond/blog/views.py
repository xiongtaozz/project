# coding:utf-8
from django.shortcuts import render,render_to_response


# Create your views here.
def index(request):
    # title = 'Desmond blog'
    # hello = 'hello desmond'
    return render_to_response('test.html',locals())

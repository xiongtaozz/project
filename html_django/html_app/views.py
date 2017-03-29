from django.shortcuts import render,HttpResponse

# Create your views here.


def add(req):
    id = req.GET.get('id')
    print id
    return HttpResponse(''+id)
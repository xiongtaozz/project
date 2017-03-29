from django.shortcuts import render,render_to_response
import models
# Create your views here.

def index(req):
    books=models.Book.objects.all()
    return render_to_response('index.html',{'books':books})

def index_find(req):

    pass

def index_update(req,id):
    req.POST['']
    pass
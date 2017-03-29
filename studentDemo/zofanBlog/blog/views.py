from django.shortcuts import render
from django.http import HttpResponse
from blog.models import *
from datetime import date

def index(request):
    c = main.objects.all()
    d = date.today()
    return render(request, 'index.html', locals())

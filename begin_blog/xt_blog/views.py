from django.shortcuts import render,render_to_response,HttpResponse

# Create your views here.

def index(req,tem):
    user='XT'
    print tem
    return render_to_response(tem,locals())
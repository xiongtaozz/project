from django.shortcuts import render,render_to_response
from django.db.transaction import *
from cart.models import *
# Create your views here.


# def index(req):
#     return render_to_response('index.html',locals())


def index(req):
    books = Book.objects.all()
    return render_to_response('index1.html',locals())

# def find(req):
#     carts = Cart.objects.get(user__username=='001')


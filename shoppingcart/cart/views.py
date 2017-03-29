from django.shortcuts import render_to_response
from django.http.response import HttpResponseRedirect
from django.http import JsonResponse
from django import forms
from cart.models import *
from cart.cart_froms import *
# Create your views here.

# class UserForm(forms.Form):
#     username=forms.CharField(label='Username')
#     password=forms.CharField(label="Password", widget=forms.PasswordInput())


def loginis(req):
    form=login_froms()
    return render_to_response('login.html',locals())

def login(req):
    if req.method=='POST':
        username=req.POST['username']
        password=req.POST['password']
        print username,password
        if username and password :
            user=User.objects.get(username__exact=username,password__exact=password)
            if user!=None:
                req.session['user']=username
                return HttpResponseRedirect('/cart/index/')#render_to_response('index.html',{'user':username})
                    #HttpResponseRedirect('/index/')
            else:
               return  HttpResponseRedirect('/cart/loginis/')
        else:
            return  HttpResponseRedirect('/cart/loginis/')
    return  HttpResponseRedirect('/cart/loginis/')

def index(req):
    books=Book.objects.all()
    user = req.session['user']
    return render_to_response('index.html',locals())

def addcart(req):
    #cart=req.session['cart']
    bookname=req.POST['bookname']
    if bookname:
        cart=Cart.objects.filter(book_name__exact=bookname)
        print len(cart)
        if cart:
            return JsonResponse(False,safe=False)
        else:
            Cart.objects.create(book_name=bookname,qty=1,price=100)
            return JsonResponse(True,safe=False)
    else:
        return JsonResponse(False,safe=False)

def findcart(req):
    carts =Cart.objects.all()
    return render_to_response('cart.html',{'carts':carts})

def updatecart(req,id):
    qty=req.POST['qty']
    qty=int(qty)
    if id:
        c=Cart.objects.get(id=id)
        c.qty=qty
        c.save()
        return JsonResponse(True,safe=False)
    else:
        return JsonResponse(False,safe=False)

def delcart(req,id):
    if id:
        #Cart.objects.get(id=id).delete()
        return JsonResponse(True,safe=False)
    else:
        return JsonResponse(False,safe=False)

def base_html(req):
    return render_to_response('q_2.html',{})

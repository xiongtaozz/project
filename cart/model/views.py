# coding:utf-8
from django.shortcuts import render_to_response,HttpResponse
from django.http.response import HttpResponseRedirect
from django.http import JsonResponse
from cart.models import *
from model.form_view import *
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger
from django.core.serializers import  serialize
import json
def  index_d1(req):
    return HttpResponse('Hello Word!')

class UserForm(forms.Form):
    username=forms.CharField(label='Username')
    password=forms.CharField(label="Password",widget=forms.PasswordInput())

def loginis(req):
    form = Login()
    return render_to_response('login.html', locals())

def login(req):
    'try except'
    if req.method == 'POST':
        username=req.POST.get('username' , '')
        password=req.POST.get('password' , '')
        print username,password
        if username and password :
            user=User.objects.filter(username__exact=username,password__exact=password)
            if user!=None:
                req.session['user']=username
                return HttpResponseRedirect('/cart/index/')#render_to_response('index.html',{'user':username})
                    #HttpResponseRedirect('/index/')
            else:
               return  HttpResponseRedirect('/cart/loginis/')
        else:
            return  HttpResponseRedirect('/cart/loginis/')
    return HttpResponseRedirect('/cart/loginis/')

def index(req):
    books = Book.objects.all()
    user=req.session['user']
    return render_to_response('index_01.html',locals())

def addcart(req):
    #cart=req.session['cart']
    bookname = req.POST.get('bookname','')
    # qty =req.POST.get('qty','')
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

def find_cart(req):
     # page =int(req.GET['page_id'])
    carts = Cart.objects.all()
    pa = Paginator(carts,2) #limit 0,2
    cart = pa.page(1)
    return render_to_response('cart.html',{'carts':cart})

def update_cart(req,id):
    qty = req.POST.get('qty','')
    qty = int(qty)
    if id:
        c=Cart.objects.get(id=id)
        c.qty=qty
        c.save()
        return JsonResponse(True,safe=False)
    else:
        return JsonResponse(False,safe=False)

def del_cart(req,id):
    if id:
        Cart.objects.get(id=id).delete()
        return JsonResponse(True,safe=False)
    else:
        return JsonResponse(False, safe=False)

def logout(req):
    del req.session['user']
    return HttpResponseRedirect('/cart/login/')
def base_html(req):
    return render_to_response('q_2.html',{})

#json
def get_json(req):
    # c = Cart.objects.all()
    # pa = Paginator(c,2)
    carts = serialize('json',Paginator(Cart.objects.all(),2).page(1))
    return HttpResponse(json.dumps(carts),content_type='application/json')
#coding:utf-8
from django.shortcuts import render,render_to_response,HttpResponseRedirect,HttpResponse
from django_app import forms
from django_app.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def login_view(req):
    # if req.user.is_authenticated():
            # 方法一
            # form = LoginFrom(req.POST or None,req.FILES)
            # if form.is_valid():
            #     username = form.cleaned_data['username']
            #     password = form.cleaned_data['password']
            #方法二
    if req.method=='POST':
            username=req.POST.get('username','')
            password=req.POST.get('password','')
            # if username and password:
            #     user=User.objects.get(username__icontains=username,password__excat=password)
            user = authenticate(username=username,password=password)
            if user is not None:
                # login(re)
                login(req,user)
                return render_to_response('index.html', locals())
    # else:
    #     return HttpResponseRedirect('/login/?next=%s' % req.path)
    else:
        form=forms.LoginFrom()
        return render_to_response('login.html',locals())


def logout_view(req):
    logout(req)
    return HttpResponseRedirect('/login/')


def index(req):#login
    return render_to_response('depot/create_pro.html')

def create_pro(req):
    form=forms.ProductForm()
    if req.method == 'POST':
        form =forms.ProductForm(req.POST or None , req.FILES)
        if form.is_valid():
            form.save()
    return render(req , 'depot/create_pro.html', locals())
def create_view(req):
    req.POST.get('name' , '')


def update(req):#update
    form=forms.ProductForm(instance=Product.objects.get(pk=1))
    # form.save()
    # udate this form
    return render_to_response('depot/find_pro.html',locals())

def createBook(req):# create book
    form = forms.BookForm()
    if req.method == 'POST':
        form = forms.BookForm(req.POST or None, req.FILES)
        if form.is_valid():
            form.save()
    return render(req,'book/create_book.html',locals())

def findAll(req): # find all this
    books = Book.objects.all()
    return render_to_response('book/find_book.html',locals())

def updateBook(req,id): # id find this
    if req.method == 'POST':
        form = forms.BookForm(req.POST,instance=Book.objects.get(id=id))
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/text/find_book/')
    else:
        form = forms.BookForm(instance=Book.objects.get(id=id))
        return render_to_response('book/update_book.html',locals())


def updateBooSuc(req):  # update success
    if req.method == 'POST':
        form = forms.BookForm(req.POST)
        if form.is_valid():
            new_blog=form.save(commit=False)
            new_blog.authors = form.cleaned_data['authors']
            new_blog.save()
            form.save_m2m()
    return render_to_response('depot/success.html',locals())
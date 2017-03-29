from django.shortcuts import render,render_to_response
from index.models import Product
# Create your views here.


def index(request):
    pros = Product.objects.all()
    return render_to_response('list.html', locals())


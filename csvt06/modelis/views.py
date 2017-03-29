from django.shortcuts import  render_to_response
from modelis.models import Author,Book
# Create your views here.


def show_anthor(req):
    authors=Author.objects.all()
    return render_to_response('show_anthor.html',{'authors':authors})

def show_book(req):
    books=Book.objects.all()
    return render_to_response('show_book.html',{'books':books})
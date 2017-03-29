from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def test(request):
    print request.method
    print request.GET.get('username')
    print request.META
    print request.META['REMOTE_ADDR']
    print request.META['HTTP_USER_AGENT']
    # Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0
    return HttpResponse("ok", content_type="text/html")
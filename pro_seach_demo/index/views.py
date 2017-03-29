# coding:utf-8
from django.shortcuts import render,render_to_response,HttpResponse
import xlrd
import os
from index.models import *

# Create your views here.


def index(req):
    fi = FileUrl.objects.all()[:1]
    return render_to_response('index.html', locals())


def excel(req):
    if req.method == 'POST':
        filename = req.FILES.get('filename')
        file_url = save(filename)
        if file_url:
            print file_url.url
            file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'uploads/'+str(file_url.url))
            print file
            # xls解析 这里自己镶嵌 xls解析出来是一个对象.这里可以直接返回前端页面.
            data = xlrd.open_workbook(file, encoding_override='utf-8')
            table = data.sheets()[0]
            nrows = table.nrows()
            print nrows
        else:
            return HttpResponse('error')
    return render_to_response('index.html')


def save(filename):
    xls = 'xls/'+str(filename)
    print xls
    files = FileUrl.objects.filter(url=xls)
    if not files:
        fileurl = FileUrl()
        fileurl.url = filename
        fileurl.save()
        return fileurl
    return files[0]


def bigFileView(req):

    def readFile(fn, buf_size=262144):
        f = open(fn, "rb")
        while True:
            c = f.read(buf_size)
            if c:
                yield c
            else:
                break
        f.close()
    fi = FileUrl.objects.all()[:1]
    # file_name = fi.url
    response = HttpResponse(readFile(fi.url))
    return response
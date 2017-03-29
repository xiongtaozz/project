from django.shortcuts import render,render_to_response
import xlrd
import os
from index.models import *

# Create your views here.


def index(req):
    return render_to_response('index.html', locals())


def excel(req):
    if req.method == 'POST':
        filename = req.FILES.get('filename')
        print filename
        save(filename)
        # print file_url.url
        # data = xlrd.open_workbook(file_url.url)
        # table = data.sheets()[0]
        # nrows = table.nrows()
        # print nrows
    return render_to_response('index.html')


def save(filename):
    xls = 'xls/'+str(filename)
    print xls
    files = FileUrl.objects.filter(url=xls)

    try:
        files = FileUrl.objects.filter(url=xls)
        print files
    except Exception as e:
        pass
    else:
        if not files:
            fileurl = FileUrl()
            fileurl.url = filename
            fileurl.save()
    # return FileUrl.objects.get(url='xls/'+filename)
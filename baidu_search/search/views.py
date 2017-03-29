# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
import json
from search.models import Word
from django.core.serializers import serialize
from django.core.paginator import Paginator

# Create your views here.
def auto_complete(request):
    return render(request,'index.html',locals())

def validate_word(request):
    word = request.GET.get("word",'')
    try:
        if word:
            list = Word.objects.filter(word_value__istartswith=word).order_by('-pk')
            paginator = Paginator(list,4)
            word_list = serialize("json",paginator.page(1))
            status = {"code":"success", "message": word_list}
        else:
            pass
    except Word.DoesNotExist:
        status["code"] = "failure"
    return HttpResponse(json.dumps(status), content_type="application/json")
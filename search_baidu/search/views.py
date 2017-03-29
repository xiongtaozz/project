# -*- coding:utf-8 -*-
from django.shortcuts import render,render_to_response
from django.http import HttpResponse
import json
from search.models import Word
from django.core.serializers import serialize
from django.core.paginator import Paginator

# Create your views here.
def auto_complete(request):
    return render_to_response('index.html')

def validate_word(request):
    word = request.GET.get("word",'')
    try:
        if word:
            list = Word.objects.filter(word_value__icontains=word).order_by('-pk')
            paginator = Paginator(list,4)
            word_list = serialize("json",paginator.page(1))
            # status = {"message": word_list}
        else:
            pass
    except Word.DoesNotExist:
         pass
    return HttpResponse(json.dumps(word_list), content_type="application/json")
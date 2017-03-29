from django.shortcuts import render,render_to_response,HttpResponse,HttpResponseRedirect
from search.models import *
from django.core.serializers import serialize
import json
from django.core.paginator import Paginator


# Create your views here.

def index(req):
    return render_to_response('index.html')

def search(req):
    word = req.GET.get('word','')
    print word
    if word:
        pa =Paginator(Word.objects.filter(word_value__contains=word),3)
        # list= Word.objects.filter(word_value__contains=word)[:4]#exact
        word_list=serialize('json',pa.page(1))
    return HttpResponse(json.dumps(word_list),content_type='application/json')

def questionDetail(req):
    ques=Question.objects.get(id=1)
    return render_to_response('question_detail.html',locals())

def quesComm(req,cid,qid):
    print cid,qid
    Comment.objects.get(id=cid).delete()
    return HttpResponseRedirect('/ques/')

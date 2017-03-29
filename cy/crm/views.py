# -*- coding: utf-8 -*-


from forms import BudgetForm, BudgetdForm
from models import Budget, Budgetd, Subject
from general.models import Company, Year, Month, Depts, Subject
import time, datetime
import json
from django.http.response import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.contrib.auth.models import AbstractUser, User

# Create your views here.
@cache_page(1)
def budget(request, url):
    now = datetime.datetime.now().strftime("%Y-%m-%d")
    budget = BudgetForm(initial={'company': '1', 'crdate': now})
    budgetd = BudgetdForm()
    sub = Subject.objects.all()
    st = 'B'
    y = time.strftime('%Y', time.localtime(time.time()))

    index = cache.get('index')

    if index:
        num = st + y + str(index + 1)  # 产生单号
        cache.set('index', index + 1)
        return render(request, url,
                      {'budgetform': budget, 'budgetd': budgetd, 'sub': sub, 'len': len(sub), 'num': json.dumps(num)})
    else:
        id = Budget.objects.filter(year=y)
        if len(id) == 0:
            num = st + y + '1'
            cache.set('index', 1)
            return render(request, url, {'budgetform': budget, 'budgetd': budgetd, 'sub': sub, 'len': len(sub),
                                         'num': json.dumps(num)})

        else:
            num = st + y + str(len(id) + 1)
            cache.set('index', len(id) + 1)
            return render(request, url, {'budgetform': budget, 'budgetd': budgetd, 'sub': sub, 'len': len(sub),
                                         'num': json.dumps(num)})


def add_budget(request, url):
    if request.method == "POST":
        post = request.POST


        # postlist =request.POST.getlist('postname',[])
        # k=list(post[u'postname'])
        k = request.POST.getlist("postname")
    return render(request, url, {"post": post, "k": k, })


def remark(request, url):
    if request.method == 'POST':  # 如果表单被提交
        post = BudgetForm(request.POST)  # 获取Post表单数据
        # post.save()
        data = request.POST
        num = request.POST.getlist(u'numd')
        line = request.POST.getlist(u'line')
        company = request.POST.getlist(u'companyd')
        type = request.POST.getlist(u'type')
        year = request.POST.getlist(u'yeard')
        month = request.POST.getlist(u'monthd')
        dept = request.POST.getlist(u'deptd')
        sub = request.POST.getlist(u'subd')
        amt = request.POST.getlist(u'amt')
        cruser = request.POST.getlist(u'cruserd')
        crdate = request.POST.getlist(u'crdated')

        for i in range(len(company)):
            nums = num[i]
            lines = line[i]
            types = type[i]
            crdates = crdate[i]
            amts = amt[i]
            companys = Company.objects.get(id=company[i])
            years = Year.objects.get(year=year[i])
            months = Month.objects.get(id=month[i])
            subjects = Subject.objects.get(num=sub[i])
            depts = Depts.objects.get(id=dept[i])
            crusers = User.objects.get(id=cruser[i])

            entry = Budgetd(num=nums, line=lines, company=companys, type=types, year=years, month=months,
                            cruser=crusers, crdate=crdates, subject=subjects, dept=depts, amt=amts)
            entry.save()
        # if post.is_valid(): # 验证表单
            return render(request, url,
                          {'k': data, 'num': num, 'line': line, 'company': companys, 'year': years, 'month': months,
                           'subject': subjects,
                           'cruser': crusers, 'dept': depts, 'amt': amt, 'len': len(company)})


def test(request, url):
    sub = Year.objects.all()

    return render(request, url, {'sub': sub, 'len': len(sub)})


@csrf_exempt
def ret(request):
    rtxt = BudgetdForm()
    return HttpResponse({"msg": rtxt})

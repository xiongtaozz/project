#coding:utf-8
from __future__ import division
from django.shortcuts import render
from .models import we30_1st

# Create your views here.

def we30_index(request):
    sales = 1000
    SN = we30_1st.objects.all().values_list('id','name','SN','type')
    alls = int(len(we30_1st.objects.all()))/sales*100
    hardwareQuestion = int(len(we30_1st.objects.filter(question_type='硬件')))/sales*100
    name = we30_1st.objects.filter(name = '张三')
    return render(request,'we30.html',{'SN':SN,'name':name,'hardwareQuestion':hardwareQuestion,'alls':alls,})
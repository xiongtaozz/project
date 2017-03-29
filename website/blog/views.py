from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Context
import datetime
class Person(object):
	def __init__(self,name,age,sex):
		self.name=name
		self.age=age
		self.sex=sex
	def say(self):
		return "my name is"+self.name
	
def index(request):
	
     
	t=loader.get_template("index.htm")
	user={'1':'2','3':'4','5':'6','7':'8','9':'10','11':'12','13':'14','15':'16','17':'18'}
	person=Person('jack',25,'female')
	c=Context({'title':'django','name':'tom','user':user,'today':datetime.datetime.now()})
	return HttpResponse(t.render(c))
     
# Create your views here.

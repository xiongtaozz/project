from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect
from .forms import UserForm, PostForm
from .models import MyUser, Question
from django.contrib import auth

from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

def regist(request):
	if request.method == 'POST':
		uf = UserForm(request.POST)
		if uf.is_valid():
			email = uf.cleaned_data['email']
			username = uf.cleaned_data['username']
			password = uf.cleaned_data['password']
			MyUser.objects.create_user(email=email, username=username, password=password)
			return HttpResponseRedirect('/login/')
	else:
		uf = UserForm()
	return render(request, 'micq/regist.html', {'uf': uf})

def login(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/index/')

	email = request.POST.get('email', '')
	password = request.POST.get('password', '')

	user = auth.authenticate(email = email, password=password)

	if user is not None and user.is_active:
		auth.login(request, user)
		return HttpResponseRedirect('/index')
	else:
		return render(request, 'micq/login.html')

@login_required
def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/index/')



def index(request):
	return render(request, 'micq/index.html')


class QuestionDetail(generic.DetailView):
	model = Question 
	template_name = 'micq/question_detail.html'

class QuestionList(generic.ListView):
	model = Question
	template_name = 'micq/question_list.html'

class QuestionCreate(CreateView):
	#form_class = PostForm
	model = Question
	template_name = 'micq/question_create.html'

	# def form_valid(self, form):
	# 	form.instance.created_by = self.request.user
	# 	return super(QuestionCreate, self), form_valid(form)

class QuestionUpdate(UpdateView):
	model = Question

class QuestionDelete(DeleteView):
	model = Question
	success_url = reverse_lazy('question_detail')




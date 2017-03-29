from django import forms 
from . models import MyUser, Question

class UserForm(forms.Form):
	email = forms.EmailField(label="Email Address")
	username = forms.CharField(label="Name", max_length=200)
	password = forms.CharField(label="Password", 
		widget=forms.PasswordInput())
	#remember_me = forms.BooleanField()

	class Meta:
		model = MyUser


class PostForm(forms.Form):
	title = forms.CharField(label='Title', max_length=200)
	body = forms.CharField(label='Body', max_length=200)
	publish = forms.BooleanField()

	class Meta:
		model = Question
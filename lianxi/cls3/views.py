from django.shortcuts import render_to_response

# Create your views here.


def cls3(request):
	return render_to_response( 'cl3.html', {"tmpValue":[1,2,3]})
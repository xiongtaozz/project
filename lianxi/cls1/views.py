from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'cls1.html', {'titles': "Hello", 'words': "<h3>e</h3>"})
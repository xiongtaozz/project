from django.shortcuts import render,render_to_response

def index(request,template_name,year):
    if template_name=='index1.html':
       pass
    else:
        pass
    user = 'cat'
    return render_to_response(template_name,{'user':user})

def test(req):
     pass
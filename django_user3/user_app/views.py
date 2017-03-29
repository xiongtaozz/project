from django.shortcuts import render,render_to_response,HttpResponseRedirect

# Create your views here.
from django.contrib.auth import authenticate, login, logout


'''
  userȨ����֤����
'''


def login_view(req):
    # if req.user.is_authenticated():
            #  ����һ
            # form = LoginFrom(req.POST or None,req.FILES)
            # if form.is_valid():
            #     username = form.cleaned_data['username']
            #     password = form.cleaned_data['password']
    # ������
    if req.method=='POST':
            username=req.POST.get('username','')
            password=req.POST.get('password','')
            # if username and password:
            #     user=User.objects.get(username__icontains=username,password__excat=password)
            user = authenticate(username=username,password=password)
            if user is not None:
                # login(re)
                login(req,user)
                return render_to_response('index.html', locals())
    # else:
    #     return HttpResponseRedirect('/login/?next=%s' % req.path)
    else:
        return render_to_response('login.html', locals())


def logout_view(req):
    logout(req)
    return HttpResponseRedirect('/login/')
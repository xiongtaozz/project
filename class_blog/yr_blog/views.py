from django.shortcuts import render_to_response,HttpResponseRedirect
from yr_blog.forms_view import Login
# Create your views here.


def login(req,tem):
    form = None
    if req.method == 'POST':
        form = Login(req.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # send_mail(
            #     cd['subject'],
            #     cd['message'],
            #     cd.get('email', 'noreply@example.com'),
            #     ['siteowner@example.com'],
            # )
            return HttpResponseRedirect('')
    else:
        form=Login()
    return render_to_response(tem,locals())
from django.shortcuts import render,render_to_response
import xt_blog.models as m

# Create your views here.


def show_techer(req,tem):
    techers=m.Techer.objects.all()
    return render_to_response(tem,{'techers':techers})


def show_stu(req,tem):
    students= m.Student.objects.all()
    return render_to_response(tem,{'stus':students})


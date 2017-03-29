from django.template import Context, loader  
from django.http import HttpResponse  
from blog.models import Job
from django.shortcuts import get_object_or_404, render_to_response  


def home(request):  
    return HttpResponse("Hello Django")  
  
      
def index(request):    
    object_list = Job.objects.order_by('-pub_date')[:10]    
    # t = loader.get_template('mytemp/job_list.html')
    # c = Context({
    #     'object_list': object_list,
    #     })
    return render_to_response('mytemp/job_list.html',locals())
      
      
def detail(request,job_id):
    job = Job.objects.get(pk=job_id)
    return render_to_response('mytemp/job_detail.html', {'job': job})
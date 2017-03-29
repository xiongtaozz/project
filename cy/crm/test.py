from models import Subject
from django.shortcuts import render
def budget(request, url):
    sub=Subject.objects.all()
    return render(request, url, {'sub': sub})
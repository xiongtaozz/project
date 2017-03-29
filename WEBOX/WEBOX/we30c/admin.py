from django.contrib import admin
from .models import *
# Register your models here.

class we30c_admin(admin.ModelAdmin):
    list_display = (
    'id', 'type', 'order_number', 'name', 'SN', 'MAC', 'question', 'phenomenon', 'question_type', 'reason', 'ranges',
    'time')

    search_fields = ['SN']

admin.site.register(we30c_1st,we30c_admin)
admin.site.register(we30c_2nd,we30c_admin)
admin.site.register(we30c_3th,we30c_admin)
admin.site.register(we30c_4th,we30c_admin)
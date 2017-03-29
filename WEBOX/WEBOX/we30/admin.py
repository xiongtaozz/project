from django.contrib import admin
from .models import *
# Register your models here.

class we30_admin(admin.ModelAdmin):
    list_display = (
    'id', 'type', 'order_number', 'name', 'SN', 'MAC', 'question', 'phenomenon', 'question_type', 'reason', 'ranges',
    'time')
    search_fields = ['SN']



admin.site.register(we30_1st,we30_admin)
admin.site.register(we30_2nd,we30_admin)
admin.site.register(we30_3th,we30_admin)
admin.site.register(we30_4th,we30_admin)
admin.site.register(we30_5th,we30_admin)
admin.site.register(we30_6th,we30_admin)
admin.site.register(we30_7th,we30_admin)
admin.site.register(we30_8th,we30_admin)
admin.site.register(we30_9th,we30_admin)
admin.site.register(we30_10th,we30_admin)
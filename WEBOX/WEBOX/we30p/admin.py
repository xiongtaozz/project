from django.contrib import admin
from .models import *
# Register your models here.

class we30p_admin(admin.ModelAdmin):
    list_display = (
    'id', 'type', 'order_number', 'name', 'SN', 'MAC', 'question', 'phenomenon', 'question_type', 'reason', 'ranges',
    'time')

    search_fields = ['SN']



admin.site.register(we30p_1st,we30p_admin)
admin.site.register(we30p_2nd,we30p_admin)
admin.site.register(we30p_3th,we30p_admin)
admin.site.register(we30p_4th,we30p_admin)
admin.site.register(we30p_5th,we30p_admin)
admin.site.register(we30p_6th,we30p_admin)
admin.site.register(we30p_7th,we30p_admin)
admin.site.register(we30p_8th,we30p_admin)
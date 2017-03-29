from django.contrib import admin
from models import Company,Fcy,Subject,Depts,Year,Month,Bps,Bptype

# Register your models here.
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('num', 'des', 'type','upnum')
    list_filter = ('num',)
    date_hierarchy = 'crdate'
    ordering = ('num','upnum')
class MonthAdmin(admin.ModelAdmin):
    list_display = ('year', 'month', 'datedeb','datefin')
    list_filter = ('year',)
    ordering = ('-year',)

admin.site.register(Company)
admin.site.register(Fcy)
admin.site.register(Subject,SubjectAdmin)
admin.site.register(Year)
admin.site.register(Month,MonthAdmin)
admin.site.register(Bptype)
admin.site.register(Bps)
admin.site.register(Depts)

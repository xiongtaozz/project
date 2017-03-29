from django.contrib import admin
from models import Budget,Budgetd
# Register your models here.
class BudgetAdmin(admin.ModelAdmin):
    list_display = ('num', 'company', 'type', 'year', 'month', 'cruser', 'crdate')
class BudgetdAdmin(admin.ModelAdmin):
    list_display = ('num', 'line','company', 'type', 'year', 'month', 'subject', 'dept', 'amt')
admin.site.register(Budget,BudgetAdmin)
admin.site.register(Budgetd,BudgetdAdmin)
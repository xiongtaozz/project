__author__ = 'hunter'
from django.forms import ModelForm, Textarea
from crm.models import Budget, Budgetd
from django import forms

class BudgetForm(ModelForm):
    class Meta:
        model = Budget
        fields = ('num', 'company', 'type', 'year', 'month', 'cruser', 'crdate')


class BudgetdForm(ModelForm):
    class Meta:
        model = Budgetd
        fields = ('num', 'line','company', 'type', 'year', 'month', 'subject', 'dept', 'amt')



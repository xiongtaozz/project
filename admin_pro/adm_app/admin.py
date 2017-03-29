# coding:utf-8
from django.contrib import admin
from adm_app.models import Techer

# Register your models here.


class TecherAdmin(admin.ModelAdmin):
    actions = ['make_sh']
    date_hierarchy = 't_bariy_date'
    # exclude = ['t_sh']
    list_display = ['t_name', 't_email', 't_frist_date']
    # fields = (('t_name', 't_email'), 't_remark')
    fieldsets = (
        (None, {'fields': ('t_name', 't_email')}),
        ('日期', {'fields': ('t_sh', 't_bariy_date')}),
        ('remark', {'fields': ('t_remark',)}),
        ('other', {'fields': ('t_photo', 't_url')}),
    )
    # ordering = ['t_no']  排序

    def make_sh(self, request, queryset):
        rows_updated = queryset.update(t_sh='FR')
        if rows_updated == 1:
            message_bit = '1 story was'
        else:
            message_bit = '%s stories were' % rows_updated
        self.message_user(request, "%s successfully marked as published." % message_bit)
    make_sh.short_description = 'Mark selected stories as sh'

admin.site.register(Techer, TecherAdmin)
# @admin.register(Techer)
# class TecherAdmin(admin.ModelAdmin):
#     fieldsets = (
#         (None, {'fields': ('t_name', 't_email')}),
#         ('日期', {'fields': ('t_sh', 't_bariy_date')}),
#         ('remark', {'fields': ('t_remark',)}),
#         ('other', {'fields': ('t_photo', 't_url')}),
#     )
#     date_hierarchy = 't_bariy_date'
#     # fields = (('t_name', 't_email'), 't_remark')
#     list_display = ['t_name', 't_email']
#     # ordering = ['']
#     actions = ['make_sh']
#
#     def make_sh(self, request, queryset):
#         rows_updated = queryset.update(t_sh='FR')
#         if rows_updated == 1:
#             message_bit = '1 story was'
#         else:
#             message_bit = '%s stories were' % rows_updated
#         self.message_user(request, "%s successfully marked as published." % message_bit)
#     make_sh.short_description = 'Mark selected stories as sh'



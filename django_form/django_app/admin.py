# coding:utf-8
from django.contrib import admin
from django_app.models import *

# Register your models here.


class AdminPro(admin.ModelAdmin):
    class Media:
        js = (
            '/static/js/kindeditor-4.1.10/kindeditor-min.js',
            '/static/js/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.10/config.js',
        )
# class BookLine(admin.StackedInline):
#     model = Book
# class AuthorAdmin(admin.ModelAdmin):
#     inlines = [
#         BookLine,
#     ]#关系为ForeignKey 才可指定
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Product,AdminPro)
admin.site.register(MyUser)

# class profile(admin.StackedInline):
#     model = Profile
#     verbose_name = 'profile'
#
# class UserAdmin(admin.ModelAdmin):
#     inlines = (profile,)
#
# admin.site.unregister(User)
# admin.site.register(User,UserAdmin)

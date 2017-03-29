# coding:utf-8
from django.contrib import admin
from blog_app.models import *
# Register your models here.


class AdminArt(admin.ModelAdmin):

    # 添加富文本编辑器

    class Media:
        js = (
            '/static/js/kindeditor-4.1.10/kindeditor-min.js',
            '/static/js/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.10/config.js',
        )

admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Article, AdminArt)
admin.site.register(Comment)
admin.site.register(Links)
admin.site.register(Ad)

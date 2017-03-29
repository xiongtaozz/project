# coding:utf-8
from django.contrib import admin
from models import Product
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):

    list_display = ('title',)
    list_display_links = ('title', )
    # list_editable = ('click_count',)

    fieldsets = (
        (None, {
            'fields': ('title',)
        }),
        ('其他', {
            'classes': ('collapse',),
            'fields': ('pubmark',)
        }),
    )

    class Media:
        js = (
            '/static/js/kindeditor-4.1.10/kindeditor-min.js',
            '/static/js/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.10/config.js',
        )

admin.site.register(Product, ArticleAdmin)

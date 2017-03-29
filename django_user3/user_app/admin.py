from django.contrib import admin
from user_app import models
# Register your models here.


# class MyUserAdmin(admin.ModelAdmin):
#
#     fields = ('user', 'description', 'headImage', 'scope')

admin.site.register(models.MyUser)
# admin.site.register(models.Product)



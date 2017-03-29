from django.contrib import admin
from mysite import models
# Register your models here.

admin.site.register(models.Answer)
# admin.site.register(models.Answer)
admin.site.register(models.MyUser)
# admin.site.register(models.UserManager)
admin.site.register(models.Question)
# admin.site.register(models.AbstractBaseUser)
# admin.site.register(models.BaseUserManager)
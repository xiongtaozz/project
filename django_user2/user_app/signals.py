# -*- coding:utf-8 -*-
# from django.db.models.signals import post_save
# from django.contrib.auth.models import User
#
# 替换user
# def create_user_detail(sender, instance, signal, *args, **kwargs):
#     print sender, instance, signal, args, kwargs
#     from .models import MyUser
#     if kwargs['created']:
#         u = MyUser()
#         u.__dict__.update(instance.__dict__)
#         u.save()
#
# post_save.connect(create_user_detail, sender=User)



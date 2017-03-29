# coding: utf-8
from django.shortcuts import render, redirect,HttpResponseRedirect
from django.contrib.auth.decorators import permission_required, login_required, user_passes_test
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from myuser.models import Article
from django.contrib.auth.models import User


# Create your views here.

# 登录认证   Post
def do_login(request):
    if request.method == "POST":
        account = request.POST.get("account", None)
        password = request.POST.get("password", None)
        # 返回的是一个对象,如果返回为None ,这里出出一个异常
        # user = User.objects.get(username=account, password=password) # 对象
        # print user
        # authenticate 只针对系统user,None
        # user = None
        user = authenticate(username=account, password=password)
        print user
        if user:
            # 验证通过
            login(request, user)
            return redirect("/index/")
        else:
            # 验证失败
            return HttpResponse(u"验证失败")
    return render(request, "login.html", locals())


def do_logout(request):
    logout(request)
    return redirect("/login/")


# 必须有增加文章的权限才能访问index
def u(user):
    # 做自定义的权限的判断
    return user.has_perms(['myuser.add_article', 'myuser.add_userprofile'])


# 要求必须登录才能访问被装饰的view函数
# @login_required(login_url="/login/")
# @user_passes_test(u, login_url="/login/")
@permission_required('myuser.add_article', login_url="/login/")
def index(request):
    # 2、如果要在代码中动态增加一个note_article的权限如何增加。
    content_type = ContentType.objects.get_for_model(Article)
    print content_type
    if content_type is None:
        Permission.objects.create(codename="find_article",
                                  name="can find article",
                                  content_type=content_type)
    # myuser.groups.is_superuser
    print request.user.is_superuser
    # myuser.groups.all = [group_list]
    print request.user.groups.all()
    # myuser.groups.add(group, group, ...)
    print request.user.groups.add(2)
    print request.user.groups.all()
    # myuser.groups.remove(group, group, ...)
    # request.user.groups.remove(1)
    # print request.user.groups.all()
    # myuser.groups.clear()
    # request.user.groups.clear()
    # print request.user.groups.all()
    # myuser.user_permissions = [permission_list]
    # print request.user.user_permissions.all()
    # myuser.user_permissions.add(permission, permission, ...)
    # request.user.user_permissions.add(22, 23)
    # print request.user.user_permissions.all()
    # myuser.user_permissions.remove(permission, permission, ...)
    # request.user.user_permissions.remove(22, 23)
    # print request.user.user_permissions.all()
    # myuser.user_permissions.clear()
    # request.user.user_permissions.clear()
    # print request.user.user_permissions.all()

    # 判断用户是否有某个model的对应权限：
    # user.has_perm('foo.add_bar')
    print request.user.has_perm('myuser.find_article')
    # user.has_perms(['foo.change_bar'])
    print request.user.has_perms(['myuser.add_article', 'myuser.find_article', 'myuser.add_userprofile'])

    # 获取用户对应的分组权限：
    # user.get_group_permissions
    print request.user.get_group_permissions()

    # 获取用户所有的权限(包括分组和单独的权限)：
    # user.get_all_permissions
    print request.user.get_all_permissions()
    # 获取用户是否拥有某个app的权限
    # user.has_module_perms
    print request.user.has_module_perms("myuser")
    return render(request, "index.html", locals())






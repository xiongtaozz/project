# -*- coding:utf-8 -*-
from django.shortcuts import render,render_to_response,HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, InvalidPage, PageNotAnInteger
from django.db.models import Sum
from django.contrib.auth import authenticate,login,logout
from blog_app.models import *
from blog_app.froms import *
import logging
# Create your views here.

logger = logging.getLogger('blog.views')


def find_index_all(req):
    try:
        open('ttt.txt', 'r')
    except Exception as e:
        logger.error(e)  # 定义异常捕获模式
    return locals()


def login_view(req):
    if req.method == 'POST':
        username = req.POST.get('username', '')
        password = req.POST.get('password', '')

        user = authenticate(username=username, password=password)  # 使用方法只能在auth.user 表下使用
        print '------->', user
        print req.user
        if user is not None:
            req.session['user'] = username
            login(req, user)
    else:
        loginfrom = login_form()
        return render_to_response('login.html', locals())
    return HttpResponseRedirect('/index/')


def index(req):
    try:
        user = req.session['user']
        links = Links.objects.all()[:10]  # 友情连接模块
        articles = get_page(req, Article.objects.all().order_by('-click_count'), 5)  # 这里是最新文章 按照时间倒序
        # 右侧浏览排行榜
        article_clicks = Article.objects.all().order_by('-click_count')[:6]  # 排行部分因是固定显示所以无需使用分页格式
        # 右侧评论排行榜
        # artks = Article.objects.order_by('-click_count').values('title',
        # 'content', 'click_count','date_publish', 'tag').annotate(sum_time=Sum('cmment_set'))
        artks = Article.objects.raw('SELECT ar.id,ar.title,count(com.article_id) as sum_count FROM blog_app_article ar '
                                    'INNER JOIN blog_app_comment com on ar.id=com.article_id GROUP BY ar.id ')[:6]
        # 右侧站长推存榜
        article_recommends = Article.objects.filter(is_recommend=True).order_by('-pk')[:6]
        # 标签云
        tags = Tag.objects.all()[:10]
        return render_to_response('index.html', locals())
    except Exception as e:
        logger.error('index:', e)
    return HttpResponseRedirect('/login/')


def find_blog_id(req, id):
    article = Article.objects.get(pk=id)
    return render_to_response('article.html', locals())


# 分页调用接口
def get_page(req, page_list, count_in_page):
    pator = Paginator(page_list, count_in_page)
    try:
        page = int(req.POST.get('page', 1))
        page_list = pator.page(page)
    except (EmptyPage, InvalidPage, PageNotAnInteger):
        page_list = pator.page(1)
    return page_list
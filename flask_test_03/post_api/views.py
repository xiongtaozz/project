# coding:utf-8
from post_api import post_api
from .forms import AddPostForm
from flask import request, render_template, redirect
from app.models import Post
from app import db


# {#    资料: http://www.hustlzp.com/post/2015/10/flask-macros#}

@post_api.route('/add', methods=['GET', 'POST'])
def add_post():
    print('postapi add_post')
    form = AddPostForm(request.form)
    if request.method == 'GET':
        return render_template('add_post.html', form = form)
    else:
        if form.validate():
            post = Post()
            post.title = form.title.data
            post.content = form.content.data
            db.session.add(post)
            db.session.commit()
        else:
            print(form.errors)
        return redirect('/')


@post_api.route('/delete/<int:id>')
def del_post(id):
    print(id)
    return redirect('/')


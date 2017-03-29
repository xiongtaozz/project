# coding:utf-8

from flask import Flask, render_template, flash, redirect, url_for, session,request
# from flask_bootstrap import Bootstrap
from config import db
from form import PostForm
from models import Work
from datetime import datetime
# from flask_login import current_user

app = Flask(__name__)
Bootstrap(app)
# 读取外部文件
app.config.from_pyfile('secure')


@app.route('/', methods=['GET', 'POST'])
def index():
    posts = None
    form = PostForm()
    print request.method
    print form.validate_on_submit()
    if form.validate_on_submit():
        print 'GOOD1'
        work = PostForm(body=form.body.data)
        db.session.add(work)
        return redirect(url_for('index'))
    posts = Work.query.order_by(Work.time.desc()).all()
    return render_template('index.html', form=form, posts=posts)

@app.route('/add',methods=['GET','POST'])
def add():
    form = PostForm()
    if form.validate_on_submit():
        return redirect('/posts')
    return render_template('index.html', form=form, posts=posts)

# # 添加新的事件
# @app.route('/posts', methods=['GET', 'POST'])
# @app.route('/posts/<int:id>', methods=['GET', 'POST'])
# def post(id):
#     # 详情页
#     post_id = Work.query.filter_by(post_id=id).first()
#     if post_id is None:
#         raise Exception
#     works = post_id.works.order_by(Work.time.desc()).all()
#     return render_template('main.html', post_id=post_id, works=works)


    # detail_id = Work.query.get_or_404(id)
    #
    # # 添加事项窗体
    # form = PostForm()
    # # 保存事件
    # if form.validate_on_submit():
    #     work = Work(detail=form.body.data)
    #     db.session.add(work)
    #     db.session.commit()
    #     print form.body.data
    # return render_template('index.html', form=form, post=detail_id)





# #编辑已有的事件
# @app.route('/edit',methods=['GET','POST'])
# @app.route('/edit/<int:id>',methods=['GET','POST'])
# def edit(id):
#     form = PostForm()
#     if id == 0:
#         post = Work(author=current_user)
#     else:
#         post = Work.query.get_or_404(id)
#
#     if form.validate_on_submit():
#         post.body = form.body.data
#         post.title = form.edit.data
#         db.session.add(post)
#         db.session.commit()
#
#         return redirect(url_for('.post',id=post.id))
#     form.title.data = post.title
#     form.body.data = post.body
#
#
#     title = 'Add'
#     if id > 0:
#         title = ()


# 删除已有的事件
# @app.route('/delete/<int:id>',methods=['GET','POST'])
# def delete(id):
#     pass


# 复选框设置
# @app.route('/check/<int:id>',methods=['GET','POST'])
# def check(id):
#     pass


# 404自定义页面
# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template('404.html'),404


# #500自定义页面
# @app.errorhandler(500)
# def internal_server_error(e):
#     render_template('500.html'),500



if __name__ == '__main__':
    app.run(debug=True)

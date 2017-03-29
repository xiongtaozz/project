from app import app
from flask import render_template
from .models import Post


@app.route('/')
@app.route('/home')
def index():
    posts = Post.query.all()
    return render_template('post.html', posts=posts)


@app.route('/aboutme')
def aboutme():
    return render_template('aboutme.html', user_name='xt')



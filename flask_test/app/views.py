from app import app
from flask import render_template
from app.models import Post


@app.route('/')
@app.route('/home')
def index():
    # Post.query.all()
    return render_template('index.html', name='xt')
# coding:utf-8
from flask import Flask, render_template, url_for, request, redirect
from models import Pool as ps
# from flask.ext.sqlalchemy import SQLAlchemy
from dbs import Products
from config import db
from froms import ProFrom

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/index/<int:page>')
def index(page):
    if request.method == 'GET':
        print page
        # page = request.args.get('page', 1)
        indexCss = url_for('static', filename='css/bootstrap.min.css')
        if page > 1:
            prospage = Products.query.paginate(page, 2, False)
        else:
            prospage = Products.query.paginate(1, 2, False)
        print prospage.total
        print prospage.total/2   # 页数定义
        return render_template('list.html', indexCss=indexCss,
                               pros=prospage.items,
                               prospage=prospage,
                               total=prospage.total/2,
                               a=3, b=2)


@app.route('/add', methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        query = request.form
        pro = Products()
        pro.name = query['name']
        pro.style = query['pro_style']
        pro.qty = query['pro_qty']
        pro.price = query['pro_price']
        pro.type = query['pro_type']
        pro.remark = query['remark']
        db.session.add(pro)
        db.session.commit()
        return redirect('/index/1')
    else:
        return render_template('add.html')


@app.route('/add_from', methods=['POST', 'GET'])
def add_from():
    proFrom = ProFrom()
    if proFrom.validate_on_submit():
        pro = ProFrom(body=proFrom.body.data)
        db.session.add(pro)
        db.session.commit()
        return redirect('/index/1')
    else:
        return render_template('add_from.html', proFrom=proFrom)

if __name__ == '__main__':
    app.run(debug=True)

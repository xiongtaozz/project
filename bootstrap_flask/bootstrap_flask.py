from flask import Flask,render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.script import Manager

app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/user/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()

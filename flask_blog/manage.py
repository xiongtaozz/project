from flask_script import Manager, Server
from app import app, db
from app.models import Post

manager = Manager(app)
manager.add_command('runserver',
                    Server(host='127.0.0.1', port=8000, use_debugger=True))


@manager.command
def create_table():
    db.create_all()


@manager.command
def add_post(title, content):
    post = Post(title=title, content=content)
    db.session.add(post)
    db.session.commit()


@manager.command
def query():
    posts = Post.query.all()
    for post in posts:
        print(post, post.content)
    print(len(posts))

if __name__ == '__main__':
    manager.run()
from flask_script import Manager, Server
from app import app, db
from app.models import Post

manager = Manager(app)
manager.add_command('runserver',
                    Server(host='127.0.0.1', port=8000, use_debugger=True))


if __name__ == '__main__':
    manager.run()
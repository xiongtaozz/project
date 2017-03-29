from flask_script import Manager, Server
from app import app, db

manager = Manager(app)
manager.add_command('runserver',
                    Server(host='127.0.0.1', port=8080, use_debugger=True))


@manager.command
def create_table():
    db.create_all()

if __name__ == '__main__':
    manager.run()


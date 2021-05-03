from app import create_app, db
from flask_script import Manager, Server
from app.models import Subscription, Writer, Blog, Comment
from flask_migrate import Migrate, MigrateCommand

app = create_app('test')

manager = Manager(app)
manager.add_command('server', Server)

migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

@manager.shell
def make_app_context():
    return dict(app = app, db = db, Writer = Writer, Blog = Blog, Comment = Comment, Subscription = Subscription)

@manager.command
def test():
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    manager.run()

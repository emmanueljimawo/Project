from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import os
import unittest
import coverage

from project import app, db

app.config.from_object('config.BaseConfig')
# app.config.from_envvar('PRODUCTION_CONFIG',silent=True)
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

@manager.command
def test():
    """Runs the test without coverage"""
    tests=unittest.TestLoader().discover('.')
    unittest.TextTestRunner(verbosity=2).run(tests)

@manager.command
def cov():
    """Runs unnitest with coverage"""
    cov=coverage.coverage(branch=True, include='project/*')
    cov.start()
    tests=unittest.TestLoader().discover('.')
    unittest.TextTestRunner(verbosity=2).run(tests)
    cov.stop()
    cov.save()
    print('Coverage Summary:')
    cov.report()
    basedir = os.path.abspath(os.path.dirname(__file__))
    covdir = os.path.join(basedir, 'coverage')
    cov.html_report(directory=covdir)
    cov.erase()

if __name__ == '__main__':
    manager.run()

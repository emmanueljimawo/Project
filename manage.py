from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import os
import unittest
import coverage

from project import app, db

app.config.from_object('config.ProductionConfig')
# app.config.from_envvar('PRODUCTION_CONFIG',silent=True)
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

@manager.command
def test():
    """Runs the test without coverage"""
    tests = unittest.TestLoader().discover('.')
    unittest.TextTestRunner(verbosity=2).run(tests)

@manager.command
def cov():
    """Runs unnitest with coverage"""
    covr = coverage.coverage(branch=True, include='project/*', omit='*/__init__.py')
    covr.start()
    tests = unittest.TestLoader().discover('.')
    unittest.TextTestRunner(verbosity=2).run(tests)
    covr.stop()
    covr.save()
    print('Coverage Summary:')
    covr.report()
    basedir = os.path.abspath(os.path.dirname(__file__))
    covdir = os.path.join(basedir, 'coverage')
    covr.html_report(directory=covdir)
    covr.erase()

if __name__ == '__main__':
    manager.run()

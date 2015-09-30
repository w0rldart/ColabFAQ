# project/util.py


from flask.ext.testing import TestCase

from app import factory
from app.models import db, User


class BaseTestCase(TestCase):

    def create_app(self):
        testapp = factory.create_app('project.config.TestingConfig')
        return test

    def setUp(self):
        db.create_all()
        # user = User(
        #     email="test@user.com",
        #     password="just_a_test_user",
        #     confirmed=False
        # )
        # db.session.add(user)
        # db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
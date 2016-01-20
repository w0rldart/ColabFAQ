from flask.ext.script import Command
from flask.ext.security.confirmable import confirm_user

from faqcolab.models import FlaskDocument, db, user_datastore


class ResetDB(Command):
    """Drops all tables and recreates them"""
    def run(self, **kwargs):
        self.drop_collections()

    @staticmethod
    def drop_collections():
        for klass in FlaskDocument.all_subclasses():
            klass.drop_collection()


class PopulateDB(Command):
    """Fills in predefined data to DB"""
    def run(self, **kwargs):
        self.create_roles()
        self.create_users()

    @staticmethod
    def create_roles():
        for role in ('admin', 'editor', 'author'):
            user_datastore.create_role(name=role, description=role)

        user_datastore.commit()

    @staticmethod
    def create_users():
        for u in (('matt', 'snow', 'matt@lp.com', 'password', ['admin'], True),
                  ('joe', 'doe', 'joe@lp.com', 'password', ['editor'], True),
                  ('jill', 'mcarthy', 'jill@lp.com', 'password', ['author'], True),
                  ('tiya', 'sheer', 'tiya@lp.com', 'password', [], False)):
            user = user_datastore.create_user(
                first_name=u[0],
                last_name=u[1],
                email=u[2],
                password=u[3],
                roles=u[4],
                active=u[5]
            )
            confirm_user(user)

            user_datastore.commit()

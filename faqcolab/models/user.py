import datetime
from flask.ext.security import UserMixin, RoleMixin
from faqcolab.models import db, FlaskDocument

class Role(FlaskDocument, RoleMixin):
    name          = db.StringField(required=True, unique=True)
    description   = db.StringField(required=True)

    meta = {
        'indexes': [
            {'fields': ['name'], 'unique': True}
        ]
    }

    def __unicode__(self):
        return self.name


class User(FlaskDocument, UserMixin):
    email            = db.StringField(required=True, unique=True)
    password         = db.StringField(required=True)
    active           = db.BooleanField()

    first_name       = db.StringField(max_length=64, required=True)
    last_name        = db.StringField(max_length=64, required=True)

    registered_at    = db.DateTimeField(default=datetime.datetime.utcnow())
    confirmed        = db.BooleanField()
    confirmed_at     = db.DateTimeField()

    last_login_at    = db.DateTimeField()
    current_login_at = db.DateTimeField()
    last_login_ip    = db.StringField(max_length=45)
    current_login_ip = db.StringField(max_length=45)
    login_count      = db.IntField()

    company          = db.ReferenceField('Company')
    roles            = db.ListField(db.ReferenceField(Role), default=[])

    meta = {
        'indexes': [
            {'fields': ['email'], 'unique': True}
        ]
    }


    def __unicode__(self):
        return self.first_name + ' ' + self.last_name

    def has_role(self, role_name):
        return self.roles.filter_by(name=role_name).first()

    @property
    def profile(self):
        profile = UserProfile.objects(user=self).get()

        if (not profile.avatar):
            profile.avatar = '/static/images/avatar/nan.jpg'

        return profile


class UserProfile(FlaskDocument):
    user        = db.ReferenceField(User)
    avatar      = db.StringField()
    description = db.StringField(max_length=128)
    preferences = db.StringField()

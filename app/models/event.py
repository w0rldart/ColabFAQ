import datetime
from app.models import db, FlaskDocument

class Event(FlaskDocument):
    name          = db.StringField(max_length=64, required=True)
    description   = db.StringField(required=True)
    visible       = db.BooleanField(default=True)
    author        = db.ReferenceField('User')
    company       = db.ReferenceField('Company')
    created_at    = db.DateTimeField(default=datetime.datetime.utcnow())


    def __unicode__(self):
        return self.name
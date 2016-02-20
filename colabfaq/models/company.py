import datetime
from colabfaq.models import db, FlaskDocument

class Company(FlaskDocument):
    name        = db.StringField(max_length=64, required=True)
    description = db.StringField(required=True)
    author      = db.ReferenceField('User')
    members     = db.ListField(db.ReferenceField('User'), default=[])
    created_at  = db.DateTimeField(default=datetime.datetime.utcnow())


    def __unicode__(self):
        return self.name

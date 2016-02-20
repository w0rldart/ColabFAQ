import datetime
from colabfaq.models import db, FlaskDocument

class Faq(FlaskDocument):
    name        = db.StringField(max_length=64, required=True)
    description = db.StringField(required=True)
    private     = db.BooleanField(default=False)
    event       = db.ReferenceField('Event')
    created_at  = db.DateTimeField(default=datetime.datetime.utcnow())


    def __unicode__(self):
        return self.name

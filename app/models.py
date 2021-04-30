from . import db


class Writer(db.Model):
    username = db.Column(db.String(120))
    
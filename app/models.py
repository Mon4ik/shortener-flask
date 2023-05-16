from datetime import datetime

from . import db


class URLS(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.Text, nullable=False)
    short = db.Column(db.String(40), unique=True, nullable=False)
    visits = db.Column(db.Integer, default=0)
    date = db.Column(db.DateTime, default=datetime.utcnow())

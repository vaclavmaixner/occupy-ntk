from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView

class Occupation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    floor_6 = db.Column(db.Integer())
    floor_5 = db.Column(db.Integer())
    floor_4 = db.Column(db.Integer())
    floor_3 = db.Column(db.Integer())
    sum_of_people = db.Column(db.Integer())
    floor_6_perc = db.Column(db.Integer())
    floor_5_perc = db.Column(db.Integer())
    floor_4_perc = db.Column(db.Integer())
    floor_3_perc = db.Column(db.Integer())
    overall_occ = db.Column(db.Integer())
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<Occupation {}>'.format(self.timestamp)

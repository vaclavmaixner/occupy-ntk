from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView
import numpy as np

class Occupation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    floor_6_perc = db.Column(db.Integer())
    floor_5_perc = db.Column(db.Integer())
    floor_4_perc = db.Column(db.Integer())
    floor_3_perc = db.Column(db.Integer())
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<Occupation {}>'.format(self.timestamp)
    
    def get_number_of_people(self):
        no_people = {}

        no_people['floor_6'] = round(self.floor_6_perc/100*323)
        no_people['floor_5'] = round(self.floor_5_perc/100*275)
        no_people['floor_4'] = round(self.floor_4_perc/100*333)
        no_people['floor_3'] = round(self.floor_3_perc/100*331)

        return no_people

    def get_floors_as_list(self):
        return [self.floor_6_perc, self.floor_5_perc, self.floor_4_perc, self.floor_3_perc]

    def get_sum_of_people(self):
        sum_of_people = round(np.sum(self.get_floors_as_list()))
        return sum_of_people

    def get_overall_perc(self):
        overall_perc = int(round(self.get_sum_of_people()/1262 * 100))
        return overall_perc

    def get_tuple_sum_of_people(self):
        return (self.timestamp.date, self.sum_of_people)
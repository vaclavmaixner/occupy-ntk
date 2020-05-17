from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.fileadmin import FileAdmin

from apscheduler.schedulers.background import BackgroundScheduler
from app import scraper_task
from flask_moment import Moment
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
moment = Moment(app)

from app import routes, models
from app.models import Occupation

admin = Admin(app, name='Admin Zone')
admin.add_view(ModelView(Occupation, db.session))

from app import scraper_task
import requests

TARGET_URL = 'https://www.techlib.cz/cs/83028-mista-ke-studiu'

def run_scraper():
    # occ_list contains percentages of occupation scraped from website
    r = requests.get(TARGET_URL)

    occ_list = scraper_task.run_scraper(r.text)
    
    occupation = Occupation(floor_6_perc=occ_list[0],
    floor_5_perc=occ_list[1], floor_4_perc=occ_list[2], floor_3_perc=occ_list[3])
    
    db.session.add(occupation)
    db.session.commit()



sched = BackgroundScheduler()
sched.add_job(run_scraper,'cron',hour='8-23', minute='*/5')
sched.start()


# generate dummy data and push it into database
import numpy as np
import pandas as pd

LENGTH = 4000
def add_dummy_data(LENGTH):
    num_rows_deleted = db.session.query(Occupation).delete()

    dummy_times = pd.date_range('2020-03-01', periods=LENGTH, freq='5T')
    dummy_occupations = np.random.randint(0,100,size=(LENGTH, 4)).astype(np.int32)

    for datapoint in range(LENGTH):
        # print(dummy_times[datapoint])
        # print(dummy_occupations[datapoint][0])

        # print(dummy_occupations[datapoint][1])

        dummy_occupation = Occupation(floor_6_perc=int(dummy_occupations[datapoint][0]),
        floor_5_perc=int(dummy_occupations[datapoint][1]),
        floor_4_perc=int(dummy_occupations[datapoint][2]),
        floor_3_perc=int(dummy_occupations[datapoint][3]),
        timestamp=dummy_times[datapoint])
        
        db.session.add(dummy_occupation)
    
    
    db.session.commit()

add_dummy_data(LENGTH)
    
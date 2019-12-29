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

# def sensor():
#     """ Function for test purposes. """
#     print("Scheduler is alive!")

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

def run_scraper():
    occ_list = scraper_task.run_scraper()
    
    occupation = Occupation(floor_6 = occ_list[0][0], floor_5 = occ_list[0][1],
    floor_4 = occ_list[0][2], floor_3 = occ_list[0][3], floor_6_perc=occ_list[1][0],
    floor_5_perc=occ_list[1][1], floor_4_perc=occ_list[1][2], floor_3_perc=occ_list[1][3],
    overall_occ=occ_list[2], sum_of_people=int(occ_list[3]))
    db.session.add(occupation)
    db.session.commit()


sched = BackgroundScheduler()
sched.add_job(run_scraper,'cron',hour='8-23', minute='*/5')
sched.start()


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
    # occupation = Occupation(floor_6 = 1, floor_5=2, floor_4=3, floor_3=4)
    occupation = Occupation(floor_6 = occ_list[0], floor_5 = occ_list[1], floor_4 = occ_list[2], floor_3 = occ_list[3])
    db.session.add(occupation)
    db.session.commit()

sched = BackgroundScheduler()
# sched.add_job(scraper_task.run_scraper,'interval',seconds=30)
# sched.add_job(run_scraper,'interval',seconds=15)
sched.add_job(run_scraper,'cron',hour='8-23', minute='*/15')
sched.start()
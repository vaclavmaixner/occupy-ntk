from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.fileadmin import FileAdmin

from apscheduler.schedulers.background import BackgroundScheduler
from app import scraper_task

# def sensor():
#     """ Function for test purposes. """
#     print("Scheduler is alive!")



sched = BackgroundScheduler()
sched.add_job(scraper_task.run_scraper,'interval',seconds=30)
sched.start()


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models
from app.models import Occupation

admin = Admin(app, name='Admin Zone')
admin.add_view(ModelView(Occupation, db.session))
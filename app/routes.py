from app import app
from app import db
from flask import render_template, flash, redirect, url_for, request
from werkzeug.urls import url_parse
from datetime import datetime, timedelta

import requests
from bs4 import BeautifulSoup
import re
import numpy as np

from app import scraper_task, plotting
from app.models import Occupation

from datetime import datetime
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

from bokeh.embed import components
from bokeh.models import ColumnDataSource, HoverTool, PrintfTickFormatter
from bokeh.plotting import figure
from bokeh.transform import factor_cmap


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    r = requests.get('https://www.techlib.cz/cs/83028-mista-ke-studiu')

    soup = BeautifulSoup(r.text, 'html.parser')

    occupations = Occupation.query.order_by(Occupation.id.desc()).limit(1)
    occupation = occupations[0]

    history_4hours = Occupation.query.order_by(Occupation.id.desc()).limit(48)
    history_24hours = Occupation.query.order_by(
        Occupation.id.desc()).limit(288)
    history_week = Occupation.query.order_by(Occupation.id.desc()).limit(2016)

    script_4hours, div_4hours = components(
        plotting.plot_4hours(history_4hours))
    script_24hours, div_24hours = components(
        plotting.plot_24hours(history_24hours))
    script_week, div_week = components(plotting.plot_week(history_week))

    week_before = datetime.today() - timedelta(days=7)
    week_before_data = Occupation.query.filter(
        Occupation.timestamp == week_before).all()

    return render_template('index.html', occupation=occupation,
                           script_4hours=script_4hours, div_4hours=div_4hours,
                           script_24hours=script_24hours, div_24hours=div_24hours,
                           script_week=script_week, div_week=div_week,
                           week_before_data=week_before_data)

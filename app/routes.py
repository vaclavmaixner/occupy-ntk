from app import app
from app import db
from flask import render_template, flash, redirect, url_for, request
from werkzeug.urls import url_parse
from datetime import datetime

import requests
from bs4 import BeautifulSoup
import re
import numpy as np

from app import scraper_task
from app.models import Occupation

from datetime import datetime
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

from bokeh.embed import components
from bokeh.models import ColumnDataSource, HoverTool, PrintfTickFormatter
from bokeh.plotting import figure
from bokeh.transform import factor_cmap

# def push_to_db(no_people):
#     occupation = Occupation(
#         floor_6=no_people[0], floor_5=no_people[1], floor_4=no_people[2], floor_3=no_people[3])
#     db.session.add(occupation)
#     db.session.commit()
#     print('Your post is now live!')

def create_figure(time_col, sum_col):
    p = figure(plot_height=400, title='Did/Did not Survive for Current Class')
    p.line(time_col, sum_col)

    return p

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    r = requests.get('https://www.techlib.cz/cs/83028-mista-ke-studiu')

    soup = BeautifulSoup(r.text, 'html.parser')

    # occupation = soup.find_all('div', {'class': 'progress-bar'})
    # no_people = scraper_task.scrape(occupation)[0]
    # percentages = scraper_task.scrape(occupation)[1]
    # overall_occ = scraper_task.scrape(occupation)[2]
    # sum_of_people = scraper_task.scrape(occupation)[3]
    # occupation = Occupation(
    #     floor_6=no_people[0], floor_5=no_people[1], floor_4=no_people[2], floor_3=no_people[3])

    occupations = Occupation.query.order_by(Occupation.id.desc()).limit(1)
    occupation = occupations[0]
    history = Occupation.query.order_by(Occupation.id.desc()).limit(40)

    time_col = []
    sum_col = []
    for h in history:
        # time = h.timestamp.strftime('%H:%M:%S')
        # time_col.append(time)
        time_col.append(h.timestamp)
        sum_col.append(h.sum_of_people + 1)
    
    fig = figure(plot_width=800, plot_height=400, x_axis_type='datetime', title='Occupation in last 2 hrs')
    # , tools="hover", tooltips='$name @time_col')
    fig.vbar(
        x=time_col,
        top=sum_col,
        width=200000,
        bottom=0,
        color= (92,184,92)
    )
    script, div = components(fig)


    return render_template('index.html', occupation=occupation, history=history, script=script, div=div)
# return 'hello'

@app.route('/plot', methods=["GET"])
def plot_view():
    pass

# @app.route('/news/<int:id>')
# def news_article(id):
#     article = Occupation.query.get_or_404(id)
#     return render_template('news-post.html', articles=[article])

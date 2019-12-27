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


def push_to_db(no_people):
    occupation = Occupation(
        floor_6=no_people[0], floor_5=no_people[1], floor_4=no_people[2], floor_3=no_people[3])
    db.session.add(occupation)
    db.session.commit()
    print('Your post is now live!')


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    r = requests.get('https://www.techlib.cz/cs/83028-mista-ke-studiu')

    soup = BeautifulSoup(r.text, 'html.parser')

    occupation = soup.find_all('div', {'class': 'progress-bar'})
    no_people = scraper_task.scrape(occupation)[0]
    percentages = scraper_task.scrape(occupation)[1]
    overall_occ = scraper_task.scrape(occupation)[2]
    sum_of_people = scraper_task.scrape(occupation)[3]
    # scraper_task.push_to_db(floors_people)
    occupation = Occupation(
        floor_6=no_people[0], floor_5=no_people[1], floor_4=no_people[2], floor_3=no_people[3])
    # db.session.add(occupation)
    # db.session.commit()

    # history = 

    return render_template('index.html', occupation=occupation, percentages=percentages, overall_occ=overall_occ, sum_of_people=sum_of_people)
# return 'hello'


# @app.route('/news/<int:id>')
# def news_article(id):
#     article = Occupation.query.get_or_404(id)
#     return render_template('news-post.html', articles=[article])

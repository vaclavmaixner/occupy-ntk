from app import app
from app import db
from flask import render_template, flash, redirect, url_for, request
from werkzeug.urls import url_parse
from datetime import datetime

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


def get_figure_cols(history):
    time_col = []
    sum_col = []

    for h in history:
        time_col.append(h.timestamp)
        sum_col.append(h.get_sum_of_people()+20)

    return time_col, sum_col

def plot_4hours(history):
    time_col, sum_col = get_figure_cols(history)

    p = figure(plot_width=800, plot_height=400, 
        x_axis_type='datetime', title='Occupation in last 4 hours')
    p.vbar(
        x=time_col,
        top=sum_col,
        width=200000,
        bottom=0,
        color= (92,184,92)
    )
    return p

def plot_24hours(history):
    time_col, sum_col = get_figure_cols(history)

    p2 = figure(plot_width=800, plot_height=400, 
        x_axis_type='datetime', title='Occupation in last 24 hours')
    p2.vbar(
        x=time_col,
        top=sum_col,
        width=200000,
        bottom=0,
        color= (92,184,92)
    )
    return p2

def plot_week(history):
    time_col, sum_col = get_figure_cols(history)

    p3 = figure(plot_width=800, plot_height=400, 
        x_axis_type='datetime', title='Occupation in last week')
    p3.vbar(
        x=time_col,
        top=sum_col,
        width=200000,
        bottom=0,
        color= (92,184,92)
    )
    return p3

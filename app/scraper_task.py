import requests
from bs4 import BeautifulSoup
import re 
import numpy as np


def perc_to_people(floors_percentages):
    floors_percentages[:] = [x/100 for x in floors_percentages]

    no_people = []
    for i in range(len(floors_percentages)):
        if i == 0:
            no_people.append(floors_percentages[i]*323)
        elif i == 1:
            no_people.append(floors_percentages[i]*275)
        elif i == 2:
            no_people.append(floors_percentages[i]*333)
        elif i == 3:
            no_people.append((floors_percentages[i]*331))
    no_people[:] = [round(x) for x in no_people]

    return no_people


def scrape(occupation):
    floors_percentages = []
    floors_percentages_out = []
    pattern = re.compile(r'width:\s*([0-9]+)')

    for i in range(len(occupation)):
        occ = occupation[i].get('style')
        floor_occ = pattern.search(occ).group(1)
        floors_percentages.append(int(floor_occ))
        floors_percentages_out.append(int(floor_occ))

    return floors_percentages_out
    

def run_scraper():
    r = requests.get('https://www.techlib.cz/cs/83028-mista-ke-studiu')

    soup = BeautifulSoup(r.text, 'html.parser')

    occupation = soup.find_all('div', {'class': 'progress-bar'})

    return scrape(occupation)
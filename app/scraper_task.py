from bs4 import BeautifulSoup
import re
import numpy as np


def perc_to_people(floors_percentages):
    floors_percentages[:] = [x / 100 for x in floors_percentages]

    no_people = []

    max_floor_capacity = np.array([323, 275, 333, 331])
    floors_percentages = np.array(floors_percentages)

    no_people = max_floor_capacity * floors_percentages

    no_people = [round(x) for x in list(no_people)]

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


def get_soup(html):
    return BeautifulSoup(html, 'html.parser')


def run_scraper(html):
    soup = get_soup(html)

    occupation = soup.find_all('div', {'class': 'progress-bar'})

    return scrape(occupation)

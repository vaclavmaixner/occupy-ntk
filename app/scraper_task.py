import requests
from bs4 import BeautifulSoup
import re 
import numpy as np
# from app import db
# from app.models import Occupation

r = requests.get('https://www.techlib.cz/cs/83028-mista-ke-studiu')

soup = BeautifulSoup(r.text, 'html.parser')

occupation = soup.find_all('div', {'class': 'progress-bar'})


def perc_to_people(floors_percentages):
    floors_percentages[:] = [x/100 for x in floors_percentages]

    # print(floors_percentages)
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
    # print(no_people)
    # print(np.sum(no_people))
    # print(len(no_people))

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

    TOTAL_CAPACITY = 1262

    no_people = perc_to_people(floors_percentages)
    sum_of_people = round(np.sum(no_people))
    overall_occ = int(round(np.sum(no_people)/TOTAL_CAPACITY * 100))
    # print(overall_occ)
    return no_people, floors_percentages_out, overall_occ, sum_of_people

# def push_to_db(no_people):
#     occupation = Occupation(floor_6 = no_people[0], floor_5=no_people[1], floor_4=no_people[2], floor_3=no_people[3])
#     db.session.add(occupation)
#     db.session.commit()
#     print('Your post is now live!')

def run_scraper():
    r = requests.get('https://www.techlib.cz/cs/83028-mista-ke-studiu')

    soup = BeautifulSoup(r.text, 'html.parser')

    occupation = soup.find_all('div', {'class': 'progress-bar'})
    floors_people = scrape(occupation)[0]
    return floors_people
    # push_to_db(floors_people)
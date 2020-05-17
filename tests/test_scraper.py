from app import app, scraper_task
import requests
import html


def test_scraper():
    with open("tests/mockup_ntk.html", "r") as f:
        local_html = f.read()
    scraper = scraper_task.run_scraper(local_html)

    assert scraper == [71, 41, 31, 61]


def test_perc_to_people():
    no_people = scraper_task.perc_to_people([10, 20, 30, 40])
    assert no_people == [32, 55, 100, 132]

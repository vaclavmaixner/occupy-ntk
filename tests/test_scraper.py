from app import app, scraper_task
import requests, html

def test_scraper():
    with open("tests/mockup_ntk.html", "r") as f:
        local_html = f.read()
    scraper = scraper_task.run_scraper(local_html)

    assert scraper == [71, 41, 31, 61]
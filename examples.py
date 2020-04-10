import os

from pyuni import Client, University, Scraper

university_scraper = University.UNIVERSITY_OF_MELBOURNE

with Client(headless=False) as client:
    with Scraper(client=client, university_scraper=university_scraper) as scraper:
        scraper.authenticate(os.environ['TEST_USERNAME'], os.environ['TEST_PASSWORD'])
        scraper.scrape()

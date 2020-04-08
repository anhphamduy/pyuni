import os

from pyuni import Client, University, Scraper

university_scraper = University.UNIVERSITY_OF_MELBOURNE
client = Client(headless=False)
scraper = Scraper(client=client, university_scraper=university_scraper)

scraper.authenticate(os.environ['TEST_USERNAME'], os.environ['TEST_PASSWORD'])

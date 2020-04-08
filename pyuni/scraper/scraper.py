class Scraper:

    def __init__(self, client, university_scraper):
        self.client = client
        self.university_scraper = university_scraper()

    def scrape(self):
        raise NotImplementedError()

    def authenticate(self, username, password):
        """
        Authenticate the client against the university system
        :rtype: None
        :param username: the username or email to log in to the uni system
        :type username: str
        :param password: the password to log in to the system
        :type password: str
        """
        self.university_scraper.authenticate(self.client, username, password)

from .university_scraper import UniversityScraper


class UniversityOfMelbourneScraper(UniversityScraper):
    login_url = 'https://mytimetable.students.unimelb.edu.au/even/student'
    login_success_url = 'https://mytimetable.students.unimelb.edu.au/even/student?ss='

    urls = {
        'homepage': 'https://mytimetable.students.unimelb.edu.au/even/student'
    }

    element_selectors = {
        'username_input': '#usernameInput',
        'password_input': '#passwordInput',
        'login_button': '.page-inner form button[type="submit"]',
        'timetable_anchor_menu': 'a[href="#timetable"]'
    }

    @classmethod
    def authenticate(cls, client, username, password):
        client.get(cls.login_url)

        username_input = client.find_element_by_css_selector(cls.element_selectors['username_input'])
        password_input = client.find_element_by_css_selector(cls.element_selectors['password_input'])
        login_button = client.find_element_by_css_selector(cls.element_selectors['login_button'])

        username_input.send_keys(username)
        password_input.send_keys(password)
        login_button.click()

        if cls.login_success_url not in client.current_url:
            # TODO: raise authentication error in here
            raise NotImplementedError()

    @classmethod
    def scrape(cls, client):
        cls.go_to_timetable_page(client)

    @classmethod
    def go_to_timetable_page(cls, client):
        client.get(cls.urls['homepage'])
        client.find_element_by_css_selector(cls.element_selectors['timetable_anchor_menu']).click()

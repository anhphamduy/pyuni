from abc import ABC, abstractmethod


class UniversityScraper(ABC):
    @property
    @abstractmethod
    def element_selectors(self):
        """
        :return: the dictionary of the selectors that are used within the class
        :rtype: dict
        """
        pass

    @property
    @abstractmethod
    def login_url(self):
        """
        :return: the login url of the corresponding university
        :rtype: str
        """
        pass

    @property
    @abstractmethod
    def urls(self):
        """
        :return: a dict of urls that are used within the class
        :rtype: dict
        """
        pass

    @abstractmethod
    def authenticate(self, username, password):
        """
        Authenticate the client against the university system
        :rtype: None
        :param username: the username or email to log in to the uni system
        :type username: str
        :param password: the password to log in to the system
        :type password: str
        """
        pass
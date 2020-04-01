from abc import ABC, abstractmethod


class UniversityDetail(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def login_url(self):
        pass

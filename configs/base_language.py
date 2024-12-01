from abc import ABC, abstractmethod


class Language(ABC):

    @property
    @abstractmethod
    def catalog(self):
        pass

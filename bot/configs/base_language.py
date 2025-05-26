from abc import ABC, abstractmethod


class Language(ABC):

    @property
    @abstractmethod
    def catalog(self):
        pass

    @property
    @abstractmethod
    def audio_uploaded(self):
        pass

    @property
    @abstractmethod
    def video_uploaded(self):
        pass

    @property
    @abstractmethod
    def photos_added(self):
        pass

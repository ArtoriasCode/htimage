from abc import ABC, abstractmethod


class Finder(ABC):

    @abstractmethod
    def find_browser(self):
        ...

    @abstractmethod
    def _find_mac(self):
        ...

    @abstractmethod
    def _find_win(self):
        ...

    @abstractmethod
    def _find_linux(self):
        ...
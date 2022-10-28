from abc import abstractmethod


class WaardenObject:
    @abstractmethod
    def __init__(self):
        self._parent = None

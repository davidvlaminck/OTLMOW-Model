from abc import abstractmethod


class WaardenObject:
    @abstractmethod
    def __init__(self):
        self._parent = None

    def __iter__(self):
        for k, v in vars(self).items():
            if k in ['_parent', '_geometry_types', '_valid_relations']:
                continue
            yield v

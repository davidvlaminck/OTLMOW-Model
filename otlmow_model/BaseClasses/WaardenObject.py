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

    def clear_value(self, attribute_name: str):
        if attribute_name is None:
            raise ValueError('attribute_name is None')
        attr = getattr(self, '_' + attribute_name, None)
        if attr is None:
            raise ValueError(f'attribute {attribute_name} does not exist')
        attr.set_waarde(None)
        attr.mark_to_be_cleared = True

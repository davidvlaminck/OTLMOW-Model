from abc import abstractmethod
from typing import Generator

from otlmow_model.OtlmowModel.Exceptions.CanNotClearAttributeError import CanNotClearAttributeError


class WaardenObject:
    @abstractmethod
    def __init__(self):
        self._parent = None

    def clear_value(self, attribute_name: str):
        if attribute_name is None:
            raise ValueError('attribute_name is None')
        attr = getattr(self, f'_{attribute_name}', None)
        if attr is None:
            raise ValueError(f'attribute {attribute_name} does not exist')
        if attr.readonly:
            raise ValueError(f'attribute {attribute_name} is readonly')
        if attr.objectUri in {
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator.identificator',
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator.toegekendDoor',
        }:
            raise CanNotClearAttributeError(f'attribute {attribute_name} can not be cleared')
        attr.set_waarde(None)
        attr.mark_to_be_cleared = True

    def __iter__(self) -> Generator:
        for k, v in vars(self).items():
            if k in ['_parent', '_geometry_types', '_valid_relations']:
                continue
            yield v

import warnings
from datetime import date, time, datetime
from typing import Union, Dict, List, Generator

from otlmow_model.BaseClasses.DateField import DateField
from otlmow_model.BaseClasses.DateTimeField import DateTimeField
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.BaseClasses.TimeField import TimeField
from otlmow_model.Exceptions.ClassDeprecationWarning import ClassDeprecationWarning


def create_dict_from_asset(asset, waarde_shortcut=False) -> dict:
    d = recursive_create_dict_from_asset(asset, waarde_shortcut=waarde_shortcut)
    if d is None:
        return {}
    return d


def recursive_create_dict_from_asset(asset=None, waarde_shortcut=False) -> Union[Dict, List[Dict]]:
    if isinstance(asset, list) and not isinstance(asset, dict):
        l = []
        for item in asset:
            dict_item = recursive_create_dict_from_asset(asset=item, waarde_shortcut=waarde_shortcut)
            if dict_item is not None:
                l.append(dict_item)
        if len(l) > 0:
            return l
    else:
        d = {}
        for k, v in vars(asset).items():
            if k in ['_parent', '_geometry_types', '_valid_relations']:
                continue
            if v.waarde is None or v.waarde == []:
                continue

            if v.field.waardeObject is not None:  # complex
                if waarde_shortcut and v.field.waarde_shortcut_applicable:
                    if isinstance(v.waarde, list):
                        dict_item = []
                        for item in v.waarde:
                            dict_item.append(item.waarde)
                        if len(dict_item) > 0:
                            d[k[1:]] = dict_item
                    else:
                        dict_item = v.waarde.waarde
                        if dict_item is not None:
                            d[k[1:]] = dict_item
                else:
                    dict_item = recursive_create_dict_from_asset(asset=v.waarde, waarde_shortcut=waarde_shortcut)
                    if dict_item is not None:
                        d[k[1:]] = dict_item
            else:
                if v.field == TimeField:
                    d[k[1:]] = time.strftime(v.waarde, "%H:%M:%S")
                elif v.field == DateField:
                    d[k[1:]] = date.strftime(v.waarde, "%Y-%m-%d")
                elif v.field == DateTimeField:
                    d[k[1:]] = datetime.strftime(v.waarde, "%Y-%m-%d %H:%M:%S")
                else:
                    d[k[1:]] = v.waarde

        if len(d.items()) > 0:
            return d


def clean_dict(d) -> Union[Dict, None]:
    """Recursively remove None values and empty dicts from input dict"""
    if d is None:
        return None
    for k in list(d):
        v = d[k]
        if isinstance(v, dict):
            clean_dict(v)
            if len(v.items()) == 0:
                del d[k]
        if v is None:
            del d[k]
    return d


def build_string_version(asset, indent: int = 4) -> str:
    if indent < 4:
        indent = 4
    d = create_dict_from_asset(asset)
    string_version = '\n'.join(_make_string_version_from_dict(d, level=1, indent=indent, prefix='    '))
    if string_version != '':
        string_version = '\n' + string_version
    return f'<{asset.__class__.__name__}> object\n{(" " * indent)}typeURI : {asset.typeURI}' + string_version


def _make_string_version_from_dict(d, level: int = 0, indent: int = 4, list_index: int = -1, prefix: str = '') -> List:
    lines = []

    if list_index != -1:
        index_string = f'[{list_index}]'
        index_string += ' ' * (indent - len(index_string))
        prefix += index_string

    for key in sorted(d):
        value = d[key]
        if isinstance(value, dict):
            lines.append(prefix + f'{key} :')
            lines.extend(_make_string_version_from_dict(value, level=level + 1, indent=indent, prefix=prefix + ' ' * indent * level))
        elif isinstance(value, list):
            lines.append(prefix + f'{key} :')
            for index, item in enumerate(value):
                if index == 10:
                    if len(value) == 11:
                        lines.append(prefix + '...(1 more item)')
                    else:
                        lines.append(prefix + f'...({len(value) - 10} more items)')
                    break
                if isinstance(item, dict):
                    lines.extend(_make_string_version_from_dict(item, level=level, indent=indent, list_index=index, prefix=prefix))
                else:
                    index_string = f'[{index}]'
                    index_string += ' ' * (indent - len(index_string))
                    lines.append(prefix + index_string + f'{item}')
        else:
            lines.append(prefix + f'{key} : {value}')
    return lines


class OTLObject:
    typeURI = ''
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        if hasattr(self, 'deprecated_version'):
            if self.deprecated_version is not None:
                try:
                    warnings.warn(message=f'{self.typeURI} is deprecated since version {self.deprecated_version}',
                                  category=ClassDeprecationWarning)
                except KeyError:
                    warnings.warn(
                        message=f'used a class ({self.__class__.__name__}) that is deprecated since version {self.deprecated_version}',
                        category=ClassDeprecationWarning)

    def create_dict_from_asset(self, waarde_shortcut=False) -> Dict:
        return create_dict_from_asset(asset=self, waarde_shortcut=waarde_shortcut)

    def fill_with_dummy_data(self):
        gen = self._generator_for_attributes()
        for attr in gen:
            if attr is not None:
                attr.fill_with_dummy_data()

    def __repr__(self):
        return build_string_version(asset=self)

    def _generator_for_attributes(self) -> Generator[OTLAttribuut, None, None]:
        for k, v in vars(self).items():
            if k in ['_parent', '_geometry_types', '_valid_relations']:
                continue
            yield v

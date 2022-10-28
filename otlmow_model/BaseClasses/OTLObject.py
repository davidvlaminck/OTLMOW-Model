import warnings
from datetime import date, time, datetime
from typing import Generator, Iterable, Union, Tuple

from otlmow_model.Helpers.DotnotationHelper import DotnotationHelper
from otlmow_model.BaseClasses.DateField import DateField
from otlmow_model.BaseClasses.DateTimeField import DateTimeField
from otlmow_model.BaseClasses.TimeField import TimeField


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
    string_version = '\n'.join(_make_string_version_from_dict(d, level=1, indent=indent))
    if string_version != '':
        string_version = '\n' + string_version
    return f'<{asset.__class__.__name__}> object\n{(" " * indent)}typeURI : {asset.typeURI}' + string_version


def _make_string_version_from_dict(d, level:int=0, indent:int=4) -> List:
    lines = []
    for key in sorted(d):
        value = d[key]
        if isinstance(value, dict):
            lines.append(' ' * indent * level + f'{key} :')
            lines.extend(_make_string_version_from_dict(value, level=level + 1, indent=indent))
        elif isinstance(value, list):
            lines.append(' ' * indent * level + f'{key} :')
            for index, item in enumerate(value):
                if index == 10:
                    if len(value) == 11:
                        lines.append(' ' * indent * level + '...(1 more item)')
                    else:
                        lines.append(' ' * indent * level + f'...({len(value) - 10} more items)')
                    break
                index_string = f'[{index}]'
                index_string += ' ' * (indent - len(index_string))
                lines.append(' ' * indent * level + index_string + f'{item}')

        else:
            lines.append(' ' * indent * level + f'{key} : {value}')
    return lines


class OTLObject:
    typeURI = ''

    def __init__(self):
        if hasattr(self, 'deprecated_version'):
            if self.deprecated_version is not None:
                try:
                    warnings.warn(message=f'{self.typeURI} is deprecated since version {self.deprecated_version}',
                                  category=DeprecationWarning)
                except KeyError:
                    warnings.warn(
                        message=f'used a class ({self.__class__.__name__}) that is deprecated since version {self.deprecated_version}',
                        category=DeprecationWarning)

    def create_dict_from_asset(self, waarde_shortcut=False) -> dict:
        return OTLObjectHelper.create_dict_from_asset(asset=self, waarde_shortcut=waarde_shortcut)

    def list_attributes_and_values_by_dotnotation(self, waarde_shortcut: bool = False,
                                                  separator: str = '.',
                                                  cardinality_indicator: str = '[]') -> Iterable[Tuple[str, object]]:
        for k, v in OTLObjectHelper.list_attributes_and_values_by_dotnotation(asset=self, waarde_shortcut=waarde_shortcut,
                                                                              separator=separator,
                                                                              cardinality_indicator=cardinality_indicator):
            yield k, v

    def __str__(self, use_dotnotation=False):
        return f'information about {self.__class__.__name__} {self.__hash__()}:\n' + \
               OTLObjectHelper.build_string_version(asset=self, indent=4, use_dotnotation=use_dotnotation)

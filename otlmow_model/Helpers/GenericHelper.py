from collections import defaultdict
from typing import Iterable

from otlmow_model.BaseClasses.OTLObject import OTLObject


def count_assets_by_type(objects: Iterable[OTLObject]) -> defaultdict:
    d = defaultdict(int)
    for i in objects:
        d[i.typeURI] += 1
    return d


def print_overview_assets(objects: Iterable[OTLObject]) -> None:
    for k, v in count_assets_by_type(objects).items():
        print(f'counting {str(v)} assets of type {k}')


def remove_duplicates_in_iterable_based_on_property(iterable: Iterable[OTLObject], property_name: str) -> []:
    d = {}
    for asset in iterable:
        item = asset
        last = property_name
        while '.' in last:
            first = last.split('.')[0]
            last = last.split('.', 1)[1]
            if hasattr(item, first):
                item = getattr(item, first)
                if isinstance(item, list):
                    raise NotImplementedError(
                        "can't use remove_duplicates_in_iterable_based_on_property() when the property value is a list")
        if hasattr(item, last):
            item_prop = getattr(item, last)
            if isinstance(item_prop, list):
                raise NotImplementedError(
                    "can't use remove_duplicates_in_iterable_based_on_property() when the property value is a list")
            item_prop_str = str(item_prop)
            if item_prop_str not in d:
                d[item_prop_str] = asset
    return list(d.values())


def get_shortened_uri(object_uri: str):
    if 'https://wegenenverkeer.data.vlaanderen.be/ns/' not in object_uri:
        raise ValueError(f'{object_uri} is not a valid uri to extract a namespace from')
    return object_uri.split('/ns/')[1]


def get_ns_and_name_from_uri(object_uri):
    short_uri = get_shortened_uri(object_uri)
    short_uri_array = short_uri.split('#')
    return short_uri_array[0], short_uri_array[1]


def get_class_directory_from_ns(ns):
    return 'Classes/' + get_titlecase_from_ns(ns)


def get_titlecase_from_ns(ns: str) -> str:
    if ns == 'abstracten':
        return 'Abstracten'
    elif ns == 'implementatieelement':
        return 'ImplementatieElement'
    elif ns == 'installatie':
        return 'Installatie'
    elif ns == 'levenscyclus':
        return 'Levenscyclus'
    elif ns == 'onderdeel':
        return 'Onderdeel'
    elif ns == 'proefenmeting':
        return 'ProefEnMeting'
    else:
        raise ValueError()

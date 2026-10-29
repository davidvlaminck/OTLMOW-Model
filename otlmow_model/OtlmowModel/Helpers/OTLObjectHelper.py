import base64
import warnings
from collections import defaultdict
from pathlib import Path
from typing import Iterable, List, Dict

from ..BaseClasses.OTLObject import OTLObject, create_dict_from_asset, dynamic_create_instance_from_ns_and_name
from ..Helpers.GenericHelper import validate_guid
from ..Helpers.generated_lists import get_hardcoded_relation_dict

_MISSING_PROPERTY = object()


def count_assets_by_type(objects: Iterable[OTLObject]) -> defaultdict:
    d = defaultdict(int)
    for i in objects:
        d[i.typeURI] += 1
    return d


def print_overview_assets(objects: Iterable[OTLObject]) -> None:
    for k, v in count_assets_by_type(objects).items():
        print(f'counting {str(v)} assets of type {k}')


# TODO move to converter (this is using a dotnotation)
def remove_duplicates_in_iterable_based_on_property(iterable: Iterable[OTLObject], property_name: str) -> []:
    d = {}
    for asset in iterable:
        item_prop = _property_value(asset, property_name)
        if item_prop is _MISSING_PROPERTY:
            continue
        d.setdefault(str(item_prop), asset)
    return list(d.values())


def _property_value(asset, property_name: str):
    """Return the value of a (dot notation) property of an asset.

    Returns ``_MISSING_PROPERTY`` when the asset does not have the property.
    """
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
    if not hasattr(item, last):
        return _MISSING_PROPERTY
    item_prop = getattr(item, last)
    if isinstance(item_prop, list):
        raise NotImplementedError(
            "can't use remove_duplicates_in_iterable_based_on_property() when the property value is a list")
    return item_prop


def compare_two_lists_of_objects_object_level(first_list: List[OTLObject], second_list: List[OTLObject],
                                              model_directory=None) -> List:
    """Given two lists of objects return the differences from the second list compared to the first list.
    Returns full objects from the second list when unmatched with the first list. """
    l1 = list(map(lambda x: create_dict_from_asset(x), first_list))
    l2 = list(map(lambda x: create_dict_from_asset(x), second_list))
    diff_list = [d for d in l2 if d not in l1]
    return list(map(lambda x: OTLObject.from_dict(x, model_directory), diff_list))


def custom_dict_diff(first_dict, second_dict):
    diff_dict = {}
    for k, v in second_dict.items():
        orig_v = first_dict.get(k)
        if orig_v is None:
            diff_dict[k] = v
            continue
        if orig_v != v:
            diff_dict.update(_diff_of_value(orig_v, v, k))
    return diff_dict


def _diff_of_value(orig_v, v, key):
    if isinstance(v, dict) and isinstance(orig_v, dict):
        result_dict = custom_dict_diff(orig_v, v)
        if result_dict == {}:
            return {}
        return {key: result_dict}
    return {key: v}


def compare_two_lists_of_objects_attribute_level(first_list: List[OTLObject], second_list: List[OTLObject],
                                                 model_directory: Path = None) -> List:
    """
    Given two lists of objects return the differences from the second list compared to the first list.
    Assumes both lists have objects with a unique assetId. Returns partial objects (on attribute level)
    from the second list when unmatched with the first list. """
    if model_directory is None:
        current_file_path = Path(__file__)
        model_directory = current_file_path.parent.parent.parent

    l1 = _dict_list_of(first_list)
    l2 = _dict_list_of(second_list)

    l1_dict_list = {dict_asset['assetId']['identificator']: dict_asset for dict_asset in l1}

    diff_list = []
    for d in l2:
        diff = _diff_for_asset(d, l1_dict_list)
        if diff is not None:
            diff_list.append(diff)

    return [OTLObject.from_dict(x, model_directory) for x in diff_list]


def _dict_list_of(objects: list[OTLObject]) -> list[dict]:
    dict_list = [create_dict_from_asset(x) for x in objects]
    verify_asset_id_is_unique_within_list(dict_list)
    return dict_list


def _diff_for_asset(asset_dict: dict, l1_dict_list: dict):
    """Return the difference of one asset, or None when there is none."""
    asset_id = asset_dict['assetId']['identificator']
    if asset_id not in l1_dict_list:
        return asset_dict
    orig_dict = l1_dict_list[asset_id]
    if orig_dict == asset_dict:
        return None
    diff_dict = custom_dict_diff(orig_dict, asset_dict)
    if diff_dict == {}:
        return None
    diff_dict['assetId'] = {'identificator': asset_id}
    diff_dict['typeURI'] = orig_dict['typeURI']
    return diff_dict


def verify_asset_id_is_unique_within_list(dict_list: List[Dict]) -> bool:
    d = {}
    for asset_dict in dict_list:
        asset_id = asset_dict['assetId']['identificator']
        if asset_id is None:
            raise ValueError(f'This list has a None value for assetId for at least one asset in this list:\n'
                             f'{asset_dict}')
        asset_d = d.get(asset_id)
        if asset_d is not None:
            raise ValueError(f"There are non-unique assetId's in assets in this list: {asset_id}")
        d[asset_dict['assetId']['identificator']] = asset_dict
    return True


def is_relation(otl_object: OTLObject, model_directory=Path(__file__).parent.parent.parent) -> bool:
    type_uri = otl_object.typeURI
    relation_dict = get_hardcoded_relation_dict(model_directory=model_directory)
    if type_uri in relation_dict:
        return True


def is_directional_relation(otl_object: OTLObject, model_directory=Path(__file__).parent.parent.parent) -> bool:
    type_uri = otl_object.typeURI
    relation_dict = get_hardcoded_relation_dict(model_directory=model_directory)
    relation_info = relation_dict.get(type_uri)
    if relation_info is None:
        return False
    return relation_dict[type_uri]['directional']


def is_aim_id(aim_id: str, model_directory: Path = None) -> bool:
    """
    Checks if the aim_id is valid. An aim_id is valid if it is a valid guid followed by a base64 encoded shortened uri.
    :param aim_id: the aim_id to be validated
    :type aim_id: str
    :param model_directory: directory where the model is located, defaults to otlmow_model's own model
    :type model_directory: Path
    :return: 'True' if the aim_id is valid, 'False' otherwise
    :rtype: bool
    """
    if not aim_id:
        return False
    if len(aim_id) < 38:
        return False

    uuid = aim_id[:36]
    short_uri_encoded = aim_id[37:]

    if not validate_guid(uuid):
        return False
    if not short_uri_encoded:
        return False

    short_uri = _decode_short_uri(short_uri_encoded)
    if short_uri is None:
        return False
    return _is_known_short_uri(short_uri, model_directory)


def _decode_short_uri(short_uri_encoded: str) -> str | None:
    """Decode the base64 encoded short uri, or None when it is not ascii."""
    if missing_padding := len(short_uri_encoded) % 4:
        short_uri_encoded += '=' * (4 - missing_padding)

    short_uri_bytes = base64.b64decode(short_uri_encoded)
    try:
        return short_uri_bytes.decode('ascii')
    except UnicodeDecodeError:
        return None


def _is_known_short_uri(short_uri: str, model_directory: Path) -> bool:
    try:
        if short_uri == 'purl:Agent':
            return True
        ns, name = short_uri.split('#')
        instance = dynamic_create_instance_from_ns_and_name(ns, name, model_directory=model_directory)
        return instance is not None
    except ModuleNotFoundError:
        warnings.warn('Could not import the module for the given aim_id, did you forget the model_directory?', category=ImportWarning)
        return False
    except ValueError:
        return False

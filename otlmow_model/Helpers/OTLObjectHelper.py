from collections import defaultdict
from typing import Iterable, List

from otlmow_model.BaseClasses.OTLObject import OTLObject, create_dict_from_asset


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


def compare_two_lists_of_objects_object_level(first_list: List[OTLObject], second_list: List[OTLObject], directory=None
                                              ) -> List:
    """Given two lists of objects return the differences from the second list compared to the first list.
    Returns full objects from the second list when unmatched with the first list. """
    l1 = list(map(lambda x: create_dict_from_asset(x), first_list))
    l2 = list(map(lambda x: create_dict_from_asset(x), second_list))
    diff_list = [d for d in l2 if d not in l1]
    return list(map(lambda x: OTLObject.from_dict(x, directory), diff_list))


def custom_dict_diff(first_dict, second_dict):
    diff_dict = {}
    for k, v in second_dict.items():
        orig_v = first_dict.get(k)
        if orig_v is None:
            diff_dict[k] = v
            continue
        if orig_v != v:
            if isinstance(v, dict) and isinstance(orig_v, dict):
                result_dict = custom_dict_diff(orig_v, v)
                if result_dict != {}:
                    diff_dict[k] = custom_dict_diff(orig_v, v)
            else:
                diff_dict[k] = v
    return diff_dict


def compare_two_lists_of_objects_attribute_level(first_list: List[OTLObject], second_list: List[OTLObject],
                                                 directory=None) -> List:
    """
    Given two lists of objects return the differences from the second list compared to the first list.
    Assumes both lists have objects with a unique assetId. Returns partial objects (on attribute level)
    from the second list when unmatched with the first list. """
    l1 = list(map(lambda x: create_dict_from_asset(x), first_list))
    verify_asset_id_is_unique_within_list(l1)

    l2 = list(map(lambda x: create_dict_from_asset(x), second_list))
    verify_asset_id_is_unique_within_list(l2)

    l1_dict_list = {dict_asset['assetId']['identificator']: dict_asset for dict_asset in l1}
    l1_dict_list_keys = list(l1_dict_list.keys())

    diff_list = []
    for d in l2:
        asset_id = d['assetId']['identificator']
        if asset_id not in l1_dict_list_keys:
            diff_list.append(d)
            continue
        orig_dict = l1_dict_list[asset_id]
        if orig_dict == d:
            continue
        diff_dict = custom_dict_diff(orig_dict, d)
        if diff_dict == {}:
            continue
        diff_dict['assetId'] = {'identificator': asset_id}
        diff_dict['typeURI'] = orig_dict['typeURI']
        diff_list.append(diff_dict)

    return list(map(lambda x: OTLObject.from_dict(x, directory), diff_list))


def verify_asset_id_is_unique_within_list(dict_list) -> bool:
    try:
        asset_ids_list_1 = list(map(lambda x: x['assetId']['identificator'], dict_list))
        asset_ids_set_1 = set(asset_ids_list_1)
        if None in asset_ids_set_1:
            raise ValueError('This list has a None value for assetId for at least one asset in this list')
        if len(asset_ids_list_1) != len(asset_ids_set_1):
            raise ValueError("There are non-unique assetId's in assets in this list")
        return True
    except Exception as ex:
        raise ex

import warnings
from datetime import date, datetime, time
from typing import Any, TYPE_CHECKING, Optional, Union

from ..Exceptions.NonStandardAttributeWarning import NonStandardAttributeWarning
from .DateTimeField import DateTimeField
from .OTLAttribuut import get_attribute_by_name, get_attribute_by_uri

if TYPE_CHECKING:
    from .OTLObject import OTLObject

SKIPPED_ATTRIBUTE_KEYS = {
    '_parent',
    '_valid_relations',
    '_geometry_types',
    '_is_union_waarden_object',
    '_is_waarden_object',
}

CLEARED_VALUE_MARKER = '88888888 <value_marked_to_be_cleared>'


class SerialisationOptions:
    """The options that steer the serialisation of an asset.

    Bundling them keeps the internal helpers below five arguments and makes the
    recursive calls pass a single object around.
    """

    def __init__(
        self,
        *,
        waarde_shortcut: bool = False,
        rdf: bool = False,
        cast_datetime: bool = False,
        allow_non_otl_conform_attributes: bool = True,
        warn_for_non_otl_conform_attributes: bool = True,
    ):
        self.waarde_shortcut = waarde_shortcut
        self.rdf = rdf
        self.cast_datetime = cast_datetime
        self.allow_non_otl_conform_attributes = allow_non_otl_conform_attributes
        self.warn_for_non_otl_conform_attributes = warn_for_non_otl_conform_attributes


def create_dict_from_asset(
    otl_object: 'OTLObject',
    waarde_shortcut=False,
    rdf: bool = False,
    cast_datetime: bool = False,
    allow_non_otl_conform_attributes: bool = True,
    warn_for_non_otl_conform_attributes: bool = True,
) -> dict[str, Any]:
    """Creates a dictionary from an OTLObject with key value pairs for attributes and their values. Saves the type of the object in typeURI (or @type for the RDF dict)

    :param otl_object: input object to be transformed
    :type: OTLObject
    :param waarde_shortcut: whether to use the waarde shortcut when processing the dictionary, defaults to False
    :type: bool
    :param rdf: whether to generate a dictionary where the keys are the URI's of the attributes rather than the names, defaults to False
    :type: bool
    :param cast_datetime: whether to convert dates, times and datetimes to strings, defaults to False
    :type: bool
    :param allow_non_otl_conform_attributes: whether to allow non OTL conform attributes. Raising ValueError if not, Defaults to True
    :type: bool
    :param warn_for_non_otl_conform_attributes: whether to generate warnings when using non OTL conform attributes. Defaults to True
    :type: bool

    :return: returns an dictionary where the values of the dictionary matches the given input object
    :rtype: dict"""
    options = SerialisationOptions(
        waarde_shortcut=waarde_shortcut,
        rdf=rdf,
        cast_datetime=cast_datetime,
        allow_non_otl_conform_attributes=allow_non_otl_conform_attributes,
        warn_for_non_otl_conform_attributes=warn_for_non_otl_conform_attributes,
    )

    if rdf:
        d = _recursive_create_rdf_dict_from_asset(otl_object, options)
    else:
        d = _recursive_create_dict_from_asset(otl_object, options)

    if d is None:
        d = {}
    if rdf:
        d['@type'] = otl_object.typeURI
    else:
        d['typeURI'] = otl_object.typeURI
    return d


def _recursive_create_dict_from_asset(asset, options: SerialisationOptions) -> Union[dict[str, Any], list[Any]]:
    if isinstance(asset, list) and not isinstance(asset, dict):
        return _create_dict_from_list(asset, options)
    return _create_dict_from_object(asset, options)


def _create_dict_from_list(asset: list, options: SerialisationOptions) -> list[Any]:
    items = []
    for item in asset:
        dict_item = _recursive_create_dict_from_asset(item, options)
        if dict_item is not None:
            items.append(dict_item)
    return items


def _create_dict_from_object(asset, options: SerialisationOptions) -> Optional[dict[str, Any]]:
    d = {}
    for attr_key, attr in vars(asset).items():
        if attr_key in SKIPPED_ATTRIBUTE_KEYS:
            continue
        d.update(_dict_entry_for_attribute(attr_key, attr, asset, options))
    if len(d.items()) > 0:
        return d
    return None


def _dict_entry_for_attribute(attr_key: str, attr, asset, options: SerialisationOptions) -> dict[str, Any]:
    if _is_otl_attribute(attr):
        return _dict_entry_for_otl_attribute(attr, options)
    return _non_standard_attribute_entry(attr_key, attr, asset, options)


def _dict_entry_for_otl_attribute(attr, options: SerialisationOptions) -> dict[str, Any]:
    if not attr.mark_to_be_cleared:
        if attr.waarde is None:
            return {}
        if attr.waarde == []:
            return {attr.naam: []}
    if attr.field.waardeObject is not None:
        return _dict_entry_for_complex_attribute(attr, options)
    return _dict_entry_for_simple_attribute(attr, options)


def _dict_entry_for_complex_attribute(attr, options: SerialisationOptions) -> dict[str, Any]:
    if options.waarde_shortcut and attr.field.waarde_shortcut_applicable:
        dict_item = _shortcut_value(attr)
    else:
        dict_item = _recursive_create_dict_from_asset(attr.waarde, options)
    if dict_item is None:
        return {}
    return {attr.naam: dict_item}


def _dict_entry_for_simple_attribute(attr, options: SerialisationOptions) -> dict[str, Any]:
    if attr.mark_to_be_cleared:
        return {attr.naam: attr.field.clearing_value}
    if options.cast_datetime and attr.field.is_otl_field:
        return {attr.naam: _cast_datetime_value(attr)}
    return {attr.naam: attr.waarde}


def _cast_datetime_value(attr):
    native_type = attr.field.native_type
    if native_type == time:
        return _format_time_value(attr.waarde)
    elif native_type == date:
        return _format_date_value(attr.waarde)
    elif native_type == datetime:
        return _format_datetime_value(attr.waarde)
    return attr.waarde


def _format_time_value(waarde):
    if isinstance(waarde, list):
        return [time.strftime(list_item, '%H:%M:%S') for list_item in waarde]
    return time.strftime(waarde, '%H:%M:%S')


def _format_date_value(waarde):
    if isinstance(waarde, list):
        return [date.strftime(list_item, '%Y-%m-%d') for list_item in waarde]
    return date.strftime(waarde, '%Y-%m-%d')


def _format_datetime_value(waarde):
    if isinstance(waarde, list):
        return [DateTimeField.value_default(list_item) for list_item in waarde]
    return DateTimeField.value_default(waarde)


def _shortcut_value(attr):
    if isinstance(attr.waarde, list):
        return _shortcut_list_value(attr.waarde)
    return _shortcut_single_value(attr.waarde)


def _shortcut_list_value(waarde) -> Optional[list[Any]]:
    item_list = [_shortcut_item_value(item) for item in waarde]
    return item_list if len(item_list) > 0 else None


def _shortcut_item_value(item):
    if item._waarde.mark_to_be_cleared:
        return item._waarde.field.clearing_value
    return item._waarde.waarde


def _shortcut_single_value(waarde):
    if waarde._waarde.mark_to_be_cleared:
        return waarde._waarde.field.clearing_value
    return waarde.waarde


def _is_otl_attribute(attr) -> bool:
    return hasattr(attr, 'is_otl_attribute') and attr.is_otl_attribute


def _non_standard_attribute_entry(attr_key: str, attr, asset, options: SerialisationOptions) -> dict[str, Any]:
    if attr_key.startswith('_'):
        raise ValueError(
            f'{attr_key} is a non standardized attribute of {asset.__class__.__name__}. '
            f'While this is supported, the key can not start with "_".'
        )
    if not options.allow_non_otl_conform_attributes:
        raise ValueError(
            f'{attr_key} is a non standardized attribute of {asset.__class__.__name__}. '
            f'If you want to allow this, set allow_non_otl_conform_attributes to True.'
        )
    if options.warn_for_non_otl_conform_attributes:
        warnings.warn(
            message=f'{attr_key} is a non standardized attribute of {asset.__class__.__name__}. '
            f'The attribute will be added on the instance.',
            stacklevel=2,
            category=NonStandardAttributeWarning,
        )
    return {attr_key: attr}


def _recursive_create_rdf_dict_from_asset(asset, options: SerialisationOptions) -> Union[dict[str, Any], list[Any]]:
    if isinstance(asset, list) and not isinstance(asset, dict):
        return _create_rdf_dict_from_list(asset, options)
    return _create_rdf_dict_from_object(asset, options)


def _create_rdf_dict_from_list(asset: list, options: SerialisationOptions) -> Optional[list[Any]]:
    items = []
    for item in asset:
        dict_item = _recursive_create_rdf_dict_from_asset(item, options)
        if dict_item is not None:
            items.append(dict_item)
    return items if len(items) > 0 else None


def _create_rdf_dict_from_object(asset, options: SerialisationOptions) -> Optional[dict[str, Any]]:
    d = {}
    for attr_key, attr in vars(asset).items():
        if attr_key in SKIPPED_ATTRIBUTE_KEYS:
            continue
        d.update(_rdf_entry_for_attribute(attr_key, attr, asset, options))
    if len(d.items()) > 0:
        return d
    return None


def _rdf_entry_for_attribute(attr_key: str, attr, asset, options: SerialisationOptions) -> dict[str, Any]:
    if _is_otl_attribute(attr):
        return _rdf_entry_for_otl_attribute(attr, options)
    return _non_standard_attribute_entry(attr_key, attr, asset, options)


def _rdf_entry_for_otl_attribute(attr, options: SerialisationOptions) -> dict[str, Any]:
    if not attr.mark_to_be_cleared:
        if attr.waarde is None:
            return {}
        if attr.waarde == []:
            return {attr.objectUri: []}
    if attr.field.waardeObject is not None:
        return _rdf_entry_for_complex_attribute(attr, options)
    return _rdf_entry_for_simple_attribute(attr, options)


def _rdf_entry_for_complex_attribute(attr, options: SerialisationOptions) -> dict[str, Any]:
    if options.waarde_shortcut and attr.field.waarde_shortcut_applicable:
        dict_item = _shortcut_value(attr)
    else:
        _propagate_clearing_to_children(attr)
        dict_item = _recursive_create_rdf_dict_from_asset(attr.waarde, options)
    if dict_item is None:
        return {}
    return {attr.objectUri: dict_item}


def _propagate_clearing_to_children(attr) -> None:
    if attr.mark_to_be_cleared:
        for a in attr.waarde:
            a.mark_to_be_cleared = True


def _rdf_entry_for_simple_attribute(attr, options: SerialisationOptions) -> dict[str, Any]:
    if attr.mark_to_be_cleared:
        return {attr.objectUri: attr.field.clearing_value}
    if options.cast_datetime and attr.field.is_otl_field and attr.field.native_type == datetime:
        return {attr.objectUri: _format_rdf_datetime_value(attr.waarde)}
    if _has_options(attr.field):
        return {attr.objectUri: _options_value(attr)}
    return {attr.objectUri: attr.waarde}


def _format_rdf_datetime_value(waarde):
    if isinstance(waarde, list):
        return [datetime.strftime(list_item, '%Y-%m-%d %H:%M:%S') for list_item in waarde]
    return datetime.strftime(waarde, '%Y-%m-%d %H:%M:%S')


def _has_options(field) -> bool:
    return hasattr(field, 'options') and field.options is not None


def _options_value(attr):
    if isinstance(attr.waarde, list):
        if attr.waarde == [None]:
            return []
        return [attr.field.options[list_item].objectUri for list_item in attr.waarde]
    return attr.field.options[attr.waarde].objectUri


def clean_dict(d) -> Optional[dict[str, Any]]:
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
    indent = max(indent, 4)
    d = create_dict_from_asset(asset, warn_for_non_otl_conform_attributes=False)
    string_version = '\n'.join(_make_string_version_from_dict(d, level=1, indent=indent, prefix='    '))
    if string_version != '':
        string_version = '\n' + string_version
    return f'<{asset.__class__.__name__}> object\n{" " * indent}typeURI : {asset.typeURI}{string_version}'


def _make_string_version_from_dict(
    d, level: int = 0, indent: int = 4, list_index: int = -1, prefix: str = ''
) -> list[Any]:
    lines = []

    if list_index != -1:
        prefix = _index_prefix(prefix, list_index, indent)

    for key in sorted(d):
        if key == 'typeURI':
            continue
        value = _mark_cleared_value(d[key])
        if isinstance(value, dict):
            lines.append(f'{prefix}{key} :')
            lines.extend(
                _make_string_version_from_dict(value, level=level + 1, indent=indent, prefix=prefix + ' ' * indent)
            )
        elif isinstance(value, list):
            lines.append(f'{prefix}{key} :')
            lines.extend(_list_lines(value, level=level, indent=indent, prefix=prefix))
        else:
            lines.append(f'{prefix}{key} : {value}')
    return lines


def _index_prefix(prefix: str, list_index: int, indent: int) -> str:
    index_string = f'[{list_index}]'
    index_string += ' ' * (indent - len(index_string))
    return prefix + index_string


def _mark_cleared_value(value):
    if isinstance(value, float) and value == 88888888.0:
        return CLEARED_VALUE_MARKER
    if str(value) == '88888888':
        return CLEARED_VALUE_MARKER
    return value


def _list_lines(value: list, level: int, indent: int, prefix: str) -> list[Any]:
    lines = []
    for index, item in enumerate(value):
        if index == 10:
            lines.append(_truncation_line(value, prefix))
            break
        if isinstance(item, dict):
            lines.extend(
                _make_string_version_from_dict(item, level=level, indent=indent, list_index=index, prefix=prefix)
            )
        else:
            lines.append(prefix + _index_prefix('', index, indent) + f'{item}')
    return lines


def _truncation_line(value: list, prefix: str) -> str:
    if len(value) == 11:
        return f'{prefix}...(1 more item)'
    return f'{prefix}...({len(value) - 10} more items)'


# dict encoder = asset object to dict
# dict decoder = dict to asset object


def set_value_by_dictitem(
    instance_or_attribute,
    key: str,
    value,
    waarde_shortcut: bool = False,
    rdf: bool = False,
    cast_datetime: bool = False,
    allow_non_otl_conform_attributes: bool = True,
    warn_for_non_otl_conform_attributes: bool = True,
):
    _validate_set_value_arguments(instance_or_attribute, key)

    options = SerialisationOptions(
        waarde_shortcut=waarde_shortcut,
        rdf=rdf,
        cast_datetime=cast_datetime,
        allow_non_otl_conform_attributes=allow_non_otl_conform_attributes,
        warn_for_non_otl_conform_attributes=warn_for_non_otl_conform_attributes,
    )

    attribute_to_set = _find_attribute(instance_or_attribute, key, rdf)
    if attribute_to_set is None:
        _set_non_standard_attribute(instance_or_attribute, key, value, options)
        return

    if _is_clearing_value(value, attribute_to_set):
        attribute_to_set.clear_value()
        return

    if attribute_to_set.field.waardeObject is not None:  # complex / union / KwantWrd / dte
        _set_complex_value(attribute_to_set, value, options)
    else:
        _set_simple_value(attribute_to_set, value, options)


def _validate_set_value_arguments(instance_or_attribute, key: str) -> None:
    if instance_or_attribute is None:
        raise ValueError('instance_or_attribute cannot be None')
    if key is None or key == '':
        raise ValueError('key cannot be empty')


def _find_attribute(instance_or_attribute, key: str, rdf: bool):
    if rdf:
        return get_attribute_by_uri(instance_or_attribute, key)
    return get_attribute_by_name(instance_or_attribute, key)


def _set_non_standard_attribute(instance_or_attribute, key: str, value, options: SerialisationOptions) -> None:
    if not options.allow_non_otl_conform_attributes:
        raise ValueError(
            f'Attribute with name "{key}" can not be found on the given instance or attribute. '
            'Assuming this is a non standardized attribute. If you want to allow this, set '
            'allow_non_otl_conform_attributes to True.'
        )
    if options.warn_for_non_otl_conform_attributes:
        warnings.warn(
            message=f'Attribute with name "{key}" can not be found on the given instance or attribute. '
            'Assuming this is a non standardized attribute. Setting the attribute with setattr',
            category=NonStandardAttributeWarning,
        )
    setattr(instance_or_attribute, key, value)


def _is_clearing_value(value, attribute_to_set) -> bool:
    if value == attribute_to_set.field.clearing_value:
        return True
    return value == [attribute_to_set.field.clearing_value]


def _set_complex_value(attribute_to_set, value, options: SerialisationOptions) -> None:
    if isinstance(value, list):
        _set_complex_list_value(attribute_to_set, value, options)
    elif isinstance(value, dict):  # only complex / union possible
        _set_complex_dict_value(attribute_to_set, value, options)
    else:  # must be a dte / kwantWrd
        _set_complex_single_value(attribute_to_set, value, options)


def _set_complex_list_value(attribute_to_set, value, options: SerialisationOptions) -> None:
    for index, list_item in enumerate(value):
        if attribute_to_set.waarde is None or len(attribute_to_set.waarde) <= index:
            attribute_to_set.add_empty_value()

        if attribute_to_set.field.waarde_shortcut_applicable and options.waarde_shortcut:  # dte / kwantWrd
            _set_shortcut_item_value(attribute_to_set, index, list_item)
        else:  # complex / union
            for k, v in list_item.items():
                set_value_by_dictitem(
                    attribute_to_set.waarde[index],
                    k,
                    v,
                    waarde_shortcut=options.waarde_shortcut,
                    rdf=options.rdf,
                    cast_datetime=options.cast_datetime,
                    allow_non_otl_conform_attributes=options.allow_non_otl_conform_attributes,
                    warn_for_non_otl_conform_attributes=options.warn_for_non_otl_conform_attributes,
                )


def _set_shortcut_item_value(attribute_to_set, index: int, list_item) -> None:
    if list_item == attribute_to_set.waarde[index]._waarde.field.clearing_value:
        attribute_to_set.waarde[index]._waarde.clear_value()
        return
    attribute_to_set.waarde[index]._waarde.set_waarde(list_item)


def _set_complex_dict_value(attribute_to_set, value, options: SerialisationOptions) -> None:
    if attribute_to_set.waarde is None:
        attribute_to_set.add_empty_value()

    target = attribute_to_set.waarde[0] if attribute_to_set.kardinaliteit_max != '1' else attribute_to_set.waarde

    for k, v in value.items():
        set_value_by_dictitem(
            target,
            k,
            v,
            waarde_shortcut=options.waarde_shortcut,
            rdf=options.rdf,
            cast_datetime=options.cast_datetime,
            allow_non_otl_conform_attributes=options.allow_non_otl_conform_attributes,
            warn_for_non_otl_conform_attributes=options.warn_for_non_otl_conform_attributes,
        )


def _set_complex_single_value(attribute_to_set, value, options: SerialisationOptions) -> None:
    if attribute_to_set.waarde is None:
        attribute_to_set.add_empty_value()

    value = _cast_datetime_if_needed(attribute_to_set.waarde._waarde.field, value, options.cast_datetime)
    attribute_to_set.waarde._waarde.set_waarde(value)


def _set_simple_value(attribute_to_set, value, options: SerialisationOptions) -> None:
    value = _cast_datetime_if_needed(attribute_to_set.field, value, options.cast_datetime)
    attribute_to_set.set_waarde(value)


def _cast_datetime_if_needed(field, value, cast_datetime: bool):
    if cast_datetime and field.is_otl_field and field.native_type in [date, datetime, time]:
        return field.convert_to_correct_type(value=value, log_warnings=False)
    return value

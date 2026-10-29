from typing import Union

from .OTLObject import OTLObject, OTLAttribuut


def meta_info(obj: Union[OTLObject, OTLAttribuut], attribute: str = '') -> str:
    """Returns metadata of the object or attribute"""
    if attribute != '':
        return _meta_info_of_attribute(obj, attribute)
    if hasattr(obj, 'return_is_otl_object') and obj.return_is_otl_object():
        return _meta_info_otl_object(obj)
    if hasattr(obj, 'is_otl_attribute') and obj.is_otl_attribute:
        return _meta_info_attribute(obj)
    return None


def _meta_info_of_attribute(obj: Union[OTLObject, OTLAttribuut], attribute: str) -> str:
    if '.' in attribute:
        return _meta_info_of_nested_attribute(obj, attribute)
    if hasattr(obj, '_' + attribute):
        return meta_info(getattr(obj, '_' + attribute))
    raise ValueError(f"'{attribute}' does not exist, please check the spelling")


def _meta_info_of_nested_attribute(obj: Union[OTLObject, OTLAttribuut], attribute: str) -> str:
    first = attribute.split('.')[0]
    rest = attribute.split('.', 1)[1]
    if hasattr(obj, '_' + first):
        attr = getattr(obj, '_' + first)
        return meta_info(attr.field.waardeObject(), rest)
    raise ValueError(f"'{attribute}' does not exist, please check the spelling")


def _meta_info_otl_object(otl_object: OTLObject) -> str:
    object_string = (
        f'Showing metadata of {otl_object.__class__.__name__}:\n'
        f'typeURI: {getattr(otl_object, "typeURI", "")}\n'
        f'definition: {otl_object.__doc__}\n'
    )

    if hasattr(otl_object, 'deprecated_version') and getattr(otl_object, 'deprecated_version', None):
        object_string += f'deprecated since {otl_object.deprecated_version}\n'

    object_string += 'attributes:\n'

    for attr in otl_object:
        attr_line = f'    {getattr(attr, "naam", "")} (type: {getattr(getattr(attr, "field", None), "naam", "")})'
        if hasattr(attr, 'deprecated_version') and getattr(attr, 'deprecated_version', ''):
            attr_line += f' <deprecated since {attr.deprecated_version}>'
        object_string += attr_line + '\n'

    return object_string[:-1]


def _meta_info_attribute(attribute: OTLAttribuut) -> str:
    object_string = (
        f'Showing metadata of {getattr(attribute, "naam", "")}:\n'
        f'typeURI: {getattr(attribute, "objectUri", "")}\n'
        f'definition: {getattr(attribute, "definition", "")}\n'
    )

    if hasattr(attribute, 'deprecated_version') and attribute.deprecated_version != '':
        object_string += f'deprecated since {attribute.deprecated_version}\n'

    field = _field_of(attribute)
    object_string += _valid_values_of(field)
    object_string += _attributes_of(field)

    return object_string[:-1]


def _field_of(attribute: OTLAttribuut):
    field = getattr(attribute, 'field', None)
    if callable(field):
        field = field()
    return field


def _valid_values_of(field) -> str:
    if not hasattr(field, 'options'):
        return ''
    object_string = 'valid values:\n'
    options = getattr(field, 'options', {})
    valid_options = [(k, v) for k, v in options.items() if getattr(v, 'status', '') != 'verwijderd']
    for i, (k, v) in enumerate(valid_options):
        object_string += f'    {_option_line(k, v)}\n'
        if i >= 9:
            return object_string + _full_list_hint(field)
    return object_string


def _option_line(key, option) -> str:
    status = getattr(option, 'status', '')
    status_display = {'uitgebruik': '(waarde uit gebruik!)'}.get(status, '')
    status_note = f' {status_display}' if status_display else ''
    return f'{key}{status_note}'


def _full_list_hint(field) -> str:
    naam = getattr(field, 'naam', '')
    codelist = getattr(field, 'codelist', '')
    return f'    ...\nFor the full list, review the class {naam} or go to {codelist}\n'


def _attributes_of(field) -> str:
    waardeObject = getattr(field, 'waardeObject', None)
    if waardeObject is None:
        return ''
    object_string = 'attributes:\n'
    for attr in waardeObject():
        object_string += _attribute_line(attr) + '\n'
    return object_string


def _attribute_line(attr) -> str:
    attr_line = f'    {getattr(attr, "naam", "")} (type: {getattr(getattr(attr, "field", None), "naam", "")}'
    kard_min = getattr(attr, 'kardinaliteit_min', '1')
    kard_max = getattr(attr, 'kardinaliteit_max', '1')
    if kard_min != '1' or kard_max != '1':
        attr_line += f', cardinality: {kard_min}-{kard_max}'
    attr_line += ')'
    if hasattr(attr, 'deprecated_version') and getattr(attr, 'deprecated_version', ''):
        attr_line += f' <deprecated since {attr.deprecated_version}>'
    return attr_line

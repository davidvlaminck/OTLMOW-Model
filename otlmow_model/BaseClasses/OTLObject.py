import math
import random
import warnings
from datetime import date, time
from datetime import datetime
from typing import Union, Dict, List, Generator

from otlmow_model.BaseClasses.DateField import DateField
from otlmow_model.BaseClasses.DateTimeField import DateTimeField
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.OTLField import OTLField
from otlmow_model.BaseClasses.TimeField import TimeField
from otlmow_model.BaseClasses.URIField import URIField
from otlmow_model.BaseClasses.UnionTypeField import UnionTypeField
from otlmow_model.BaseClasses.UnionWaarden import UnionWaarden
from otlmow_model.Exceptions.AttributeDeprecationWarning import AttributeDeprecationWarning
from otlmow_model.Exceptions.ClassDeprecationWarning import ClassDeprecationWarning
from otlmow_model.Exceptions.MethodNotApplicableError import MethodNotApplicableError
from otlmow_model.Helpers.AssetCreator import dynamic_create_instance_from_uri


class OTLAttribuut:
    def __init__(self, naam='', label='', objectUri='', definition='', constraints='', usagenote='',
                 deprecated_version='', kardinaliteit_min='1', kardinaliteit_max='1', field=OTLField, readonly=False,
                 readonlyValue=None, owner=None):
        super().__init__()
        self.naam = naam
        self.label = label
        self.objectUri = objectUri
        self.definition = definition
        self.constraints = constraints
        self.usagenote = usagenote
        self.deprecated_version = deprecated_version
        self.readonly = readonly
        self.kardinaliteit_min = kardinaliteit_min
        self.kardinaliteit_max = kardinaliteit_max
        self._dotnotation = ''
        self.owner = owner
        self.readonlyValue = None
        self.waarde = None
        self.field = field

        if self.field.waardeObject:
            def add_empty_value():
                prev_value = self.waarde
                if kardinaliteit_max == '1':
                    if prev_value is None:
                        new_value_object = self.field.waardeObject()
                        new_value_object._parent = self
                        self.set_waarde(new_value_object)
                    else:
                        raise RuntimeError(
                            "This attribute does not have a cardinality other than 1, therefore you can only call this method once per instance")
                else:
                    if prev_value is None:
                        prev_value = []
                    new_value_object = self.field.waardeObject()
                    new_value_object._parent = self
                    prev_value.append(new_value_object)
                    self.set_waarde(prev_value)

            self.add_empty_value = add_empty_value

        if kardinaliteit_max != '1':
            def add_value(value):
                l = self.waarde
                if self.waarde is None:
                    l = []
                l.append(value)
                self.set_waarde(l)

            self.add_value = add_value

        if readonly:
            self.__dict__["waarde"] = readonlyValue

    def add_value(self, value):
        raise MethodNotApplicableError(
            "This attribute does not have a cardinality other than 1 so simply assign your value directly instead of "
            "using this method")

    def get_waarde(self):
        if self.field.waardeObject and self.waarde is None:
            self.add_empty_value()
        return self.waarde

    def add_empty_value(self):
        """Helper method for datatypes UnionType, ComplexType, KwantWrd and Dte to add the underlying waarde object"""
        if not self.field.waardeObject:
            raise MethodNotApplicableError(
                "In order to use this method this object must be one of these types: UnionType, ComplexType, KwantWrd, "
                "Dte")

    def default(self):
        if self.waarde is not dict and isinstance(self.waarde, list):
            value_list = []
            for item in self.waarde:
                if self.field.waardeObject is not None:
                    waarde_dict = vars(item)
                    value_dict = {}
                    for k, v in waarde_dict.items():
                        if v.default() is not None:
                            value_dict[k[1:]] = v.default()
                    if len(value_dict) != 0:
                        value_list.append(value_dict)
                else:
                    value_list.append(item)
            return value_list
        if self.field.waardeObject is not None:
            if self.field.waarde_shortcut_applicable:
                waarde_dict = vars(self.waarde)
                value_dict = {}
                for k, v in waarde_dict.items():
                    if v.default() is not None:
                        value_dict[k[1:]] = v.default()
                if len(value_dict) == 0:
                    return None
                return value_dict
            else:
                if self.waarde.waarde is not None:
                    if hasattr(self.waarde.waarde, 'default'):
                        return self.waarde.waarde.default()
                    else:
                        return self.waarde.waarde
                return None
        else:
            if isinstance(self.waarde, datetime):
                if self.waarde.hour == 0 and self.waarde.minute == 0 and self.waarde.second == 0:
                    return self.waarde.strftime("%Y-%m-%d")
                else:
                    return self.waarde.strftime("%Y-%m-%d %H:%M:%S")
            else:
                if hasattr(self.waarde, 'default'):
                    return self.waarde.default()
                else:
                    return self.waarde

    def _perform_cardinality_check(self, owner, value, kardinaliteit_max):
        kardinaliteit_min = int(self.kardinaliteit_min)
        if not isinstance(value, list):
            raise TypeError(f'expecting a list in {owner.__class__.__name__}.{self.naam}')
        elif isinstance(value, list) and isinstance(value, set):
            raise TypeError(f'expecting a non set type of list in {owner.__class__.__name__}.{self.naam}')
        elif 0 < len(value) < kardinaliteit_min:
            raise ValueError(
                f'expecting at least {kardinaliteit_min} element(s) in {owner.__class__.__name__}.{self.naam}')
        elif len(value) > kardinaliteit_max:
            raise ValueError(
                f'expecting at most {kardinaliteit_max} element(s) in {owner.__class__.__name__}.{self.naam}')

    def set_waarde(self, value, owner=None):
        self._perform_deprecation_check(self)

        if value is None:
            self.waarde = None
            return

        if self.kardinaliteit_max != '1':
            if self.kardinaliteit_max == '*':
                kardinaliteit_max = math.inf
            else:
                kardinaliteit_max = int(self.kardinaliteit_max)
            self._perform_cardinality_check(owner, value, kardinaliteit_max)
            converted_values = []
            for el_value in value:
                try:
                    converted_value = self.field.convert_to_correct_type(el_value)
                    if issubclass(self.field, KeuzelijstField):
                        converted_value = self.field.convert_to_invulwaarde(converted_value, self.field)

                    field_validated = self.field.validate(converted_value, self)
                    if not field_validated:
                        raise ValueError(
                            f'invalid value in list for {owner.__class__.__name__}.{self.naam}: {el_value} is not '
                            f'valid, must be valid for {self.field.naam}')
                    converted_values.append(converted_value)
                except TypeError as error:
                    raise ValueError(
                        f'invalid value in list for {owner.__class__.__name__}.{self.naam}: {el_value} is not valid, '
                        f'must be valid for {self.field.naam}\n' + str(
                            error))
            self.waarde = converted_values
        else:
            if self.field.waardeObject is not None and isinstance(value, self.field.waardeObject):
                self.waarde = value
            else:
                converted_value = self.field.convert_to_correct_type(value)
                if issubclass(self.field, KeuzelijstField):
                    converted_value = self.field.convert_to_invulwaarde(converted_value, self.field)
                if self.field.validate(value=converted_value, attribuut=self):
                    self.waarde = converted_value
                else:
                    raise ValueError(
                        f'Could not assign the best effort converted value to {owner.__class__.__name__}.{self.naam}')

        # check if kwant Wrd inside a union type, if so, call clear_props
        if owner is not None and value is not None and hasattr(owner, 'field') and owner.field.waardeObject is not None:
            if owner.field.waarde_shortcut_applicable and not isinstance(
                    owner.field, UnionTypeField) and owner.owner is not None and isinstance(owner.owner, UnionWaarden):
                owner.owner.clear_other_props('_' + owner.naam)

    @staticmethod
    def _perform_deprecation_check(owner):
        if owner is not None:
            if owner.naam == 'waarde':
                owner = owner.owner._parent

            if hasattr(owner, 'deprecated_version'):
                if owner.deprecated_version != '':
                    if hasattr(owner, 'objectUri'):
                        warnings.warn(
                            message=f'{owner.objectUri} is deprecated since version {owner.deprecated_version}',
                            category=AttributeDeprecationWarning)
                    elif hasattr(owner, 'typeURI'):
                        warnings.warn(message=f'{owner.typeURI} is deprecated since version {owner.deprecated_version}',
                                      category=AttributeDeprecationWarning)
                    else:
                        warnings.warn(
                            message=f'used a class that is deprecated since version {owner.deprecated_version}',
                            category=AttributeDeprecationWarning)

    def __str__(self):
        s = (f'information about {self.naam}:\n'
             f'naam: {self.naam}\n'
             f'uri: {self.objectUri}\n'
             f'definition: {self.definition}\n'
             f'label: {self.label}\n'
             f'usagenote: {self.usagenote}\n'
             f'constraints: {self.constraints}\n'
             f'readonly: {self.readonly}\n'
             f'kardinaliteit_min: {self.kardinaliteit_min}\n'
             f'kardinaliteit_max: {self.kardinaliteit_max}\n'
             f'deprecated_version: {self.deprecated_version}\n')
        return s

    def fill_with_dummy_data(self):
        if self.readonly:
            return

        if self.field.waardeObject is None:
            if self.naam == 'geometry':
                first_geom_type = self.owner._geometry_types[0]
                if first_geom_type == 'POINT Z':
                    self.set_waarde('POINT Z (200000 200000 0)')
                elif first_geom_type == 'LINESTRING Z':
                    self.set_waarde('LINESTRING Z (200000 200000 0, 200001 200001 1)')
                elif first_geom_type == 'POLYGON Z':
                    self.set_waarde('POLYGON Z ((200000 200000 0, 200001 200001 1, 200002 200002 2))')
                return
            else:
                data = self.field.create_dummy_data()
                if self.kardinaliteit_max != '1':
                    self.set_waarde([data])
                else:
                    self.set_waarde(data)
                return

        new_value_object = self.field.waardeObject()
        new_value_object._parent = self

        if isinstance(new_value_object, UnionWaarden):
            selected_attr = random.choice(list(new_value_object))
            selected_attr.fill_with_dummy_data()
        else:
            for a in new_value_object:
                a.fill_with_dummy_data()

        if self.kardinaliteit_max != '1':
            self.set_waarde([new_value_object])
        else:
            self.set_waarde(new_value_object)


class OTLObject(object):
    typeURI: str = None
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __setattr__(self, name, value):
        if name != 'typeURI':
            super(OTLObject, self).__setattr__(name, value)
        else:
            if hasattr(self, 'typeURI') and (value is not None or self.typeURI is not None):
                raise ValueError("The typeURI is an OSLOAttribute that indicates the class of the instance. "
                                 "Within a class this value is predefined and cannot be changed.")
            else:
                if URIField.validate(value, OTLAttribuut(naam='typeURI')):
                    self.__dict__['value'] = value
                else:
                    raise ValueError(f'{value} is not a valid value for typeURI.')

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

    def create_dict_from_asset(self, waarde_shortcut: bool = False, rdf: bool = False) -> Dict:
        """Converts this asset into a dictionary representation"""
        return create_dict_from_asset(otl_object=self, waarde_shortcut=waarde_shortcut, rdf=rdf)

    def fill_with_dummy_data(self):
        for attr in self:
            if attr is not None:
                attr.fill_with_dummy_data()

    def __repr__(self):
        return build_string_version(asset=self)

    def __iter__(self) -> Generator[OTLAttribuut, None, None]:
        yield from sorted(filter(lambda v: isinstance(v, OTLAttribuut), (vars(self).values())), key=lambda x: x.naam)

    def __eq__(self, other):
        return create_dict_from_asset(self) == create_dict_from_asset(other)

    @classmethod
    def from_dict(cls, input_dict: Dict, directory: str = 'otlmow_model.Classes',
                  waarde_shortcut: bool = False) -> object:
        """Alternative constructor. Allows the instantiation of an object using a dictionary. Either start from the
        appropriate class or add a typeURI entry to the dictionary to get an instance of that type.

        :param input_dict: input dictionary, containing key value pairs for the attributes of the instance
        :type: dict
        :param directory: directory where the class modules are located, defaults to otlmow_model.Classes
        :type: str
        :param waarde_shortcut: whether to use the waarde shortcut when processing the dictionary, defaults to False
        :type: bool
        :return: returns an instance where the values of the attributes matches the given dictionary
        :rtype: OTLObject"""
        if 'typeURI' in input_dict:
            type_uri = input_dict['typeURI']
        else:
            type_uri = cls.typeURI

        if type_uri is None:
            raise ValueError(
                'typeURI is None. Add a valid typeURI to the input dictionary or change the class you are using "from_dict" from.')

        try:
            o = dynamic_create_instance_from_uri(type_uri, directory=directory)
        except TypeError:
            raise ValueError(
                'typeURI is invalid. Add a valid typeURI to the input dictionary or change the class you are using "from_dict" from.')

        for k, v in input_dict.items():
            if k == 'typeURI':
                continue
            set_value_by_dictitem(o, k, v, waarde_shortcut=waarde_shortcut)
        return o


def create_dict_from_asset(otl_object: OTLObject, waarde_shortcut=False, rdf: bool = False) -> Dict:
    """Creates a dictionary from an OTLObject with key value pairs for attributes and their values. Saves the type of the object in typeURI (or @type for the RDF dict)

    :param otl_object: input object to be transformed
    :type: OTLObject
    :param waarde_shortcut: whether to use the waarde shortcut when processing the dictionary, defaults to False
    :type: bool
    :param rdf: whether to generate a dictionary where the key's are the URI's of the attributes rather than the names, defaults to False
    :type: bool

    :return: returns an instance where the values of the attributes matches the given dictionary
    :rtype: OTLObject"""
    if rdf:
        d = _recursive_create_rdf_dict_from_asset(asset=otl_object, waarde_shortcut=waarde_shortcut)
    else:
        d = _recursive_create_dict_from_asset(otl_object, waarde_shortcut=waarde_shortcut)

    if d is None:
        d = {}
    if rdf:
        d['@type'] = otl_object.typeURI
    else:
        d['typeURI'] = otl_object.typeURI
    return d


def _recursive_create_dict_from_asset(asset: Union[OTLObject, OTLAttribuut, list, dict],
                                      waarde_shortcut: bool = False) -> Union[Dict, List[Dict]]:
    if isinstance(asset, list) and not isinstance(asset, dict):
        l = []
        for item in asset:
            dict_item = _recursive_create_dict_from_asset(asset=item, waarde_shortcut=waarde_shortcut)
            if dict_item is not None:
                l.append(dict_item)
        if len(l) > 0:
            return l
    else:
        d = {}
        for attr in asset:
            if attr.waarde is None or attr.waarde == []:
                continue

            if attr.field.waardeObject is not None:  # complex
                if waarde_shortcut and attr.field.waarde_shortcut_applicable:
                    if isinstance(attr.waarde, list):
                        dict_item = []
                        for item in attr.waarde:
                            dict_item.append(item.waarde)
                        if len(dict_item) > 0:
                            d[attr.naam] = dict_item
                    else:
                        dict_item = attr.waarde.waarde
                        if dict_item is not None:
                            d[attr.naam] = dict_item
                else:
                    dict_item = _recursive_create_dict_from_asset(asset=attr.waarde, waarde_shortcut=waarde_shortcut)
                    if dict_item is not None:
                        d[attr.naam] = dict_item
            else:
                if attr.field == TimeField:
                    d[attr.naam] = time.strftime(attr.waarde, "%H:%M:%S")
                elif attr.field == DateField:
                    d[attr.naam] = date.strftime(attr.waarde, "%Y-%m-%d")
                elif attr.field == DateTimeField:
                    d[attr.naam] = datetime.strftime(attr.waarde, "%Y-%m-%d %H:%M:%S")
                else:
                    d[attr.naam] = attr.waarde

        if len(d.items()) > 0:
            return d


def _recursive_create_rdf_dict_from_asset(asset: Union[OTLObject, OTLAttribuut, list, dict],
                                          waarde_shortcut: bool = False) -> Union[Dict, List[Dict]]:
    if isinstance(asset, list) and not isinstance(asset, dict):
        l = []
        for item in asset:
            dict_item = _recursive_create_rdf_dict_from_asset(asset=item, waarde_shortcut=waarde_shortcut)
            if dict_item is not None:
                l.append(dict_item)
        if len(l) > 0:
            return l
    else:
        d = {}
        for attr in asset:
            if attr.waarde is None or attr.waarde == []:
                continue

            if attr.field.waardeObject is not None:  # complex
                if waarde_shortcut and attr.field.waarde_shortcut_applicable:
                    if isinstance(attr.waarde, list):
                        dict_item = []
                        for item in attr.waarde:
                            dict_item.append(item.waarde)
                        if len(dict_item) > 0:
                            d[attr.objectUri] = dict_item
                    else:
                        dict_item = attr.waarde.waarde
                        if dict_item is not None:
                            d[attr.objectUri] = dict_item
                else:
                    dict_item = _recursive_create_rdf_dict_from_asset(asset=attr.waarde,
                                                                      waarde_shortcut=waarde_shortcut)
                    if dict_item is not None:
                        d[attr.objectUri] = dict_item
            else:
                if attr.field == TimeField:
                    d[attr.objectUri] = time.strftime(attr.waarde, "%H:%M:%S")
                elif attr.field == DateField:
                    d[attr.objectUri] = date.strftime(attr.waarde, "%Y-%m-%d")
                elif attr.field == DateTimeField:
                    d[attr.objectUri] = datetime.strftime(attr.waarde, "%Y-%m-%d %H:%M:%S")
                elif issubclass(attr.field, KeuzelijstField):
                    if isinstance(attr.waarde, list):
                        if attr.waarde == [None]:
                            d[attr.objectUri] = []
                        else:
                            d[attr.objectUri] = [attr.field.options[list_item].objectUri for list_item in attr.waarde]
                    else:
                        d[attr.objectUri] = attr.field.options[attr.waarde].objectUri
                else:
                    d[attr.objectUri] = attr.waarde

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
        if key == 'typeURI':
            continue
        value = d[key]
        if isinstance(value, dict):
            lines.append(prefix + f'{key} :')
            lines.extend(_make_string_version_from_dict(value, level=level + 1, indent=indent,
                                                        prefix=prefix + ' ' * indent * level))
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
                    lines.extend(_make_string_version_from_dict(item, level=level, indent=indent, list_index=index,
                                                                prefix=prefix))
                else:
                    index_string = f'[{index}]'
                    index_string += ' ' * (indent - len(index_string))
                    lines.append(prefix + index_string + f'{item}')
        else:
            lines.append(prefix + f'{key} : {value}')
    return lines


def get_attribute_by_uri(instance_or_attribute, key: str) -> OTLAttribuut:
    return next(v for v in vars(instance_or_attribute).values() if isinstance(v, OTLAttribuut) and v.objectUri == key)


def get_attribute_by_name(instance_or_attribute, key: str) -> OTLAttribuut:
    return getattr(instance_or_attribute, '_' + key)


# dict encoder = asset object to dict
# dict decoder = dict to asset object

def set_value_by_dictitem(instance_or_attribute: Union[OTLObject, OTLAttribuut], key: str, value,
                          waarde_shortcut: bool = False):
    attribute_to_set = get_attribute_by_name(instance_or_attribute, key)

    if attribute_to_set.field.waardeObject is not None:  # complex / union / KwantWrd / dte
        if isinstance(value, list):
            for index, list_item in enumerate(value):
                if attribute_to_set.waarde is None or len(attribute_to_set.waarde) <= index:
                    attribute_to_set.add_empty_value()

                if attribute_to_set.field.waarde_shortcut_applicable and waarde_shortcut:  # dte / kwantWrd
                    attribute_to_set.waarde[index]._waarde.set_waarde(list_item)
                else:  # complex / union
                    for k, v in list_item.items():
                        set_value_by_dictitem(attribute_to_set.waarde[index], k, v, waarde_shortcut)

        elif isinstance(value, dict):  # only complex / union possible
            if attribute_to_set.waarde is None:
                attribute_to_set.add_empty_value()

            if attribute_to_set.kardinaliteit_max != '1':
                for k, v in value.items():
                    set_value_by_dictitem(attribute_to_set.waarde[0], k, v, waarde_shortcut)
            else:
                for k, v in value.items():
                    set_value_by_dictitem(attribute_to_set.waarde, k, v, waarde_shortcut)
        else:  # must be a dte / kwantWrd
            if attribute_to_set.waarde is None:
                attribute_to_set.add_empty_value()

            attribute_to_set.waarde._waarde.set_waarde(value)
    else:
        attribute_to_set.set_waarde(value)

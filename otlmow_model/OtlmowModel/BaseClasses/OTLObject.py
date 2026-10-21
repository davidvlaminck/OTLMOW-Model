import warnings
from collections.abc import Generator
from pathlib import Path
from typing import Any, Optional, TypeVar, Union

from ..Exceptions.AttributeDeprecationWarning import AttributeDeprecationWarning
from ..Exceptions.CanNotClearAttributeError import CanNotClearAttributeError
from ..Exceptions.ClassDeprecationWarning import ClassDeprecationWarning
from ..Exceptions.CouldNotCreateInstanceError import CouldNotCreateInstanceError
from ..Exceptions.MethodNotApplicableError import MethodNotApplicableError
from ..Exceptions.NonStandardAttributeWarning import NonStandardAttributeWarning
from ..Helpers.generated_lists import get_hardcoded_class_dict
from ..Helpers.GenericHelper import get_titlecase_from_ns
from .AssetSerialisation import (
    build_string_version,
    clean_dict,
    create_dict_from_asset,
    set_value_by_dictitem,
)
from .DateTimeField import DateTimeField
from .DynamicLoader import (
    dynamic_create_instance_from_ns_and_name,
    dynamic_create_instance_from_uri,
    dynamic_create_type_from_ns_and_name,
    dynamic_create_type_from_uri,
)
from .OTLAttribuut import OTLAttribuut, get_attribute_by_name, get_attribute_by_uri
from .OTLField import OTLField
from .UnionTypeField import UnionTypeField
from .UnionWaarden import UnionWaarden
from .URIField import URIField

__all__ = [
    'AttributeDeprecationWarning',
    'CanNotClearAttributeError',
    'ClassDeprecationWarning',
    'CouldNotCreateInstanceError',
    'DateTimeField',
    'MethodNotApplicableError',
    'NonStandardAttributeWarning',
    'OTLAttribuut',
    'OTLField',
    'OTLObject',
    'T',
    'URIField',
    'UnionTypeField',
    'UnionWaarden',
    'build_string_version',
    'clean_dict',
    'create_dict_from_asset',
    'dynamic_create_instance_from_ns_and_name',
    'dynamic_create_instance_from_uri',
    'dynamic_create_type_from_ns_and_name',
    'dynamic_create_type_from_uri',
    'get_attribute_by_name',
    'get_attribute_by_uri',
    'get_hardcoded_class_dict',
    'get_titlecase_from_ns',
    'set_value_by_dictitem',
]

TYPEURI_KEY = 'typeURI'
RDF_TYPEURI_KEY = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject.typeURI'
TYPEURI_KEYS = {TYPEURI_KEY, RDF_TYPEURI_KEY}

T = TypeVar('T', bound='OTLObject')


class OTLObject(object):
    typeURI: str = None
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __setattr__(self, name, value):
        if name != 'typeURI':
            super(OTLObject, self).__setattr__(name, value)
            return
        self._set_type_uri(value)

    def _set_type_uri(self, value) -> None:
        if hasattr(self, 'typeURI') and (value is not None or self.typeURI is not None):
            raise ValueError(
                'The typeURI is an OSLOAttribute that indicates the class of the instance. '
                'Within a class this value is predefined and cannot be changed.'
            )
        if URIField.validate(value, OTLAttribuut(naam='typeURI')):
            self.__dict__['value'] = value
        else:
            raise ValueError(f'{value} is not a valid value for typeURI.')

    def __init__(self):
        super().__init__()

        if hasattr(self, 'deprecated_version') and self.deprecated_version is not None:
            try:
                warnings.warn(
                    message=f'{self.typeURI} is deprecated since version {self.deprecated_version}',
                    category=ClassDeprecationWarning,
                )
            except KeyError:
                warnings.warn(
                    message=f'used a class ({self.__class__.__name__}) that is deprecated since version {self.deprecated_version}',
                    category=ClassDeprecationWarning,
                )

    def return_is_otl_object(self) -> bool:
        return True

    def clear_value(self, attribute_name: str) -> None:
        if attribute_name is None:
            raise ValueError('attribute_name is None')
        attr = get_attribute_by_name(self, attribute_name)
        if attr is None:
            raise ValueError(f'attribute {attribute_name} does not exist')
        attr.clear_value()

    def create_dict_from_asset(
        self,
        waarde_shortcut: bool = False,
        rdf: bool = False,
        cast_datetime: bool = False,
        warn_for_non_otl_conform_attributes: bool = True,
        allow_non_otl_conform_attributes: bool = True,
    ) -> dict[str, Any]:
        """Converts this asset into a dictionary representation. This is now deprecated, use to_dict instead.

        :param waarde_shortcut: whether to use the waarde shortcut when processing the dictionary, defaults to False
        :type: bool
        :param rdf: whether to generate a dictionary where the keys are the URI's of the attributes
        rather than the names, defaults to False
        :type: bool
        :param cast_datetime: whether to convert dates, times and datetimes to strings, defaults to False
        :type: bool
        :param allow_non_otl_conform_attributes: whether to allow non OTL conform attributes. Raising ValueError if not, Defaults to True
        :type: bool
        :param warn_for_non_otl_conform_attributes: whether to generate warnings when using non OTL conform attributes. Defaults to True
        :type: bool

        :return: returns a dictionary representation of this asset
        :rtype: dict"""
        warnings.warn(
            message='create_dict_from_asset is deprecated, use to_dict instead', category=AttributeDeprecationWarning
        )
        return create_dict_from_asset(
            otl_object=self,
            waarde_shortcut=waarde_shortcut,
            rdf=rdf,
            cast_datetime=cast_datetime,
            warn_for_non_otl_conform_attributes=warn_for_non_otl_conform_attributes,
            allow_non_otl_conform_attributes=allow_non_otl_conform_attributes,
        )

    def fill_with_dummy_data(self):
        for attr in self:
            if attr is not None:
                attr.fill_with_dummy_data()

    def __repr__(self):
        return build_string_version(asset=self)

    def __iter__(self) -> Generator[OTLAttribuut, None, None]:
        yield from sorted(filter(lambda v: isinstance(v, OTLAttribuut), (vars(self).values())), key=lambda x: x.naam)

    def __eq__(self, value) -> bool:
        if value is None:
            return False
        return create_dict_from_asset(self, warn_for_non_otl_conform_attributes=False) == create_dict_from_asset(
            value, warn_for_non_otl_conform_attributes=False
        )

    def is_instance_of(self, otl_type: type, dynamic_created: bool = False, model_directory: Optional[Path] = None):
        if dynamic_created:
            if model_directory is None:
                model_directory = _default_model_directory()
            try:
                otl_type_typeURI = getattr(otl_type, 'typeURI')
            except AttributeError:
                return False
            dynamic_created_type = dynamic_create_type_from_uri(otl_type_typeURI, model_directory=model_directory)
            return isinstance(self, dynamic_created_type)

        check = isinstance(self, otl_type)
        if check:
            return True

        try:
            otl_type_typeURI = getattr(otl_type, 'typeURI')
        except AttributeError:
            return False

        t = type(self)
        if t.typeURI == otl_type_typeURI:
            return True
        return issubclass(self.__class__, otl_type)

    @classmethod
    def from_dict(
        cls: T,
        input_dict: dict[str, Any],
        model_directory: Optional[Path] = None,
        rdf: bool = False,
        cast_datetime: bool = False,
        waarde_shortcut: bool = False,
        allow_non_otl_conform_attributes: bool = True,
        warn_for_non_otl_conform_attributes: bool = True,
    ) -> T:
        """Alternative constructor. Allows the instantiation of an object using a dictionary. Either start from the
        appropriate class or add a typeURI entry to the dictionary to get an instance of that type.

        :param input_dict: input dictionary, containing key value pairs for the attributes of the instance
        :type: dict
        :param model_directory: directory where the model is located, defaults to otlmow_model's own model
        :type: str
        :param rdf: whether to use uri's as keys instead of the names, defaults to False
        :type: bool
        :param waarde_shortcut: whether to use the waarde shortcut when processing the dictionary, defaults to False
        :type: bool
        :param cast_datetime: whether to convert dates, times and datetimes to strings, defaults to False
        :type: bool
        :param allow_non_otl_conform_attributes: whether to allow non OTL conform attributes. Raising ValueError if not, Defaults to True
        :type: bool
        :param warn_for_non_otl_conform_attributes: whether to generate warnings when using non OTL conform attributes. Defaults to True
        :type: bool
        :return: returns an instance where the values of the attributes matches the given dictionary
        :rtype: OTLObject"""
        type_uri = _extract_type_uri(input_dict=input_dict, rdf=rdf, default_type_uri=cls.typeURI)

        if type_uri is None:
            raise ValueError(
                'typeURI is None. Add a valid typeURI to the input dictionary or change the class you are using "from_dict" from.'
            )

        if model_directory is None:
            model_directory = _default_model_directory()

        try:
            o = dynamic_create_instance_from_uri(type_uri, model_directory=model_directory)
        except TypeError:
            raise ValueError(
                'typeURI is invalid. Add a valid typeURI to the input dictionary or change the class you are using "from_dict" from.'
            )

        for k, v in input_dict.items():
            if k in TYPEURI_KEYS:
                continue
            set_value_by_dictitem(
                o,
                k,
                v,
                waarde_shortcut=waarde_shortcut,
                rdf=rdf,
                cast_datetime=cast_datetime,
                allow_non_otl_conform_attributes=allow_non_otl_conform_attributes,
                warn_for_non_otl_conform_attributes=warn_for_non_otl_conform_attributes,
            )
        return o

    def to_dict(
        self,
        rdf: bool = False,
        cast_datetime: bool = False,
        waarde_shortcut: bool = False,
        allow_non_otl_conform_attributes: bool = True,
        warn_for_non_otl_conform_attributes: bool = True,
    ) -> dict[str, Any]:
        """Converts this asset into a dictionary representation

        :param waarde_shortcut: whether to use the waarde shortcut when processing the dictionary, defaults to False
        :type: bool
        :param rdf: whether to generate a dictionary where the keys are the URI's of the attributes
        rather than the names, defaults to False
        :type: bool
        :param cast_datetime: whether to convert dates, times and datetimes to strings, defaults to False
        :type: bool
        :param allow_non_otl_conform_attributes: whether to allow non OTL conform attributes. Raising ValueError if not, Defaults to True
        :type: bool
        :param warn_for_non_otl_conform_attributes: whether to generate warnings when using non OTL conform attributes. Defaults to True
        :type: bool

        :return: returns a dictionary representation of this asset
        :rtype: dict"""
        return create_dict_from_asset(
            otl_object=self,
            waarde_shortcut=waarde_shortcut,
            rdf=rdf,
            cast_datetime=cast_datetime,
            warn_for_non_otl_conform_attributes=warn_for_non_otl_conform_attributes,
            allow_non_otl_conform_attributes=allow_non_otl_conform_attributes,
        )


def _extract_type_uri(input_dict: dict[str, Any], rdf: bool, default_type_uri: str) -> Union[str, None]:
    if not rdf and TYPEURI_KEY in input_dict:
        return input_dict[TYPEURI_KEY]
    if rdf and RDF_TYPEURI_KEY in input_dict:
        return input_dict[RDF_TYPEURI_KEY]
    if rdf and '@type' in input_dict:
        type_uri = input_dict['@type']
        del input_dict['@type']
        return type_uri
    return default_type_uri


def _default_model_directory() -> Path:
    return Path(__file__).parent.parent.parent

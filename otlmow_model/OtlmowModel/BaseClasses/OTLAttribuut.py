import math
import random
import warnings
from typing import Optional

from ..Exceptions.AttributeDeprecationWarning import AttributeDeprecationWarning
from ..Exceptions.CanNotClearAttributeError import CanNotClearAttributeError
from ..Exceptions.MethodNotApplicableError import MethodNotApplicableError
from .OTLField import OTLField
from .UnionTypeField import UnionTypeField
from .UnionWaarden import UnionWaarden

CLEARABLE_BLOCKED_OBJECT_URIS = {
    'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMDBStatus.isActief',
    'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMNaamObject.naam',
    'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMToestand.toestand',
}

DTC_IDENTIFICATOR_OBJECT_URI = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator'

NAAMPAD_OBJECT_URI = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#NaampadObject.naampad'

DUMMY_GEOMETRY = {
    'POINT Z': 'POINT Z (200000 200000 0)',
    'LINESTRING Z': 'LINESTRING Z (200000 200000 0, 200001 200001 1)',
    'POLYGON Z': 'POLYGON Z ((200000 200000 0, 200001 200001 1, 200002 200002 2, 200000 200000 0))',
}


class OTLAttribuut:
    def __init__(
        self,
        naam: str = '',
        label: str = '',
        objectUri: str = '',
        definition: str = '',
        constraints: str = '',
        usagenote: str = '',
        deprecated_version: str = '',
        kardinaliteit_min: str = '1',
        kardinaliteit_max: str = '1',
        field: type[OTLField] = OTLField,
        readonly: bool = False,
        readonlyValue=None,
        owner=None,
    ):
        super().__init__()
        self.naam: str = naam
        self.label: str = label
        self.objectUri: str = objectUri
        self.definition: str = definition
        self.constraints: str = constraints
        self.usagenote: str = usagenote
        self.deprecated_version: str = deprecated_version
        self.readonly: bool = readonly
        self.kardinaliteit_min: str = kardinaliteit_min
        self.kardinaliteit_max: str = kardinaliteit_max
        self._dotnotation: str = ''
        self.owner = owner
        self.readonlyValue = None
        self.mark_to_be_cleared: bool = False
        self.waarde = None
        self.is_otl_attribute: bool = True
        self.field: type[OTLField] = field

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
                            'This attribute does not have a cardinality other than 1, therefore you can '
                            'only call this method once per instance'
                        )
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
                values = self.waarde
                if self.waarde is None:
                    values = []
                values.append(value)
                self.set_waarde(values)

            self.add_value = add_value

        if readonly:
            self.__dict__['waarde'] = readonlyValue

    def add_value(self, value):
        raise MethodNotApplicableError(
            'This attribute does not have a cardinality other than 1 so simply assign your value directly instead of '
            'using this method'
        )

    def get_waarde(self):
        if self.field.waardeObject and self.waarde is None:
            self.add_empty_value()
        return self.waarde

    def add_empty_value(self):
        """Helper method for datatypes UnionType, ComplexType, KwantWrd and Dte to add the underlying waarde object"""
        if not self.field.waardeObject:
            raise MethodNotApplicableError(
                'In order to use this method this object must be one of these types: UnionType, ComplexType, KwantWrd, '
                'Dte'
            )

    def clear_value(self) -> None:
        if self.readonly:
            raise ValueError(f'attribute {self.naam} is readonly')
        if self._can_not_be_cleared():
            raise CanNotClearAttributeError(f'attribute {self.naam} can not be cleared')

        # complex takes precedence over cardinality
        # => complex + kard means clearing the value of each sub attribute of each item in the list
        # => complex means clearing the value of each sub attribute
        # => list means clearing the value

        if self.field.waardeObject is not None:
            self._clear_complex_value()
        else:
            self.waarde = None
            self.mark_to_be_cleared = True

    def _can_not_be_cleared(self) -> bool:
        if self.objectUri in CLEARABLE_BLOCKED_OBJECT_URIS or self.field.objectUri == DTC_IDENTIFICATOR_OBJECT_URI:
            return True
        return (
            self.owner is not None
            and hasattr(self.owner, '_parent')
            and self.owner._parent.field.objectUri == DTC_IDENTIFICATOR_OBJECT_URI
        )

    def _clear_complex_value(self) -> None:
        if self.waarde is None:
            self.add_empty_value()
        items = self.waarde if self.kardinaliteit_max != '1' else [self.waarde]
        for item in items:
            for sub_attr in item:
                if not sub_attr.readonly:
                    sub_attr.clear_value()

    def _perform_cardinality_check(self, owner, value, kardinaliteit_max):
        kardinaliteit_min = int(self.kardinaliteit_min)
        if not isinstance(value, list):
            raise TypeError(f'expecting a list in {owner.__class__.__name__}.{self.naam}')
        elif isinstance(value, set):
            raise TypeError(f'expecting a non set type of list in {owner.__class__.__name__}.{self.naam}')
        elif 0 < len(value) < kardinaliteit_min:
            raise ValueError(
                f'expecting at least {kardinaliteit_min} element(s) in {owner.__class__.__name__}.{self.naam}'
            )
        elif len(value) > kardinaliteit_max:
            raise ValueError(
                f'expecting at most {kardinaliteit_max} element(s) in {owner.__class__.__name__}.{self.naam}'
            )

    def set_waarde(self, value, owner=None):
        self._perform_deprecation_check(self)

        if value is None:
            self.waarde = None
            return

        if self._is_clearing_value(value):
            self.clear_value()
            return

        if self.kardinaliteit_max != '1':
            self._set_waarde_list(value, owner)
        else:
            self._set_waarde_single(value, owner)

        _clear_other_props_of_union(owner, value)

    def _is_clearing_value(self, value) -> bool:
        if value == self.field.clearing_value:
            return True
        return self.kardinaliteit_max != '1' and value == '88888888'

    def _set_waarde_list(self, value, owner) -> None:
        kardinaliteit_max = math.inf if self.kardinaliteit_max == '*' else int(self.kardinaliteit_max)
        self._perform_cardinality_check(owner, value, kardinaliteit_max)
        converted_values = []
        for el_value in value:
            converted_value = self._convert_value(el_value)
            if not self.field.validate(converted_value, self):
                raise ValueError(
                    f'invalid value in list for {owner.__class__.__name__}.{self.naam}: {el_value} is not '
                    f'valid, must be valid for {self.field.naam}'
                )
            converted_values.append(converted_value)
        self.waarde = converted_values

    def _set_waarde_single(self, value, owner) -> None:
        if self.field.waardeObject is not None and isinstance(value, self.field.waardeObject):
            self.waarde = value
            return
        converted_value = self._convert_value(value)
        if self.field.validate(value=converted_value, attribuut=self):
            self.waarde = converted_value
        else:
            self._raise_invalid_value(value, owner)

    def _convert_value(self, value):
        converted_value = self.field.convert_to_correct_type(value)
        if hasattr(self.field, 'options') and self.field.options is not None:
            converted_value = self.field.convert_to_invulwaarde(converted_value, self.field)
        return converted_value

    def _raise_invalid_value(self, value, owner) -> None:
        if owner is None and self.owner is not None:
            if hasattr(self.owner, '_parent') and self.owner._parent is not None:
                raise ValueError(
                    f'Could not assign the best effort converted value to {self.owner._parent.naam}.'
                    f'{self.naam}. Value {value} is not valid (type: {self.field.label})'
                )
            else:
                raise ValueError(
                    f'Could not assign the best effort converted value to {self.owner.__class__.__name__}.'
                    f'{self.naam} Value {value} is not valid (type: {self.field.label})'
                )
        raise ValueError(
            f'Could not assign the best effort converted value to {owner.__class__.__name__}.{self.naam} '
            f'Value {value} is not valid (type: {self.field.label})'
        )

    @staticmethod
    def _perform_deprecation_check(owner):
        if owner is not None:
            if owner.naam == 'waarde':
                owner = owner.owner._parent

            if hasattr(owner, 'deprecated_version') and owner.deprecated_version != '':
                if hasattr(owner, 'objectUri'):
                    warnings.warn(
                        message=f'{owner.objectUri} is deprecated since version {owner.deprecated_version}',
                        category=AttributeDeprecationWarning,
                    )
                elif hasattr(owner, 'typeURI'):
                    warnings.warn(
                        message=f'{owner.typeURI} is deprecated since version {owner.deprecated_version}',
                        category=AttributeDeprecationWarning,
                    )
                else:
                    warnings.warn(
                        message=f'used a class that is deprecated since version {owner.deprecated_version}',
                        category=AttributeDeprecationWarning,
                    )

    def __str__(self):
        return (
            f'information about {self.naam}:\n'
            f'naam: {self.naam}\n'
            f'uri: {self.objectUri}\n'
            f'definition: {self.definition}\n'
            f'label: {self.label}\n'
            f'usagenote: {self.usagenote}\n'
            f'constraints: {self.constraints}\n'
            f'readonly: {self.readonly}\n'
            f'kardinaliteit_min: {self.kardinaliteit_min}\n'
            f'kardinaliteit_max: {self.kardinaliteit_max}\n'
            f'deprecated_version: {self.deprecated_version}\n'
        )

    def fill_with_dummy_data(self):
        if self.readonly:
            return

        if self.field.waardeObject is None:
            self._fill_simple_dummy_data()
            return

        new_value_object = self._create_dummy_waarde_object()
        if self.kardinaliteit_max != '1':
            self.set_waarde([new_value_object])
        else:
            self.set_waarde(new_value_object)

    def _fill_simple_dummy_data(self) -> None:
        if self.naam == 'geometry':
            self._fill_dummy_geometry()
            return
        data = self._dummy_naampad_data() if self.objectUri == NAAMPAD_OBJECT_URI else self.field.create_dummy_data()
        if data is None or self.kardinaliteit_max == '1':
            self.set_waarde(data)
        else:
            self.set_waarde([data])

    def _fill_dummy_geometry(self) -> None:
        first_geom_type = self.owner._geometry_types[0]
        if first_geom_type in DUMMY_GEOMETRY:
            self.set_waarde(DUMMY_GEOMETRY[first_geom_type])

    def _dummy_naampad_data(self) -> str:
        naam_attr = get_attribute_by_name(self.owner, 'naam')
        if naam_attr is not None and naam_attr.waarde is not None:
            return f'dummy/{naam_attr.waarde}'
        return 'dummy/dummy'

    def _create_dummy_waarde_object(self):
        new_value_object = self.field.waardeObject()
        new_value_object._parent = self

        if getattr(new_value_object, '_is_union_waarden_object', False):
            selected_attr = random.choice(list(new_value_object))
            selected_attr.fill_with_dummy_data()
        else:
            for a in new_value_object:
                if a == 'is_waarden_object':
                    continue
                a.fill_with_dummy_data()
        return new_value_object


def _clear_other_props_of_union(owner, value) -> None:
    if value is None or owner is None:
        return
    if not _is_union_member_with_shortcut(owner):
        return
    if not _is_in_union_waarden(owner):
        return
    owner.owner.clear_other_props(f'_{owner.naam}')


def _is_union_member_with_shortcut(owner) -> bool:
    if not hasattr(owner, 'field'):
        return False
    if owner.field.waardeObject is None:
        return False
    if not owner.field.waarde_shortcut_applicable:
        return False
    return not isinstance(owner.field, UnionTypeField)


def _is_in_union_waarden(owner) -> bool:
    if owner.owner is None:
        return False
    return isinstance(owner.owner, UnionWaarden)


def get_attribute_by_uri(instance_or_attribute, key: str) -> Optional[OTLAttribuut]:
    return next((v for v in instance_or_attribute if v.objectUri == key), None)


def get_attribute_by_name(instance_or_attribute, key: str) -> Optional[OTLAttribuut]:
    return getattr(instance_or_attribute, f'_{key}', None)

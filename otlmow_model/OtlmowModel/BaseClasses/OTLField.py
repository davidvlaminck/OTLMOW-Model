from abc import abstractmethod
from typing import Any


class OTLField:
    waarde_shortcut_applicable: bool = False
    naam: str = ''
    label: str = ''
    objectUri: str = ''
    definition: str = ''
    usagenote: str = ''
    deprecated_version: str = ''
    waardeObject: Any = None
    clearing_value: Any = None
    is_otl_field: bool = True
    native_type: Any = None

    @classmethod
    def validate(cls, value: Any, attribuut) -> bool:
        if not attribuut.field.waardeObject:
            return True
        _check_complex_type(value, attribuut)
        return _validate_attributes(value)

    @classmethod
    def value_default(cls, value: Any) -> Any:
        return value

    @classmethod
    def convert_to_correct_type(cls, value: Any, log_warnings: bool = True) -> Any:
        return value

    @abstractmethod
    def __str__(self) -> str:
        return f"""information about {self.naam}:
naam: {self.naam}
uri: {self.objectUri}
definition: {self.definition}
label: {self.label}
usagenote: {self.usagenote}
deprecated_version: {self.deprecated_version}"""

    @classmethod
    def create_dummy_data(cls):
        raise NotImplementedError()


def _check_complex_type(value: Any, attribuut) -> None:
    """Raise when the value is not a complex datatype (or a list of them)."""
    if isinstance(value, list):
        for list_item in value:
            _check_complex_type_item(list_item, attribuut)
        return
    _check_complex_type_item(value, attribuut)


def _check_complex_type_item(item: Any, attribuut) -> None:
    if not isinstance(item, attribuut.field.waardeObject):
        raise ValueError(
            f'{attribuut.objectUri} is a complex datatype. Set the values through the attributes. '
            f'Use .attr_type_info() for more info'
        )


def _validate_attributes(value: Any) -> bool:
    validation = True
    for attr in value:
        if attr.waarde is None:
            continue
        if not _validate_attribute(attr):
            validation = False
            break
    return validation


def _validate_attribute(attr) -> bool:
    if attr.kardinaliteit_max != '1':
        return _validate_attribute_list(attr)
    return bool(attr.field.validate(attr.waarde, attr))


def _validate_attribute_list(attr) -> bool:
    return bool(all(attr.field.validate(value_item, attr) for value_item in attr.waarde))

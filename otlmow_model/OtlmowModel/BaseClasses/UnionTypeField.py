from typing import Any

from .OTLField import OTLField
from ..Exceptions.UnionTypeError import UnionTypeError


def _validate_against_members(value: Any, attribuut) -> bool:
    """Return whether one of the members of the union accepts the value."""
    value_dict = vars(attribuut.field.waardeObject())
    for val_in_dict in value_dict.values():
        if val_in_dict is None:
            continue
        try:
            if val_in_dict.field.validate(value, val_in_dict):
                return True
        except Exception as e:
            raise UnionTypeError(_invalid_value_message(attribuut)) from e
    return False


def _invalid_value_message(attribuut) -> str:
    return (
        f'Invalid value for {attribuut.naam}, '
        f'check attr_type_info to see what kind of values are valid.'
    )


class UnionTypeField(OTLField):
    waarde_shortcut_applicable = False
    native_type = dict

    def __str__(self):
        return OTLField.__str__(self)

    @classmethod
    def validate(cls, value: Any, attribuut) -> bool:
        if value is None:
            return True
        if isinstance(value, attribuut.field.waardeObject):
            return True
        if _validate_against_members(value, attribuut):
            return True
        raise UnionTypeError(_invalid_value_message(attribuut))

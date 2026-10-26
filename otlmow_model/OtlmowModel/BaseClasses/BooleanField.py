import random
import warnings
from typing import Optional, Any

from .OTLField import OTLField
from ..Exceptions.CouldNotConvertToCorrectTypeError import CouldNotConvertToCorrectTypeError
from ..warnings.IncorrectTypeWarning import IncorrectTypeWarning


class BooleanField(OTLField):
    """Beschrijft een tekstregel volgens http://www.w3.org/2001/XMLSchema#string."""
    naam = 'Boolean'
    objectUri = 'http://www.w3.org/2001/XMLSchema#boolean'
    definition = 'Beschrijft een boolean volgens http://www.w3.org/2001/XMLSchema#boolean.'
    label = 'Boolean'
    usagenote = 'https://www.w3.org/TR/xmlschema-2/#boolean'
    clearing_value = '88888888'
    native_type = bool

    @classmethod
    def convert_to_correct_type(cls, value: Any, log_warnings: bool = True) -> Optional[bool]:
        if value is None or value == '-':
            return cls._convert_from_none()
        if isinstance(value, bool):
            return cls._convert_from_bool(value)
        if isinstance(value, str):
            return cls._convert_from_str(value, log_warnings)
        if isinstance(value, int):
            return cls._convert_from_int(value, log_warnings)
        return cls._convert_from_fallback(value)

    @classmethod
    def _convert_from_none(cls) -> None:
        return None

    @classmethod
    def _convert_from_bool(cls, value: bool) -> bool:
        return value

    @classmethod
    def _convert_from_str(cls, value: str, log_warnings: bool) -> bool:
        lowered_value = value.lower()
        if lowered_value == 'false':
            cls._warn_converted(
                log_warnings, 'Assigned a string to a boolean datatype. '
                              'Automatically converted to the correct type. Please change the type')
            return False
        if lowered_value == 'true':
            cls._warn_converted(
                log_warnings, 'Assigned a string to a boolean datatype. '
                              'Automatically converted to the correct type. Please change the type')
            return True
        raise CouldNotConvertToCorrectTypeError(
            f'{value} could not be converted to correct type (implied by {cls.__name__})')

    @classmethod
    def _convert_from_int(cls, value: int, log_warnings: bool) -> bool:
        cls._warn_converted(
            log_warnings, 'Assigned an integer to a boolean datatype. '
                          'Automatically converted to the correct type. Please change the type')
        return value != 0

    @classmethod
    def _convert_from_fallback(cls, value: Any) -> bool:
        raise CouldNotConvertToCorrectTypeError(
            f'{value} could not be converted to correct type (implied by {cls.__name__})')

    @classmethod
    def _warn_converted(cls, log_warnings: bool, message: str) -> None:
        if log_warnings:
            warnings.warn(category=IncorrectTypeWarning, message=message)

    @classmethod
    def validate(cls, value: Any, attribuut) -> bool:
        if value == '-':
            return True
        if value is not None and not isinstance(value, bool):
            raise TypeError(f'expecting bool in {attribuut.naam}')
        return True

    def __str__(self) -> str:
        return OTLField.__str__(self)

    @classmethod
    def create_dummy_data(cls) -> bool:
        return random.choice([True, False])

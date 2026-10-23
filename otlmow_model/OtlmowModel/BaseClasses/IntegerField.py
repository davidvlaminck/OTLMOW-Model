import decimal
import random
import warnings
from typing import Optional, Any

from .OTLField import OTLField
from ..Exceptions.CouldNotConvertToCorrectTypeError import CouldNotConvertToCorrectTypeError
from ..warnings.IncorrectTypeWarning import IncorrectTypeWarning


class IntegerField(OTLField):
    """Beschrijft een geheel getal volgens http://www.w3.org/2001/XMLSchema#integer."""
    naam = 'Integer'
    objectUri = 'http://www.w3.org/2001/XMLSchema#integer'
    definition = 'Beschrijft een DateField getal volgens http://www.w3.org/2001/XMLSchema#integer.'
    label = 'Geheel getal'
    usagenote = 'https://www.w3.org/TR/xmlschema-2/#integer'
    clearing_value = 88888888
    native_type = int

    @classmethod
    def convert_to_correct_type(cls, value: Any, log_warnings: bool = True) -> Optional[int]:
        if value is None:
            return cls._convert_from_none()
        if isinstance(value, bool):
            return cls._convert_from_bool(value, log_warnings)
        if isinstance(value, int):
            return cls._convert_from_int(value)
        if isinstance(value, (float, decimal.Decimal)):
            return cls._convert_from_float(value, log_warnings)
        if isinstance(value, str):
            return cls._convert_from_str(value, log_warnings)
        return cls._convert_from_fallback(value)

    @classmethod
    def _convert_from_none(cls) -> None:
        return None

    @classmethod
    def _convert_from_bool(cls, value: bool, log_warnings: bool) -> int:
        if log_warnings:
            warnings.warn(category=IncorrectTypeWarning,
                          message='Assigned a boolean to a integer datatype. '
                                  'Automatically converted to the correct type. Please change the type')
        return value

    @classmethod
    def _convert_from_int(cls, value: int) -> int:
        return value

    @classmethod
    def _convert_from_float(cls, value, log_warnings: bool) -> int:
        i = int(value)
        if value - i != 0:
            raise CouldNotConvertToCorrectTypeError(
                f'{value} could not be converted to correct type (implied by {cls.__name__})')
        if log_warnings:
            warnings.warn(category=IncorrectTypeWarning,
                          message='Assigned a float/decimal to a integer datatype. '
                                  'Automatically converted to the correct type. Please change the type')
        return i

    @classmethod
    def _convert_from_str(cls, value: str, log_warnings: bool) -> int:
        try:
            float_value = float(value)
            int_value = int(float_value)
            if int_value != float_value:
                raise CouldNotConvertToCorrectTypeError(
                    f'{value} could not be converted to correct type (implied by {cls.__name__})')
            if log_warnings:
                warnings.warn(category=IncorrectTypeWarning,
                              message='Assigned a string to a integer datatype. '
                                      'Automatically converted to the correct type. Please change the type')
            return int_value
        except Exception as e:
            raise CouldNotConvertToCorrectTypeError(
                f'{value} could not be converted to correct type (implied by {cls.__name__})'
            ) from e

    @classmethod
    def _convert_from_fallback(cls, value: Any) -> int:
        try:
            return int(value)
        except Exception as e:
            raise CouldNotConvertToCorrectTypeError(
                f'{value} could not be converted to correct type (implied by {cls.__name__})'
            ) from e

    @classmethod
    def validate(cls, value: Any, attribuut) -> bool:
        if value is not None and not isinstance(value, int):
            raise TypeError(f'expecting an integer in {attribuut.naam}')
        return True

    def __str__(self) -> str:
        return OTLField.__str__(self)

    @classmethod
    def create_dummy_data(cls) -> int:
        return random.randint(-100, 100)

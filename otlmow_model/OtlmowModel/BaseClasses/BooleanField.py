import logging
import random
from typing import Optional, Any

from otlmow_model.OtlmowModel.BaseClasses.OTLField import OTLField
from otlmow_model.OtlmowModel.Exceptions.CouldNotConvertToCorrectTypeError import CouldNotConvertToCorrectTypeError


class BooleanField(OTLField):
    """Beschrijft een tekstregel volgens http://www.w3.org/2001/XMLSchema#string."""
    naam = 'Boolean'
    objectUri = 'http://www.w3.org/2001/XMLSchema#boolean'
    definition = 'Beschrijft een boolean volgens http://www.w3.org/2001/XMLSchema#boolean.'
    label = 'Boolean'
    usagenote = 'https://www.w3.org/TR/xmlschema-2/#boolean'

    @classmethod
    def convert_to_correct_type(cls, value: Any, log_warnings: bool = True) -> Optional[bool]:
        if value is None:
            return None
        if isinstance(value, bool):
            return value
        if isinstance(value, str):
            if value.lower() == 'false':
                if log_warnings:
                    logging.warning('Assigned a string to a boolean datatype. '
                                    'Automatically converted to the correct type. Please change the type')
                return False
            elif value.lower() == 'true':
                if log_warnings:
                    logging.warning('Assigned a string to a boolean datatype. '
                                    'Automatically converted to the correct type. Please change the type')
                return True
            else:
                raise CouldNotConvertToCorrectTypeError(
                    f'{value} could not be converted to correct type (implied by {cls.__name__})')
        elif isinstance(value, int):
            if log_warnings:
                logging.warning('Assigned an integer to a boolean datatype. '
                                'Automatically converted to the correct type. Please change the type')
            if value == 0:
                return False
            return True
        raise CouldNotConvertToCorrectTypeError(
            f'{value} could not be converted to correct type (implied by {cls.__name__})')

    @classmethod
    def validate(cls, value: Any, attribuut) -> bool:
        if value is not None and not isinstance(value, bool):
            raise TypeError(f'expecting bool in {attribuut.naam}')
        return True

    def __str__(self) -> str:
        return OTLField.__str__(self)

    @classmethod
    def create_dummy_data(cls) -> bool:
        return random.choice([True, False])

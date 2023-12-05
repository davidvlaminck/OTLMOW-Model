﻿import logging
import string
import random
from typing import Optional, Any

from otlmow_model.OtlmowModel.Exceptions.CouldNotConvertToCorrectTypeError import CouldNotConvertToCorrectTypeError
from otlmow_model.OtlmowModel.BaseClasses.OTLField import OTLField


class StringField(OTLField):
    """Beschrijft een tekstregel volgens http://www.w3.org/2001/XMLSchema#string."""
    naam = 'String'
    objectUri = 'http://www.w3.org/2001/XMLSchema#string'
    definition = 'Beschrijft een tekstregel volgens http://www.w3.org/2001/XMLSchema#string.'
    label = 'String'
    usagenote = 'https://www.w3.org/TR/xmlschema-2/#string'

    @classmethod
    def convert_to_correct_type(cls, value: Any, log_warnings: bool = True) -> Optional[str]:
        if value is None:
            return None
        if isinstance(value, str):
            return value
        if isinstance(value, list) or isinstance(value, dict):
            raise CouldNotConvertToCorrectTypeError(f'The given value of object of type {type(value)} could not be '
                                                    f'converted to string (implied by {cls.__name__})')
        try:
            str_val = str(value)
            if log_warnings:
                logging.warning('Assigned a non-string to a boolean datatype. '
                                'Automatically converted to the correct type. Please change the type')
            return str_val
        except TypeError:
            raise CouldNotConvertToCorrectTypeError(f'The given value of object of type {type(value)} could not be '
                                                    f'converted to string (implied by {cls.__name__})')

    @classmethod
    def validate(cls, value: Any, attribuut) -> bool:
        if value is not None and not isinstance(value, str):
            raise TypeError(f'expecting string in {attribuut.naam}')
        return True

    def __str__(self) -> str:
        return OTLField.__str__(self)

    @classmethod
    def create_dummy_data(cls) -> str:
        return 'dummy_' + ''.join(random.choice(string.ascii_letters) for _ in range(random.randint(1, 10)))

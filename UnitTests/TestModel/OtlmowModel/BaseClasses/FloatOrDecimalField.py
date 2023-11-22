﻿import decimal
import logging
import random

from otlmow_model.Exceptions.CouldNotConvertToCorrectTypeError import CouldNotConvertToCorrectTypeError
from otlmow_model.BaseClasses.OTLField import OTLField


class FloatOrDecimalField(OTLField):
    """Beschrijft een decimaal getal volgens http://www.w3.org/2001/XMLSchema#decimal."""
    naam = 'Decimal'
    objectUri = 'http://www.w3.org/2001/XMLSchema#decimal'
    definition = 'Beschrijft een decimaal getal volgens http://www.w3.org/2001/XMLSchema#decimal.'
    label = 'Decimaal getal'
    usagenote = 'https://www.w3.org/TR/xmlschema-2/#decimal'

    @classmethod
    def convert_to_correct_type(cls, value, log_warnings=True):
        if value is None:
            return None
        if isinstance(value, bool):
            if log_warnings:
                logging.warning(
                    'Assigned a boolean to a decimal datatype. Automatically converted to the correct type. Please change the type')
            return value
        if isinstance(value, float):
            return value
        if isinstance(value, int) or isinstance(value, decimal.Decimal):
            return float(value)
        try:
            float_value = float(value)
            if log_warnings:
                logging.warning(
                    'Assigned a string to a decimal datatype. Automatically converted to the correct type. Please change the type')
            return float_value
        except ValueError:
            raise CouldNotConvertToCorrectTypeError(f'"{value}" could not be converted to correct type (implied by {cls.__name__})')
        except TypeError:
            raise CouldNotConvertToCorrectTypeError(f'"{value}" could not be converted to correct type (implied by {cls.__name__})')

    @classmethod
    def validate(cls, value, attribuut):
        if value is not None:
            if isinstance(value, bool) or isinstance(value, float):
                return True
            raise TypeError(f'expecting a number (int, float or Decimal) in {attribuut.naam}')
        return True

    @classmethod
    def create_dummy_data(cls):
        return round(random.random() * 100, 2)

    def __str__(self):
        return OTLField.__str__(self)

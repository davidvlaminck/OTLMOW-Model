import logging
import random

from otlmow_model.Exceptions.CouldNotConvertToCorrectTypeError import CouldNotConvertToCorrectTypeError
from otlmow_model.BaseClasses.OTLField import OTLField


class BooleanField(OTLField):
    """Beschrijft een tekstregel volgens http://www.w3.org/2001/XMLSchema#string."""
    naam = 'Boolean'
    objectUri = 'http://www.w3.org/2001/XMLSchema#boolean'
    definition = 'Beschrijft een boolean volgens http://www.w3.org/2001/XMLSchema#boolean.'
    label = 'Boolean'
    usagenote = 'https://www.w3.org/TR/xmlschema-2/#boolean'

    @classmethod
    def convert_to_correct_type(cls, value, log_warnings=True):
        if value is None:
            return None
        if value == True or value == False:
            return value
        if isinstance(value, str):
            if value.lower() == 'false':
                if log_warnings:
                    logging.warning('Assigned a string to a boolean datatype. Automatically converted to the correct type. Please change the type')
                return False
            elif value.lower() == 'true':
                if log_warnings:
                    logging.warning('Assigned a string to a boolean datatype. Automatically converted to the correct type. Please change the type')
                return True
            else:
                raise CouldNotConvertToCorrectTypeError(f'{value} could not be converted to correct type (implied by {cls.__name__})')
        raise CouldNotConvertToCorrectTypeError(f'{value} could not be converted to correct type (implied by {cls.__name__})')

    @staticmethod
    def validate(value, attribuut):
        if value is not None and not isinstance(value, bool):
            raise TypeError(f'expecting bool in {attribuut.naam}')
        return True

    def __str__(self):
        return OTLField.__str__(self)

    @classmethod
    def create_dummy_data(cls):
        return random.choice([True, False])

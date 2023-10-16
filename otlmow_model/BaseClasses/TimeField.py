import logging
import random
from datetime import time, datetime, date, timezone

from otlmow_model.Exceptions.CouldNotConvertToCorrectTypeError import CouldNotConvertToCorrectTypeError
from otlmow_model.BaseClasses.OTLField import OTLField


class TimeField(OTLField):
    """Beschrijft een tekstregel volgens http://www.w3.org/2001/XMLSchema#string."""
    naam = 'Time'
    objectUri = 'http://www.w3.org/2001/XMLSchema#time'
    definition = 'Beschrijft een datum volgens http://www.w3.org/2001/XMLSchema#time.'
    label = 'Tijd'
    usagenote = 'https://www.w3.org/TR/xmlschema-2/#time'

    @classmethod
    def convert_to_correct_type(cls, value, log_warnings=True):
        if value is None:
            return None
        if isinstance(value, bool):
            raise CouldNotConvertToCorrectTypeError(f'{value} could not be converted to correct type (implied by {cls.__name__})')
        if isinstance(value, time):
            return value
        if isinstance(value, datetime):
            if log_warnings:
                logging.warning(
                    'Assigned a datetime to a time datatype. Automatically converted to the correct type. Please change the type')
            return time(value.hour, value.minute, value.second)
        if isinstance(value, date):
            if log_warnings:
                logging.warning(
                    'Assigned a date to a time datatype. Automatically converted to the correct type. Please change the type')
            return time()
        if isinstance(value, int):
            if log_warnings:
                logging.warning(
                    'Assigned a int to a date datatype. Automatically converted to the correct type. Please change the type')
            timestamp = datetime.fromtimestamp(value, timezone.utc)

            return time(timestamp.hour, timestamp.minute, timestamp.second)
        if isinstance(value, str):
            try:
                dt = datetime.strptime(value, "%H:%M:%S")
                if log_warnings:
                    logging.warning(
                        'Assigned a string to a time datatype. Automatically converted to the correct type. Please change the type')
                return time(dt.hour, dt.minute, dt.second)
            except ValueError:
                try:
                    dt = datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
                    if log_warnings:
                        logging.warning(
                            'Assigned a string to a time datatype. Automatically converted to the correct type. Please change the type')
                    return time(dt.hour, dt.minute, dt.second)
                except ValueError:
                    try:
                        dt = datetime.strptime(value, "%d/%m/%Y %H:%M:%S")
                        if log_warnings:
                            logging.warning(
                                'Assigned a string to a time datatype. Automatically converted to the correct type. Please change the type')
                        return time(dt.hour, dt.minute, dt.second)
                    except Exception:
                        raise CouldNotConvertToCorrectTypeError(f'{value} could not be converted to correct type (implied by {cls.__name__})')
        raise CouldNotConvertToCorrectTypeError(f'{value} could not be converted to correct type (implied by {cls.__name__})')

    @classmethod
    def validate(cls, value, attribuut):
        if value is not None and not isinstance(value, time):
            raise TypeError(f'expecting datetime in {attribuut.naam}')
        return True

    @classmethod
    def value_default(cls, value):
        if value is None:
            return None
        return value.strftime("%H:%M:%S")

    def __str__(self):
        return OTLField.__str__(self)

    @classmethod
    def create_dummy_data(cls):
        return time(hour=random.randint(0, 23), minute=random.randint(0, 59), second=random.randint(0, 59))

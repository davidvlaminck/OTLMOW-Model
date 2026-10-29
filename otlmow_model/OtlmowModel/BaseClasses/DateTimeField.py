import datetime
import logging
import warnings
from datetime import timedelta
from random import randrange
from typing import Any

from ..Exceptions.CouldNotConvertToCorrectTypeError import CouldNotConvertToCorrectTypeError
from .OTLField import OTLField
from ..warnings.IncorrectTypeWarning import IncorrectTypeWarning


class DateTimeField(OTLField):
    """Beschrijft een datum volgens http://www.w3.org/2001/XMLSchema#dateTime."""
    naam = 'DateTime'
    objectUri = 'http://www.w3.org/2001/XMLSchema#dateTime'
    definition = 'Beschrijft een datum volgens http://www.w3.org/2001/XMLSchema#dateTime.'
    label = 'Datumtijd'
    usagenote = 'https://www.w3.org/TR/xmlschema-2/#dateTime'
    clearing_value = '88888888'
    native_type = datetime.datetime

    @classmethod
    def validate(cls, value: Any, attribuut) -> bool:
        if value is not None and not isinstance(value, datetime.datetime):
            raise TypeError(f'expecting datetime in {attribuut.naam}')
        return True

    @classmethod
    def convert_to_correct_type(cls, value: Any, log_warnings: bool = True) -> datetime.datetime | None:
        if value is None:
            return None
        if isinstance(value, bool):
            raise CouldNotConvertToCorrectTypeError(
                f'{value} could not be converted to correct type (implied by {cls.__name__})')
        if isinstance(value, datetime.datetime):
            return value
        if isinstance(value, datetime.date):
            return cls._convert_date(value, log_warnings)
        if isinstance(value, int):
            return cls._convert_int(value, log_warnings)
        if isinstance(value, str):
            return cls._convert_string(value, log_warnings)
        return cls._convert_fallback(value)

    @classmethod
    def _convert_date(cls, value: datetime.date, log_warnings: bool) -> datetime.datetime:
        if log_warnings:
            warnings.warn(category=IncorrectTypeWarning,
                          message='Assigned a date to a datetime datatype. '
                                  'Automatically converted to the correct type. Please change the type')
        return datetime.datetime(year=value.year, month=value.month, day=value.day)

    @classmethod
    def _convert_int(cls, value: int, log_warnings: bool) -> datetime.datetime:
        if log_warnings:
            warnings.warn(category=IncorrectTypeWarning,
                          message='Assigned a int to a datetime datatype. '
                                  'Automatically converted to the correct type. Please change the type')
        timestamp = datetime.datetime.fromtimestamp(value, datetime.timezone.utc)
        return datetime.datetime(timestamp.year, timestamp.month, timestamp.day, timestamp.hour,
                                 timestamp.minute, timestamp.second)

    @classmethod
    def _convert_string(cls, value: str, log_warnings: bool) -> datetime.datetime:
        try:
            dt = datetime.datetime.strptime(value, cls._datetime_string_format(value))
        except ValueError:
            try:
                dt = datetime.datetime.strptime(value, cls._datetime_alternative_format(value))
            except Exception as e:
                raise CouldNotConvertToCorrectTypeError(
                    f'{value} could not be converted to correct type (implied by {cls.__name__})'
                ) from e
        if log_warnings:
            warnings.warn(category=IncorrectTypeWarning,
                          message='Assigned a string to a datetime datatype. '
                                  'Automatically converted to the correct type. Please change the type')
        return dt

    @classmethod
    def _convert_fallback(cls, value: Any) -> datetime.datetime:
        try:
            return datetime.datetime(value)
        except Exception as exc:
            raise CouldNotConvertToCorrectTypeError(
                f'{value} could not be converted to correct type (implied by {cls.__name__})'
            ) from exc

    @staticmethod
    def _datetime_string_format(value: str) -> str:
        if 'T' in value:
            return '%Y-%m-%dT%H:%M:%S.%f' if '.' in value else '%Y-%m-%dT%H:%M:%S'
        return '%Y-%m-%d %H:%M:%S.%f' if '.' in value else '%Y-%m-%d %H:%M:%S'

    @staticmethod
    def _datetime_alternative_format(value: str) -> str:
        if 'T' in value:
            return '%d/%m/%YT%H:%M:%S'
        return '%d/%m/%Y %H:%M:%S'

    @classmethod
    def value_default(cls, value: datetime.datetime) -> str | None:
        if value is None:
            return None
        if not isinstance(value, datetime.datetime):
            raise TypeError(f'Expecting datetime.datetime in {cls.__name__} and got {type(value)} when trying to '
                            f'parse {value}')
        if value.microsecond > 0:
            return value.strftime("%Y-%m-%dT%H:%M:%S.%f")
        else:
            return value.strftime("%Y-%m-%dT%H:%M:%S")

    def __str__(self) -> str:
        return OTLField.__str__(self)

    @staticmethod
    def random_date(start: datetime.datetime, end: datetime.datetime) -> datetime.datetime:
        delta = end - start
        int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
        random_second = randrange(int_delta)
        return start + timedelta(seconds=random_second)

    @classmethod
    def create_dummy_data(cls) -> datetime.datetime:
        return DateTimeField.random_date(start=datetime.datetime(2000, 1, 1),
                                         end=datetime.datetime(2020, 1, 1))

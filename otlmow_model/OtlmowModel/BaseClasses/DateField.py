import warnings
from datetime import date, datetime, timedelta, timezone
from random import randrange
from typing import Any

from .OTLField import OTLField
from ..Exceptions.CouldNotConvertToCorrectTypeError import CouldNotConvertToCorrectTypeError
from ..warnings.IncorrectTypeWarning import IncorrectTypeWarning


class DateField(OTLField):
    """Beschrijft een datum volgens http://www.w3.org/2001/XMLSchema#date."""

    naam = 'Date'
    objectUri = 'http://www.w3.org/2001/XMLSchema#date'
    definition = 'Beschrijft een datum volgens http://www.w3.org/2001/XMLSchema#date.'
    label = 'Datum'
    usagenote = 'https://www.w3.org/TR/xmlschema-2/#date'
    clearing_value = '88888888'
    native_type = date

    @classmethod
    def convert_to_correct_type(cls, value: Any, log_warnings: bool = True) -> date | None:
        if value is None:
            return cls._convert_from_none()
        if isinstance(value, bool):
            return cls._convert_from_bool(value)
        if isinstance(value, datetime):
            return cls._convert_from_datetime(value, log_warnings)
        if isinstance(value, date):
            return cls._convert_from_date(value)
        if isinstance(value, int):
            return cls._convert_from_int(value, log_warnings)
        if isinstance(value, str):
            return cls._convert_from_str(value, log_warnings)
        return cls._convert_from_fallback(value)

    @classmethod
    def _convert_from_none(cls) -> None:
        return None

    @classmethod
    def _convert_from_bool(cls, value: bool) -> date:
        raise CouldNotConvertToCorrectTypeError(
            f'{value} could not be converted to correct type (implied by {cls.__name__})'
        )

    @classmethod
    def _convert_from_datetime(cls, value: datetime, log_warnings: bool) -> date:
        if log_warnings:
            warnings.warn(
                category=IncorrectTypeWarning,
                message='Assigned a datetime to a date datatype. '
                'Automatically converted to the correct type. Please change the type',
            )
        return date(value.year, value.month, value.day)

    @classmethod
    def _convert_from_date(cls, value: date) -> date:
        return value

    @classmethod
    def _convert_from_int(cls, value: int, log_warnings: bool) -> date:
        if log_warnings:
            warnings.warn(
                category=IncorrectTypeWarning,
                message='Assigned a int to a date datatype. '
                'Automatically converted to the correct type. Please change the type',
            )
        timestamp = datetime.fromtimestamp(value, timezone.utc)
        return date(timestamp.year, timestamp.month, timestamp.day)

    @classmethod
    def _convert_from_str(cls, value: str, log_warnings: bool) -> date:
        try:
            dt = datetime.strptime(value, '%Y-%m-%d')
        except ValueError:
            return cls._convert_from_str_with_slashes(value, log_warnings)
        cls._warn_string_converted(log_warnings)
        return date(dt.year, dt.month, dt.day)

    @classmethod
    def _convert_from_str_with_slashes(cls, value: str, log_warnings: bool) -> date:
        try:
            dt = datetime.strptime(value, '%d/%m/%Y')
        except ValueError as e:
            raise CouldNotConvertToCorrectTypeError(
                f'{value} could not be converted to correct type (implied by {cls.__name__})'
            ) from e
        cls._warn_string_converted(log_warnings)
        return date(dt.year, dt.month, dt.day)

    @classmethod
    def _warn_string_converted(cls, log_warnings: bool) -> None:
        if log_warnings:
            warnings.warn(
                category=IncorrectTypeWarning,
                message='Assigned a string to a date datatype. '
                'Automatically converted to the correct type. Please change the type',
            )

    @classmethod
    def _convert_from_fallback(cls, value: Any) -> date:
        raise CouldNotConvertToCorrectTypeError(
            f'{value} could not be converted to correct type (implied by {cls.__name__})'
        )

    @classmethod
    def validate(cls, value: Any, attribuut) -> bool:
        if value is not None and not isinstance(value, date):
            raise TypeError(f'expecting date in {attribuut.naam}')
        return True

    @classmethod
    def value_default(cls, value: date) -> str:
        return value.strftime('%Y-%m-%d')

    def __str__(self) -> str:
        return OTLField.__str__(self)

    @classmethod
    def random_date(cls, start: date, end: date) -> date:
        delta = end - start
        int_delta = delta.days
        random_days = randrange(int_delta)
        return start + timedelta(days=random_days)

    @classmethod
    def create_dummy_data(cls) -> date:
        return DateField.random_date(start=date(2000, 1, 1), end=date(2020, 1, 1))

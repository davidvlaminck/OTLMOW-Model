import logging
import warnings
import random

from difflib import get_close_matches
from typing import Dict, Any

from ..Exceptions.AttributeDeprecationWarning import AttributeDeprecationWarning
from ..Exceptions.InvalidOptionError import InvalidOptionError
from ..Exceptions.RemovedOptionError import RemovedOptionError
from .OTLField import OTLField
from .KeuzelijstWaarde import KeuzelijstWaarde


class KeuzelijstField(OTLField):
    options: Dict[str, KeuzelijstWaarde] = {}
    codelist = ''
    clearing_value = '88888888'
    native_type = str

    @classmethod
    def create_dummy_data_keuzelijst(cls, options) -> str | None:
        in_gebruik_values = list(filter(lambda option: option.status == 'ingebruik', options.values()))
        if len(in_gebruik_values) == 0:
            return None
        return random.choice(list(map(lambda x: x.invulwaarde, in_gebruik_values)))

    @classmethod
    def validate(cls, value: Any, attribuut) -> bool:
        if value is None or value == '-':
            return True
        if not isinstance(value, str):
            raise TypeError(f'{value} is not the correct type. Expecting a string')
        if value not in attribuut.field.options.keys():
            raise _invalid_option_error(value, attribuut)

        option_value = attribuut.field.options[value]
        _check_option_status(option_value, value, attribuut)
        return True

    def __str__(self) -> str:
        s = f"""information about {self.naam}:
naam: {self.naam}
uri: {self.objectUri}
definition: {self.definition}
label: {self.label}
usagenote: {self.usagenote}
deprecated_version: {self.deprecated_version}"""
        s += '\npossible values:\n'
        s += '\n'.join(list(map(lambda x: '    ' + x.print(), self.options.values())))
        return s

    @staticmethod
    def convert_to_invulwaarde(value: str, field) -> str | None:
        if value is None or value == '':
            return value
        if value == '-':
            return None

        if value in field.options.keys():
            return value

        option = _find_option(value, field)
        if option is None:
            return value
        return option.invulwaarde


def _find_option(value: str, field) -> KeuzelijstWaarde | None:
    if value.startswith('http'):
        return _find_option_by_uri(value, field)
    return _find_option_by_label(value, field)


def _invalid_option_error(value: str, attribuut) -> InvalidOptionError:
    """Build the error of an option that is not in the list, with the closest matches."""
    closest_matches = get_close_matches(value, attribuut.field.options.keys(), n=5, cutoff=0.9)
    closest_matches_string = '", "'.join(closest_matches)

    error = InvalidOptionError(
        f'{value} is not a valid option for {attribuut.naam}, '
        f'find the valid options using print(meta_info(<object>, attribute="{attribuut.naam}"))\n'
        f'Did you mean one of these? "{closest_matches_string}"')
    error.closest_matches = closest_matches
    return error


def _check_option_status(option_value: KeuzelijstWaarde, value: str, attribuut) -> None:
    if option_value.status == 'uitgebruik':
        warnings.warn(message=f'{value} is a deprecated value for {attribuut.naam}, '
                              f'please refrain from using this value.',
                      category=AttributeDeprecationWarning)
    elif option_value.status == 'verwijderd':
        logging.error(f'{value} is no longer a valid value for {attribuut.naam}.')
        raise RemovedOptionError(f'{value} is no longer a valid value for {attribuut.naam}.')


def _find_option_by_uri(value: str, field) -> KeuzelijstWaarde | None:
    return next((option for option in field.options.values() if option.objectUri == value), None)


def _find_option_by_label(value: str, field) -> KeuzelijstWaarde | None:
    return next((option for option in field.options.values() if option.label == value), None)

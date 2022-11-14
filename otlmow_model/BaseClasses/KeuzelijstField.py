import logging
import warnings

from typing import Dict

from otlmow_model.Exceptions.AttributeDeprecationWarning import AttributeDeprecationWarning
from otlmow_model.Exceptions.RemovedOptionError import RemovedOptionError
from otlmow_model.BaseClasses.OTLField import OTLField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


class KeuzelijstField(OTLField):
    options: Dict[str, KeuzelijstWaarde] = {}
    codelist = ''

    @staticmethod
    def validate(value, attribuut):
        if value is not None:
            if not isinstance(value, str):
                raise TypeError(f'{value} is not the correct type. Expecting a string')
            if value not in attribuut.field.options.keys():
                raise ValueError(
                    f'{value} is not a valid option for {attribuut.naam}, find the valid options using print(meta_info(<object>, attribute="{attribuut.naam}"))')

            option_value = attribuut.field.options[value]
            if option_value.status == 'uitgebruik':
                warnings.warn(message=f'{value} is a deprecated value for {attribuut.naam}, please refrain from using this value.',
                              category=AttributeDeprecationWarning)
            elif option_value.status == 'verwijderd':
                logging.error(f'{value} is no longer a valid value for {attribuut.naam}.')
                raise RemovedOptionError(f'{value} is no longer a valid value for {attribuut.naam}.')
        return True

    def __str__(self):
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

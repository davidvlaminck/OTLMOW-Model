# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVerkeersregelaarVoltage(KeuzelijstField):
    """Keuzelijst met de voorkomende voltages gebruikt voor verkeersregelaars."""
    naam = 'KlVerkeersregelaarVoltage'
    label = 'Verkeersregelaar voltage'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVerkeersregelaarVoltage'
    definition = 'Keuzelijst met de voorkomende voltages gebruikt voor verkeersregelaars.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVerkeersregelaarVoltage'
    options = {
        '230': KeuzelijstWaarde(invulwaarde='230',
                                label='230',
                                status='ingebruik',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersregelaarVoltage/230'),
        '40': KeuzelijstWaarde(invulwaarde='40',
                               label='40',
                               status='ingebruik',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersregelaarVoltage/40'),
        '42': KeuzelijstWaarde(invulwaarde='42',
                               label='42',
                               status='ingebruik',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersregelaarVoltage/42')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


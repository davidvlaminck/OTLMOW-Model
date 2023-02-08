# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPoEInjectorModelnaam(KeuzelijstField):
    """De modelnaam van de PoE-injector."""
    naam = 'KlPoEInjectorModelnaam'
    label = 'Power over ethernet injector modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlPoEInjectorModelnaam'
    definition = 'De modelnaam van de PoE-injector.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPoEInjectorModelnaam'
    options = {
        'npd-5001poe': KeuzelijstWaarde(invulwaarde='npd-5001poe',
                                        label='NPD 5001POE',
                                        status='ingebruik',
                                        definitie='NPD 5001POE',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPoEInjectorModelnaam/npd-5001poe'),
        'npd-6001b': KeuzelijstWaarde(invulwaarde='npd-6001b',
                                      label='NPD 6001B',
                                      status='ingebruik',
                                      definitie='NPD 6001B',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPoEInjectorModelnaam/npd-6001b'),
        'npd-9501a': KeuzelijstWaarde(invulwaarde='npd-9501a',
                                      label='NPD 9501A',
                                      status='ingebruik',
                                      definitie='NPD 9501A',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPoEInjectorModelnaam/npd-9501a')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


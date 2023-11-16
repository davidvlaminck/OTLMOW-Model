# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlNeerslagsensorModelnaam(KeuzelijstField):
    """De modelnaam van de neerslagsensor."""
    naam = 'KlNeerslagsensorModelnaam'
    label = 'Neerslagsensor modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlNeerslagsensorModelnaam'
    definition = 'De modelnaam van de neerslagsensor.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlNeerslagsensorModelnaam'
    options = {
        'WS100': KeuzelijstWaarde(invulwaarde='WS100',
                                  label='WS100',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNeerslagsensorModelnaam/WS100'),
        'drd11a': KeuzelijstWaarde(invulwaarde='drd11a',
                                   label='DRD11A',
                                   status='ingebruik',
                                   definitie='DRD11A',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNeerslagsensorModelnaam/drd11a')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


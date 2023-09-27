# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlUPSModelnaam(KeuzelijstField):
    """De modelnaam van de UPS."""
    naam = 'KlUPSModelnaam'
    label = 'UPS modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlUPSModelnaam'
    definition = 'De modelnaam van de UPS.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlUPSModelnaam'
    options = {
        'ps15': KeuzelijstWaarde(invulwaarde='ps15',
                                 label='PS15',
                                 status='ingebruik',
                                 definitie='PS15',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlUPSModelnaam/ps15'),
        'quint4-ps-1ac-24dc-2-5-pt': KeuzelijstWaarde(invulwaarde='quint4-ps-1ac-24dc-2-5-pt',
                                                      label='QUINT4-PS-1AC-24DC-2.5-PT',
                                                      status='ingebruik',
                                                      definitie='QUINT4-PS-1AC-24DC-2.5-PT',
                                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlUPSModelnaam/quint4-ps-1ac-24dc-2-5-pt')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


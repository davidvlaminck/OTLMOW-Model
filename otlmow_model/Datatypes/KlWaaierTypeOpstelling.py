# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWaaierTypeOpstelling(KeuzelijstField):
    """Keuzelijst voor de verschillende types van opstelling van een waaier."""
    naam = 'KlWaaierTypeOpstelling'
    label = 'Waaier opstelling type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWaaierTypeOpstelling'
    definition = 'Keuzelijst voor de verschillende types van opstelling van een waaier.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWaaierTypeOpstelling'
    options = {
        'axiaal': KeuzelijstWaarde(invulwaarde='axiaal',
                                   label='axiaal',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWaaierTypeOpstelling/axiaal'),
        'gemengd': KeuzelijstWaarde(invulwaarde='gemengd',
                                    label='gemengd',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWaaierTypeOpstelling/gemengd'),
        'radiaal': KeuzelijstWaarde(invulwaarde='radiaal',
                                    label='radiaal',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWaaierTypeOpstelling/radiaal')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


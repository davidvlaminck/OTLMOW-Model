# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlContactorType(KeuzelijstField):
    """Geeft aan of het een K of Q contactor betreft."""
    naam = 'KlContactorType'
    label = 'contactor type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlContactorType'
    definition = 'Geeft aan of het een K of Q contactor betreft.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlContactorType'
    options = {
        'K': KeuzelijstWaarde(invulwaarde='K',
                              label='K',
                              status='ingebruik',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlContactorType/K'),
        'Q': KeuzelijstWaarde(invulwaarde='Q',
                              label='Q',
                              status='ingebruik',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlContactorType/Q')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


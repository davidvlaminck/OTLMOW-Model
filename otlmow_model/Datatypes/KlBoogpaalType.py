# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBoogpaalType(KeuzelijstField):
    """Draagwijdte van de boogpaal."""
    naam = 'KlBoogpaalType'
    label = 'Type boogpaal'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBoogpaalType'
    definition = 'Draagwijdte van de boogpaal.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBoogpaalType'
    options = {
        '3.50': KeuzelijstWaarde(invulwaarde='3.50',
                                 label='3.50',
                                 status='ingebruik',
                                 definitie='middelgrote draagwijdte',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoogpaalType/3.50'),
        '7.50': KeuzelijstWaarde(invulwaarde='7.50',
                                 label='7.50',
                                 status='ingebruik',
                                 definitie='grote draagwijdte',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoogpaalType/7.50')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


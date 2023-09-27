# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAflsuitingType(KeuzelijstField):
    """Het type van een afsluiting"""
    naam = 'KlAflsuitingType'
    label = 'Afsluiting type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAflsuitingType'
    definition = 'Het type van een afsluiting'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAflsuitingType'
    options = {
        'draad': KeuzelijstWaarde(invulwaarde='draad',
                                  label='Draad',
                                  status='ingebruik',
                                  definitie='Draad',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAflsuitingType/draad'),
        'hekwerk': KeuzelijstWaarde(invulwaarde='hekwerk',
                                    label='Hekwerk',
                                    status='ingebruik',
                                    definitie='Hekwerk',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAflsuitingType/hekwerk'),
        'panelen': KeuzelijstWaarde(invulwaarde='panelen',
                                    label='Panelen',
                                    status='ingebruik',
                                    definitie='Panelen',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAflsuitingType/panelen')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


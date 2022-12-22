# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTankVorm(KeuzelijstField):
    """De vorm van de tank."""
    naam = 'KlTankVorm'
    label = 'Tank vorm'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTankVorm'
    definition = 'De vorm van de tank.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTankVorm'
    options = {
        'parabolische-cilinder': KeuzelijstWaarde(invulwaarde='parabolische-cilinder',
                                                  label='parabolische cilinder',
                                                  status='ingebruik',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTankVorm/parabolische-cilinder'),
        'vlakke-cilinder': KeuzelijstWaarde(invulwaarde='vlakke-cilinder',
                                            label='vlakke cilinder',
                                            status='ingebruik',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTankVorm/vlakke-cilinder')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


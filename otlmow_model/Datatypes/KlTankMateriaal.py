# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTankMateriaal(KeuzelijstField):
    """Het materiaal waaruit de tank vervaardigd is."""
    naam = 'KlTankMateriaal'
    label = 'Tank materiaal'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTankMateriaal'
    definition = 'Het materiaal waaruit de tank vervaardigd is.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTankMateriaal'
    options = {
        'composiet': KeuzelijstWaarde(invulwaarde='composiet',
                                      label='Composiet',
                                      status='ingebruik',
                                      definitie='Composiet',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTankMateriaal/composiet'),
        'kunststof': KeuzelijstWaarde(invulwaarde='kunststof',
                                      label='Kunststof',
                                      status='ingebruik',
                                      definitie='Kunststof',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTankMateriaal/kunststof'),
        'metaal': KeuzelijstWaarde(invulwaarde='metaal',
                                   label='Metaal',
                                   status='ingebruik',
                                   definitie='Metaal',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTankMateriaal/metaal')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMateriaalLadder(KeuzelijstField):
    """Het materiaal waaruit de ladder is opgebouwd."""
    naam = 'KlMateriaalLadder'
    label = 'Materiaal ladder'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlMateriaalLadder'
    definition = 'Het materiaal waaruit de ladder is opgebouwd.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMateriaalLadder'
    options = {
        'hout': KeuzelijstWaarde(invulwaarde='hout',
                                 label='Hout',
                                 status='ingebruik',
                                 definitie='De ladder is gemaakt in hout.',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalLadder/hout'),
        'kunststof': KeuzelijstWaarde(invulwaarde='kunststof',
                                      label='Kunststof',
                                      status='ingebruik',
                                      definitie='De ladder is gemaakt in kunststof.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalLadder/kunststof'),
        'metaal': KeuzelijstWaarde(invulwaarde='metaal',
                                   label='Metaal',
                                   status='ingebruik',
                                   definitie='De ladder is gemaakt in metaal.',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalLadder/metaal')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


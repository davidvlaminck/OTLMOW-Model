# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBrandblusserBlusmiddel(KeuzelijstField):
    """Keuzelijst met de verschillende mogelijke blusmiddelen voor een brandblusser."""
    naam = 'KlBrandblusserBlusmiddel'
    label = 'Brandblusser blusmiddel'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBrandblusserBlusmiddel'
    definition = 'Keuzelijst met de verschillende mogelijke blusmiddelen voor een brandblusser.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBrandblusserBlusmiddel'
    options = {
        'co2': KeuzelijstWaarde(invulwaarde='co2',
                                label='CO2',
                                status='ingebruik',
                                definitie='CO2 als blusmiddel.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBrandblusserBlusmiddel/co2'),
        'poeder': KeuzelijstWaarde(invulwaarde='poeder',
                                   label='poeder',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBrandblusserBlusmiddel/poeder'),
        'schuim': KeuzelijstWaarde(invulwaarde='schuim',
                                   label='schuim',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBrandblusserBlusmiddel/schuim')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


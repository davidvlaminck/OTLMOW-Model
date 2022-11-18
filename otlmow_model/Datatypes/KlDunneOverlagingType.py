# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDunneOverlagingType(KeuzelijstField):
    """Types van dunne overlaging."""
    naam = 'KlDunneOverlagingType'
    label = 'Dunne overlaging type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDunneOverlagingType'
    definition = 'Types van dunne overlaging.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDunneOverlagingType'
    options = {
        'SME-D1': KeuzelijstWaarde(invulwaarde='SME-D1',
                                   label='SME-D1',
                                   status='ingebruik',
                                   definitie='SME-D1',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDunneOverlagingType/SME-D1'),
        'SME-D2': KeuzelijstWaarde(invulwaarde='SME-D2',
                                   label='SME-D2',
                                   status='ingebruik',
                                   definitie='SMA-D2',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDunneOverlagingType/SME-D2'),
        'antisliplaag': KeuzelijstWaarde(invulwaarde='antisliplaag',
                                         label='antisliplaag',
                                         status='ingebruik',
                                         definitie='antisliplaag',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDunneOverlagingType/antisliplaag')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


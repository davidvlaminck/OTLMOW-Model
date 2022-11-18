# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlRegelaarRegelaartype(KeuzelijstField):
    """Keuzelijst met verschillende types verkeersregelaars."""
    naam = 'KlRegelaarRegelaartype'
    label = 'Regelaar regelaartype'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlRegelaarRegelaartype'
    definition = 'Keuzelijst met verschillende types verkeersregelaars.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlRegelaarRegelaartype'
    options = {
        'type-0': KeuzelijstWaarde(invulwaarde='type-0',
                                   label='type 0',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRegelaarRegelaartype/type-0'),
        'type-1': KeuzelijstWaarde(invulwaarde='type-1',
                                   label='type 1',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRegelaarRegelaartype/type-1'),
        'type-2': KeuzelijstWaarde(invulwaarde='type-2',
                                   label='type 2',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRegelaarRegelaartype/type-2'),
        'type-3': KeuzelijstWaarde(invulwaarde='type-3',
                                   label='type 3',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRegelaarRegelaartype/type-3')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


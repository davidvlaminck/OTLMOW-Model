# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlElastischElementHardheid(KeuzelijstField):
    """Keuzelijst die de verschillende types hardheid van een elastisch element bevat."""
    naam = 'KlElastischElementHardheid'
    label = 'Elastisch element hardheid'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlElastischElementHardheid'
    definition = 'Keuzelijst die de verschillende types hardheid van een elastisch element bevat.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlElastischElementHardheid'
    options = {
        'shore-64': KeuzelijstWaarde(invulwaarde='shore-64',
                                     label='Shore 64',
                                     status='ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlElastischElementHardheid/shore-64'),
        'shore-92': KeuzelijstWaarde(invulwaarde='shore-92',
                                     label='Shore 92',
                                     status='ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlElastischElementHardheid/shore-92'),
        'shore-98': KeuzelijstWaarde(invulwaarde='shore-98',
                                     label='Shore 98',
                                     status='ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlElastischElementHardheid/shore-98')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


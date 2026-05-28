# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeKabelsteun(KeuzelijstField):
    """Types kabelsteun"""
    naam = 'KlTypeKabelsteun'
    label = 'Type kabelsteun'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTypeKabelsteun'
    definition = 'Types kabelsteun'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeKabelsteun'
    options = {
        'geleidend': KeuzelijstWaarde(invulwaarde='geleidend',
                                      label='geleidend',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeKabelsteun/geleidend'),
        'rollend': KeuzelijstWaarde(invulwaarde='rollend',
                                    label='rollend',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeKabelsteun/rollend')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


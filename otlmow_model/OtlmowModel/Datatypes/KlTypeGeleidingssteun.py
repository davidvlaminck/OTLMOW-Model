# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeGeleidingssteun(KeuzelijstField):
    """Types geleidingssteun"""
    naam = 'KlTypeGeleidingssteun'
    label = 'Type geleidingssteun'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTypeGeleidingssteun'
    definition = 'Types geleidingssteun'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeGeleidingssteun'
    options = {
        'geleidend': KeuzelijstWaarde(invulwaarde='geleidend',
                                      label='geleidend',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeGeleidingssteun/geleidend'),
        'rollend': KeuzelijstWaarde(invulwaarde='rollend',
                                    label='rollend',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeGeleidingssteun/rollend')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


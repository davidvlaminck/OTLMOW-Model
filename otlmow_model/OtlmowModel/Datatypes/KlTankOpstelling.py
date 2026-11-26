# coding=utf-8
from types import MappingProxyType
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTankOpstelling(KeuzelijstField):
    """De opstelling van de tank."""
    naam = 'KlTankOpstelling'
    label = 'Tank opstelling'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTankOpstelling'
    definition = 'De opstelling van de tank.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTankOpstelling'
    options: MappingProxyType[str, KeuzelijstWaarde] = MappingProxyType({
        'liggend': KeuzelijstWaarde(invulwaarde='liggend',
                                    label='liggend',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTankOpstelling/liggend'),
        'staand': KeuzelijstWaarde(invulwaarde='staand',
                                   label='staand',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTankOpstelling/staand')
    })

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


# coding=utf-8
from types import MappingProxyType

from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeBallast(KeuzelijstField):
    """De mogelijke types van balast."""
    naam = 'KlTypeBallast'
    label = 'Type ballast'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTypeBallast'
    definition = 'De mogelijke types van balast.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeBallast'
    options: MappingProxyType[str, KeuzelijstWaarde] = MappingProxyType({
        'lucht': KeuzelijstWaarde(invulwaarde='lucht',
                                  label='lucht',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBallast/lucht'),
        'water': KeuzelijstWaarde(invulwaarde='water',
                                  label='water',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBallast/water')
    })

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


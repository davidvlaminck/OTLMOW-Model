# coding=utf-8
from types import MappingProxyType
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWijzeGeleiding(KeuzelijstField):
    """De mogelijke wijzen van geleiding."""
    naam = 'KlWijzeGeleiding'
    label = 'Wijze geleiding'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlWijzeGeleiding'
    definition = 'De mogelijke wijzen van geleiding.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWijzeGeleiding'
    options: MappingProxyType[str, KeuzelijstWaarde] = MappingProxyType({
        'continu': KeuzelijstWaarde(invulwaarde='continu',
                                    label='continu',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWijzeGeleiding/continu'),
        'discreet': KeuzelijstWaarde(invulwaarde='discreet',
                                     label='discreet',
                                     status='ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWijzeGeleiding/discreet')
    })

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


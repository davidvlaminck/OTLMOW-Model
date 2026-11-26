# coding=utf-8
from types import MappingProxyType
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAansluitingMIVMeetpunt(KeuzelijstField):
    """De aansluiting van de meetlussen op het verwerkingssysteem."""
    naam = 'KlAansluitingMIVMeetpunt'
    label = 'aansluiting meetlussen'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAansluitingMIVMeetpunt'
    definition = 'De aansluiting van de meetlussen op het verwerkingssysteem.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAansluitingMIVMeetpunt'
    options: MappingProxyType[str, KeuzelijstWaarde] = MappingProxyType({
        'edv': KeuzelijstWaarde(invulwaarde='edv',
                                label='EDV',
                                status='ingebruik',
                                definitie=' EDV',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAansluitingMIVMeetpunt/edv'),
        'rechtstreeks': KeuzelijstWaarde(invulwaarde='rechtstreeks',
                                         label='Rechtstreeks',
                                         status='ingebruik',
                                         definitie='Rechtstreeks',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAansluitingMIVMeetpunt/rechtstreeks'),
        'uxl': KeuzelijstWaarde(invulwaarde='uxl',
                                label='UXL',
                                status='ingebruik',
                                definitie='UXL',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAansluitingMIVMeetpunt/uxl')
    })

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


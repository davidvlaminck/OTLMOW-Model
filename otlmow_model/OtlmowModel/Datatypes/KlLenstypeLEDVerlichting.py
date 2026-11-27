# coding=utf-8
from types import MappingProxyType

from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLenstypeLEDVerlichting(KeuzelijstField):
    """De mogelijke lenstypes van een LED verlichting."""
    naam = 'KlLenstypeLEDVerlichting'
    label = 'Lenstype LED verlichting'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLenstypeLEDVerlichting'
    definition = 'De mogelijke lenstypes van een LED verlichting.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLenstypeLEDVerlichting'
    options: MappingProxyType[str, KeuzelijstWaarde] = MappingProxyType({
        '5068': KeuzelijstWaarde(invulwaarde='5068',
                                 label='5068',
                                 status='ingebruik',
                                 definitie='5068',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLenstypeLEDVerlichting/5068'),
        '5112': KeuzelijstWaarde(invulwaarde='5112',
                                 label='5112',
                                 status='ingebruik',
                                 definitie='5112',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLenstypeLEDVerlichting/5112'),
        '5121': KeuzelijstWaarde(invulwaarde='5121',
                                 label='5121',
                                 status='ingebruik',
                                 definitie='5121',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLenstypeLEDVerlichting/5121'),
        '5136': KeuzelijstWaarde(invulwaarde='5136',
                                 label='5136',
                                 status='ingebruik',
                                 definitie='5136',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLenstypeLEDVerlichting/5136'),
        '5137': KeuzelijstWaarde(invulwaarde='5137',
                                 label='5137',
                                 status='ingebruik',
                                 definitie='5137',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLenstypeLEDVerlichting/5137'),
        '5138': KeuzelijstWaarde(invulwaarde='5138',
                                 label='5138',
                                 status='ingebruik',
                                 definitie='5138',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLenstypeLEDVerlichting/5138'),
        '5139': KeuzelijstWaarde(invulwaarde='5139',
                                 label='5139',
                                 status='ingebruik',
                                 definitie='5139',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLenstypeLEDVerlichting/5139'),
        '5234': KeuzelijstWaarde(invulwaarde='5234',
                                 label='5234',
                                 status='ingebruik',
                                 definitie='5234',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLenstypeLEDVerlichting/5234'),
        '5235': KeuzelijstWaarde(invulwaarde='5235',
                                 label='5235',
                                 status='ingebruik',
                                 definitie='5235',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLenstypeLEDVerlichting/5235'),
        '5300': KeuzelijstWaarde(invulwaarde='5300',
                                 label='5300',
                                 status='ingebruik',
                                 definitie='5300',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLenstypeLEDVerlichting/5300'),
        '5301': KeuzelijstWaarde(invulwaarde='5301',
                                 label='5301',
                                 status='ingebruik',
                                 definitie='5301',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLenstypeLEDVerlichting/5301'),
        '5308': KeuzelijstWaarde(invulwaarde='5308',
                                 label='5308',
                                 status='ingebruik',
                                 definitie='5308',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLenstypeLEDVerlichting/5308'),
        '5367': KeuzelijstWaarde(invulwaarde='5367',
                                 label='5367',
                                 status='ingebruik',
                                 definitie='5367',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLenstypeLEDVerlichting/5367')
    })

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


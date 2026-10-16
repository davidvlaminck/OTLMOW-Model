# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLenstypeLEDVerlichting(KeuzelijstField):
    """De mogelijke lenstypes van een LED verlichting."""
    naam = 'KlLenstypeLEDVerlichting'
    label = 'Lenstype LED verlichting'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLenstypeLEDVerlichting'
    definition = 'De mogelijke lenstypes van een LED verlichting.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLenstypeLEDVerlichting'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


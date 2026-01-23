# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMerkRookdetector(KeuzelijstField):
    """Het merk van de rookdetector."""
    naam = 'KlMerkRookdetector'
    label = 'merk rookdetector'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlMerkRookdetector'
    definition = 'Het merk van de rookdetector.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMerkRookdetector'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlStaalsoortMetEquivalenten(KeuzelijstField):
    """De soort van het staal."""
    naam = 'KlStaalsoortMetEquivalenten'
    label = 'Staalsoort met equivalenten'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlStaalsoortMetEquivalenten'
    definition = 'De soort van het staal.'
    status = 'ingebruik'
    deprecated_version = '2.18.0'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlStaalsoortMetEquivalenten'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


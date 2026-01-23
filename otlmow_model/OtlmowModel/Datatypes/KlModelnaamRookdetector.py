# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlModelnaamRookdetector(KeuzelijstField):
    """De modelnaam van de rookdetector."""
    naam = 'KlModelnaamRookdetector'
    label = 'modelnaam rookdetector'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlModelnaamRookdetector'
    definition = 'De modelnaam van de rookdetector.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlModelnaamRookdetector'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


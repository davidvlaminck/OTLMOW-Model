# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlConserveringssysteem(KeuzelijstField):
    """De mogelijke conserveringssystemen."""
    naam = 'KlConserveringssysteem'
    label = 'Conserveringssystemen'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlConserveringssysteem'
    definition = 'De mogelijke conserveringssystemen.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlConserveringssysteem'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


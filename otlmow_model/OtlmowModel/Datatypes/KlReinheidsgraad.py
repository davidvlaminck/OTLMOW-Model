# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlReinheidsgraad(KeuzelijstField):
    """De mogelijke reinheidsgraden."""
    naam = 'KlReinheidsgraad'
    label = 'Reinheidsgraad'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlReinheidsgraad'
    definition = 'De mogelijke reinheidsgraden.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlReinheidsgraad'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMateriaalLeuning(KeuzelijstField):
    """De mogelijke materialen waar de leuning uit kan bestaan."""
    naam = 'KlMateriaalLeuning'
    label = 'materiaal leuning'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlMateriaalLeuning'
    definition = 'De mogelijke materialen waar de leuning uit kan bestaan.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMateriaalLeuning'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlIlluminatorModelnaam(KeuzelijstField):
    """De mogelijke modenamen van een illuminator."""
    naam = 'KlIlluminatorModelnaam'
    label = 'Illuminator modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlIlluminatorModelnaam'
    definition = 'De mogelijke modenamen van een illuminator.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlIlluminatorModelnaam'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


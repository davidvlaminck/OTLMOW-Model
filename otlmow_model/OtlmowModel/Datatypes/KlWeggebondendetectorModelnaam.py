# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWeggebondendetectorModelnaam(KeuzelijstField):
    """Keuzelijst met modelnamen voor Weggebondendetector."""
    naam = 'KlWeggebondendetectorModelnaam'
    label = 'Weggebondendetector modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWeggebondendetectorModelnaam'
    definition = 'Keuzelijst met modelnamen voor Weggebondendetector.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWeggebondendetectorModelnaam'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


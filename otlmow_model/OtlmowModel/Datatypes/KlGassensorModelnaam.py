# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlGassensorModelnaam(KeuzelijstField):
    """Keuzelijst die de modelnamen van gassensoren bevat."""
    naam = 'KlGassensorModelnaam'
    label = 'Gassensor modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlGassensorModelnaam'
    definition = 'Keuzelijst die de modelnamen van gassensoren bevat.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlGassensorModelnaam'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


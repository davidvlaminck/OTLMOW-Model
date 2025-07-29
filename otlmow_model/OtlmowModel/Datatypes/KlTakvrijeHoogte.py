# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTakvrijeHoogte(KeuzelijstField):
    """De mogelijke opties voor de takvrije hoogte in meter."""
    naam = 'KlTakvrijeHoogte'
    label = 'Takvrije hoogte'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTakvrijeHoogte'
    definition = 'De mogelijke opties voor de takvrije hoogte in meter.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTakvrijeHoogte'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


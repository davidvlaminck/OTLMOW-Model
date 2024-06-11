# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlOpenInfiltratievoorzieningType(KeuzelijstField):
    """De mogelijke types van een open infiltratievoorziening."""
    naam = 'KlOpenInfiltratievoorzieningType'
    label = 'Open infiltratievoorziening type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlOpenInfiltratievoorzieningType'
    definition = 'De mogelijke types van een open infiltratievoorziening.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlOpenInfiltratievoorzieningType'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


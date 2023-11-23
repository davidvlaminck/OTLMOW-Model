# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWentellagerType(KeuzelijstField):
    """Keuzelijst voor de verschillende soorten wentellager."""
    naam = 'KlWentellagerType'
    label = 'Wentellager type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWentellagerType'
    definition = 'Keuzelijst voor de verschillende soorten wentellager.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWentellagerType'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


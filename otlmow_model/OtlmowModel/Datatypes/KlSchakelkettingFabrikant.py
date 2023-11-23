# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSchakelkettingFabrikant(KeuzelijstField):
    """Keuzelijst voor de fabrikanten van schakelkettings."""
    naam = 'KlSchakelkettingFabrikant'
    label = 'Schakelketting fabrikant'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSchakelkettingFabrikant'
    definition = 'Keuzelijst voor de fabrikanten van schakelkettings.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSchakelkettingFabrikant'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


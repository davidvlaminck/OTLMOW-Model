# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAfsluitkraanModelnaam(KeuzelijstField):
    """Modelnamen van afsluitkranen volgens de fabrikant."""
    naam = 'KlAfsluitkraanModelnaam'
    label = 'Modelnaam afsluitkraan'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAfsluitkraanModelnaam'
    definition = 'Modelnamen van afsluitkranen volgens de fabrikant.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAfsluitkraanModelnaam'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBypassSchakelaarModelnaam(KeuzelijstField):
    """Modelnamen voor bypass schakelaars volgens de fabrikant."""
    naam = 'KlBypassSchakelaarModelnaam'
    label = 'Modelnamen bypass schakelaars'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBypassSchakelaarModelnaam'
    definition = 'Modelnamen voor bypass schakelaars volgens de fabrikant.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBypassSchakelaarModelnaam'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


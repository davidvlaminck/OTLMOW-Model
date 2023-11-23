# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVlotterschalelaarModelnaam(KeuzelijstField):
    """Modelnamen van de vlotterschakelaar."""
    naam = 'KlVlotterschalelaarModelnaam'
    label = 'Vlotterschakelaar modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVlotterschalelaarModelnaam'
    definition = 'Modelnamen van de vlotterschakelaar.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVlotterschalelaarModelnaam'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


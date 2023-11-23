# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWentellagerModelnaam(KeuzelijstField):
    """Lijst van modelnamen van wentellagers volgens de fabrikant."""
    naam = 'KlWentellagerModelnaam'
    label = 'Wentellager modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWentellagerModelnaam'
    definition = 'Lijst van modelnamen van wentellagers volgens de fabrikant.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWentellagerModelnaam'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


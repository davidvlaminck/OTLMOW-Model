# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlZendontvangerModelnaam(KeuzelijstField):
    """Lijst van modelnamen van zendontvangers volgens de fabrikant."""
    naam = 'KlZendontvangerModelnaam'
    label = 'Zendontvanger modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlZendontvangerModelnaam'
    definition = 'Lijst van modelnamen van zendontvangers volgens de fabrikant.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlZendontvangerModelnaam'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


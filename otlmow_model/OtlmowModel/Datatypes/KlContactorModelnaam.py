# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlContactorModelnaam(KeuzelijstField):
    """Keuzelijst met modelnaen van de contactoren volgens de fabrikanten."""
    naam = 'KlContactorModelnaam'
    label = 'Contactor modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlContactorModelnaam'
    definition = 'Keuzelijst met modelnaen van de contactoren volgens de fabrikanten.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlContactorModelnaam'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


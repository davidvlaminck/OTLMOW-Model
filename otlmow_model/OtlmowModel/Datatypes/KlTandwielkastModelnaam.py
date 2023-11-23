# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTandwielkastModelnaam(KeuzelijstField):
    """Lijst van modelnamen van tandwielkasten volgens de fabrikant."""
    naam = 'KlTandwielkastModelnaam'
    label = 'Modelnamen tandwielkasten'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTandwielkastModelnaam'
    definition = 'Lijst van modelnamen van tandwielkasten volgens de fabrikant.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTandwielkastModelnaam'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


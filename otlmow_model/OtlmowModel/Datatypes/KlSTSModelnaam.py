# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSTSModelnaam(KeuzelijstField):
    """Lijst van modelnamen volgens de fabrikant van automatische omschakelaars (Static Transfer Switch)."""
    naam = 'KlSTSModelnaam'
    label = 'Modelnamen STS'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSTSModelnaam'
    definition = 'Lijst van modelnamen volgens de fabrikant van automatische omschakelaars (Static Transfer Switch).'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSTSModelnaam'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


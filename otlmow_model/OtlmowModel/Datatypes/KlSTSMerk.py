# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSTSMerk(KeuzelijstField):
    """Lijst van merknamen volgens de fabrikant van automatische omschakelaars (Static Transfer Switch)."""
    naam = 'KlSTSMerk'
    label = 'Merknamen STS'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSTSMerk'
    definition = 'Lijst van merknamen volgens de fabrikant van automatische omschakelaars (Static Transfer Switch).'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSTSMerk'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


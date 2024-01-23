# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeNutsvoorziening(KeuzelijstField):
    """Het type nutsvoorziening van een straatkap verwijst naar de specifieke aard van de nutsinfrastructuur waartoe het deksel toegang biedt."""
    naam = 'KlTypeNutsvoorziening'
    label = 'Keuzelijst type nutsvoorziening'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTypeNutsvoorziening'
    definition = 'Het type nutsvoorziening van een straatkap verwijst naar de specifieke aard van de nutsinfrastructuur waartoe het deksel toegang biedt.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeNutsvoorziening'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


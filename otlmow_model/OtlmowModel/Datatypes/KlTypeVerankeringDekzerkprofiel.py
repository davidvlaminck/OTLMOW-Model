# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeVerankeringDekzerkprofiel(KeuzelijstField):
    """Lijst met de verschillende opties voor de verankering van een dekzerkprofiel."""
    naam = 'KlTypeVerankeringDekzerkprofiel'
    label = 'type verankering dekzerkprofiel'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTypeVerankeringDekzerkprofiel'
    definition = 'Lijst met de verschillende opties voor de verankering van een dekzerkprofiel.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeVerankeringDekzerkprofiel'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


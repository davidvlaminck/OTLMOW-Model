# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMateriaalVoegband(KeuzelijstField):
    """Lijst met de verschillende opties van materiaal voor een voegband."""
    naam = 'KlMateriaalVoegband'
    label = 'keuzelijst materiaal voegband'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlMateriaalVoegband'
    definition = 'Lijst met de verschillende opties van materiaal voor een voegband.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMateriaalVoegband'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


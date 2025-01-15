# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMateriaalVoegplaat(KeuzelijstField):
    """Lijst met de verschillende opties van materiaal voor een voegplaat."""
    naam = 'KlMateriaalVoegplaat'
    label = 'materiaal voegplaat'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlMateriaalVoegplaat'
    definition = 'Lijst met de verschillende opties van materiaal voor een voegplaat.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMateriaalVoegplaat'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


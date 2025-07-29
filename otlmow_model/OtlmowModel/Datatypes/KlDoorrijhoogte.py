# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDoorrijhoogte(KeuzelijstField):
    """De mogelijke opties voor doorrijhoogte in meters."""
    naam = 'KlDoorrijhoogte'
    label = 'Doorrijhoogte'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDoorrijhoogte'
    definition = 'De mogelijke opties voor doorrijhoogte in meters.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDoorrijhoogte'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


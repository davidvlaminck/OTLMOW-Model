# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSimkaarttype(KeuzelijstField):
    """De mogelijk types van een simkaart."""
    naam = 'KlSimkaarttype'
    label = 'Simkaarttype'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSimkaarttype'
    definition = 'De mogelijk types van een simkaart.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSimkaarttype'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


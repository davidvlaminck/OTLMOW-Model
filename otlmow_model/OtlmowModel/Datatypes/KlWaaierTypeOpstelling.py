# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWaaierTypeOpstelling(KeuzelijstField):
    """Keuzelijst voor de verschillende types van opstelling van een waaier."""
    naam = 'KlWaaierTypeOpstelling'
    label = 'Waaier opstelling type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWaaierTypeOpstelling'
    definition = 'Keuzelijst voor de verschillende types van opstelling van een waaier.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWaaierTypeOpstelling'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


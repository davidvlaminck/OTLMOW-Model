# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVormGolfplaat(KeuzelijstField):
    """De verschillende mogelijke vormen van de golfplaat."""
    naam = 'KlVormGolfplaat'
    label = 'vorm golfplaat'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVormGolfplaat'
    definition = 'De verschillende mogelijke vormen van de golfplaat.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVormGolfplaat'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


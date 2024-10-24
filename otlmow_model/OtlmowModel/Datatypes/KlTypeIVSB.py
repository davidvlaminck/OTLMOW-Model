# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeIVSB(KeuzelijstField):
    """De mogelijke types van een inwendig verlicht signalisatiebord."""
    naam = 'KlTypeIVSB'
    label = 'type inwendig verlicht signalisatiebord'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTypeIVSB'
    definition = 'De mogelijke types van een inwendig verlicht signalisatiebord.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeIVSB'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlOverigeFunctiesCentreerinrichting(KeuzelijstField):
    """De overige functies van de centreerinrichting."""
    naam = 'KlOverigeFunctiesCentreerinrichting'
    label = 'overige functies centreerinrichting'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlOverigeFunctiesCentreerinrichting'
    definition = 'De overige functies van de centreerinrichting.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlOverigeFunctiesCentreerinrichting'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


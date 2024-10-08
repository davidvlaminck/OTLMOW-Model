# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlElastischElementMateriaal(KeuzelijstField):
    """Keuzelijst die de materialen bevat waaruit een elastisch element vervaardigd kan zijn."""
    naam = 'KlElastischElementMateriaal'
    label = 'Elastisch element materiaal'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlElastischElementMateriaal'
    definition = 'Keuzelijst die de materialen bevat waaruit een elastisch element vervaardigd kan zijn.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlElastischElementMateriaal'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


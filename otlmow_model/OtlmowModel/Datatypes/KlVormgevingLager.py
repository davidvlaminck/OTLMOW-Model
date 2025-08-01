# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVormgevingLager(KeuzelijstField):
    """Mogelijke vormen"""
    naam = 'KlVormgevingLager'
    label = 'Vormgeving'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVormgevingLager'
    definition = 'Mogelijke vormen'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVormgevingLager'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


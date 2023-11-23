# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPrimaireVormCombiwand(KeuzelijstField):
    """De mogelijke primaire vormen van een combiwand."""
    naam = 'KlPrimaireVormCombiwand'
    label = 'Primaire vorm combiwand'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlPrimaireVormCombiwand'
    definition = 'De mogelijke primaire vormen van een combiwand.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPrimaireVormCombiwand'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


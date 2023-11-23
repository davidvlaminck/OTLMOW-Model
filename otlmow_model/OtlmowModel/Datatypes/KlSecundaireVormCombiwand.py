# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSecundaireVormCombiwand(KeuzelijstField):
    """De mogelijke secundaire vormen van een combiwand."""
    naam = 'KlSecundaireVormCombiwand'
    label = 'Secundaire combiwand'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlSecundaireVormCombiwand'
    definition = 'De mogelijke secundaire vormen van een combiwand.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSecundaireVormCombiwand'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


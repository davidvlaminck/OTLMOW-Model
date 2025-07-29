# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeAnkerplaat(KeuzelijstField):
    """Lijst met de verschilende types van een ankerplaat"""
    naam = 'KlTypeAnkerplaat'
    label = 'Type ankerplaat'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTypeAnkerplaat'
    definition = 'Lijst met de verschilende types van een ankerplaat'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeAnkerplaat'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


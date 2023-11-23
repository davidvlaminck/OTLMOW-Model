# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlUitvoeringsmethodeBekisting(KeuzelijstField):
    """De uitvoeringsmethode van de bekisting."""
    naam = 'KlUitvoeringsmethodeBekisting'
    label = 'Uitvoeringsmethode bekisting'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlUitvoeringsmethodeBekisting'
    definition = 'De uitvoeringsmethode van de bekisting.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlUitvoeringsmethodeBekisting'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


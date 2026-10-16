# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBranddetectorSensortype(KeuzelijstField):
    """De mogelijke types van sensor die in een  branddetector wordt gebruikt."""
    naam = 'KlBranddetectorSensortype'
    label = 'Branddetector sensortype'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBranddetectorSensortype'
    definition = 'De mogelijke types van sensor die in een  branddetector wordt gebruikt.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBranddetectorSensortype'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


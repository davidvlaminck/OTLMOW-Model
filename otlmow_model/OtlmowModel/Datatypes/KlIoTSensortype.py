# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlIoTSensortype(KeuzelijstField):
    """De mogelijke types van IoT sensoren."""
    naam = 'KlIoTSensortype'
    label = 'type sensor'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlIoTSensortype'
    definition = 'De mogelijke types van IoT sensoren.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlIoTSensortype'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


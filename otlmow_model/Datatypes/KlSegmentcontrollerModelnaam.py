# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSegmentcontrollerModelnaam(KeuzelijstField):
    """De mogelijke modelnamen voor een segmentcontroller."""
    naam = 'KlSegmentcontrollerModelnaam'
    label = 'Segmentcontroller modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSegmentcontrollerModelnaam'
    definition = 'De mogelijke modelnamen voor een segmentcontroller.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSegmentcontrollerModelnaam'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


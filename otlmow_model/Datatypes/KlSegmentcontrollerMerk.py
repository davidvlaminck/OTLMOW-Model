# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSegmentcontrollerMerk(KeuzelijstField):
    """De mogelijke merken voor een segmentcontroller."""
    naam = 'KlSegmentcontrollerMerk'
    label = 'Segmentcontroller merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSegmentcontrollerMerk'
    definition = 'De mogelijke merken voor een segmentcontroller.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSegmentcontrollerMerk'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


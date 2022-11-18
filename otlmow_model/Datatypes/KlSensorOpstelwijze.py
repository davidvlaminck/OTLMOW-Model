# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSensorOpstelwijze(KeuzelijstField):
    """Senor opstelwijzen."""
    naam = 'KlSensorOpstelwijze'
    label = 'Sensor opstelwijze'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlSensorOpstelwijze'
    definition = 'Senor opstelwijzen.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSensorOpstelwijze'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


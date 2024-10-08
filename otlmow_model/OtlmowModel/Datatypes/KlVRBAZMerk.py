# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVRBAZMerk(KeuzelijstField):
    """Keuzelijst met merknamen voor VRBAZ."""
    naam = 'KlVRBAZMerk'
    label = 'VR-BAZ merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVRBAZMerk'
    definition = 'Keuzelijst met merknamen voor VRBAZ.'
    status = 'ingebruik'
    deprecated_version = '2.12.0'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVRBAZMerk'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


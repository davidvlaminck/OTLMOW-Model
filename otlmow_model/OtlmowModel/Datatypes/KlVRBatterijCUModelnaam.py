# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVRBatterijCUModelnaam(KeuzelijstField):
    """Keuzelijst met modelnamen voor VRBatterijCU."""
    naam = 'KlVRBatterijCUModelnaam'
    label = 'Batterij CU modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVRBatterijCUModelnaam'
    definition = 'Keuzelijst met modelnamen voor VRBatterijCU.'
    status = 'ingebruik'
    deprecated_version = '2.12.0'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVRBatterijCUModelnaam'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


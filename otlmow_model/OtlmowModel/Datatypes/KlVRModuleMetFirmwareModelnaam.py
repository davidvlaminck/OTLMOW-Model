# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVRModuleMetFirmwareModelnaam(KeuzelijstField):
    """Lijst met modelnamen voor VR-modules met firmware."""
    naam = 'KlVRModuleMetFirmwareModelnaam'
    label = 'VR-module met firmware modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlVRModuleMetFirmwareModelnaam'
    definition = 'Lijst met modelnamen voor VR-modules met firmware.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVRModuleMetFirmwareModelnaam'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


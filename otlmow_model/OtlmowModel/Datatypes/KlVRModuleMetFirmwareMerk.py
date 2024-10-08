# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVRModuleMetFirmwareMerk(KeuzelijstField):
    """Lijst met merken van VR-modules met firmware."""
    naam = 'KlVRModuleMetFirmwareMerk'
    label = 'VR-module met firmware merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlVRModuleMetFirmwareMerk'
    definition = 'Lijst met merken van VR-modules met firmware.'
    status = 'ingebruik'
    deprecated_version = '2.12.0'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVRModuleMetFirmwareMerk'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


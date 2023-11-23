# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTGCUitbreidingsModuleModelnaam(KeuzelijstField):
    """Keuzelijst met modelnamen van uitbreidingsmodules van een toegangscontroller."""
    naam = 'KlTGCUitbreidingsModuleModelnaam'
    label = 'TGC uitbreidingsmodule modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTGCUitbreidingsModuleModelnaam'
    definition = 'Keuzelijst met modelnamen van uitbreidingsmodules van een toegangscontroller.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTGCUitbreidingsModuleModelnaam'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


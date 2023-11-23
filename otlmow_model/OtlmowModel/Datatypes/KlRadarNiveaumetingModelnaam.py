# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlRadarNiveaumetingModelnaam(KeuzelijstField):
    """Modelnamen van de radarniveaumeting."""
    naam = 'KlRadarNiveaumetingModelnaam'
    label = 'Radarniveaumeting modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlRadarNiveaumetingModelnaam'
    definition = 'Modelnamen van de radarniveaumeting.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlRadarNiveaumetingModelnaam'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


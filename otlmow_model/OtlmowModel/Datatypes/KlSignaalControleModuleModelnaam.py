# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSignaalControleModuleModelnaam(KeuzelijstField):
    """De modelnaam van de signaal controle module."""
    naam = 'KlSignaalControleModuleModelnaam'
    label = 'Signaal controle module modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSignaalControleModuleModelnaam'
    definition = 'De modelnaam van de signaal controle module.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSignaalControleModuleModelnaam'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlControlepaneelModelnaam(KeuzelijstField):
    """De modelnaam van het controlepaneel"""
    naam = 'KlControlepaneelModelnaam'
    label = 'Controlepaneel modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlControlepaneelModelnaam'
    definition = 'De modelnaam van het controlepaneel'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlControlepaneelModelnaam'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


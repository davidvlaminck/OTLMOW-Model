# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTemperatuursensorModelnaam(KeuzelijstField):
    """De verschillende modelnamen van een temperatuursensor."""
    naam = 'KlTemperatuursensorModelnaam'
    label = 'Temperatuursensor modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTemperatuursensorModelnaam'
    definition = 'De verschillende modelnamen van een temperatuursensor.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTemperatuursensorModelnaam'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


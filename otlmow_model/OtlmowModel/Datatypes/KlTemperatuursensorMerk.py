# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTemperatuursensorMerk(KeuzelijstField):
    """De verschillende merken van een temperatuursensor."""
    naam = 'KlTemperatuursensorMerk'
    label = 'Temperatuursensor merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTemperatuursensorMerk'
    definition = 'De verschillende merken van een temperatuursensor.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTemperatuursensorMerk'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


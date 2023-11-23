# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBewegingssensorModelnaam(KeuzelijstField):
    """De modelnaam van een bewegingssensor."""
    naam = 'KlBewegingssensorModelnaam'
    label = 'Bewegingssensor modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBewegingssensorModelnaam'
    definition = 'De modelnaam van een bewegingssensor.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBewegingssensorModelnaam'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


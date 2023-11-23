# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlUltrasoonNiveaumetingModelnaam(KeuzelijstField):
    """Modelnaam van de ultrasoon niveaumeting."""
    naam = 'KlUltrasoonNiveaumetingModelnaam'
    label = 'Ultrasoon niveaumeting modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlUltrasoonNiveaumetingModelnaam'
    definition = 'Modelnaam van de ultrasoon niveaumeting.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlUltrasoonNiveaumetingModelnaam'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


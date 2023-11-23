# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlFMRepeaterBoxMerk(KeuzelijstField):
    """Merknaam van de FM repeaterbox module."""
    naam = 'KlFMRepeaterBoxMerk'
    label = 'FM repeaterbox modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlFMRepeaterBoxMerk'
    definition = 'Merknaam van de FM repeaterbox module.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlFMRepeaterBoxMerk'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


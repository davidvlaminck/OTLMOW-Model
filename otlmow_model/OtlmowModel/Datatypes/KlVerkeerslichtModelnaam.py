# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVerkeerslichtModelnaam(KeuzelijstField):
    """Keuzelijst met modelnamen voor Verkeerslicht."""
    naam = 'KlVerkeerslichtModelnaam'
    label = 'verkeerslicht modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlVerkeerslichtModelnaam'
    definition = 'Keuzelijst met modelnamen voor Verkeerslicht.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVerkeerslichtModelnaam'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


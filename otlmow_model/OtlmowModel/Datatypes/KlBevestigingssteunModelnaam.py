# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBevestigingssteunModelnaam(KeuzelijstField):
    """De mogelijke modellen van een bevestigingssteun."""
    naam = 'KlBevestigingssteunModelnaam'
    label = 'Bevestigingssteun modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBevestigingssteunModelnaam'
    definition = 'De mogelijke modellen van een bevestigingssteun.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBevestigingssteunModelnaam'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


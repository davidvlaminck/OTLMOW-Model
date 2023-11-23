# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVerwarmingselementModelnaam(KeuzelijstField):
    """Keuzelijst van modellen van verwarmingselementen voor alle relevante merken."""
    naam = 'KlVerwarmingselementModelnaam'
    label = 'Verwarmingselement model naam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVerwarmingselementModelnaam'
    definition = 'Keuzelijst van modellen van verwarmingselementen voor alle relevante merken.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVerwarmingselementModelnaam'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


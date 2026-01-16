# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMateriaalVoegafdichting(KeuzelijstField):
    """De lijst met mogelijke materialen waaruit de voegafdichting kan bestaan."""
    naam = 'KlMateriaalVoegafdichting'
    label = 'materiaal voegafdichting'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlMateriaalVoegafdichting'
    definition = 'De lijst met mogelijke materialen waaruit de voegafdichting kan bestaan.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMateriaalVoegafdichting'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


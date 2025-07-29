# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMateriaalTaatsschoen(KeuzelijstField):
    """Lijst van mogelijke materialen voor de taatsschoen."""
    naam = 'KlMateriaalTaatsschoen'
    label = 'Materiaal taatsschoen'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlMateriaalTaatsschoen'
    definition = 'Lijst van mogelijke materialen voor de taatsschoen.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMateriaalTaatsschoen'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


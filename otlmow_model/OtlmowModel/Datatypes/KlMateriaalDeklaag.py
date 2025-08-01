# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMateriaalDeklaag(KeuzelijstField):
    """Lijst van mogelijke materialen voor de deklaag."""
    naam = 'KlMateriaalDeklaag'
    label = 'Materiaal deklaag'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlMateriaalDeklaag'
    definition = 'Lijst van mogelijke materialen voor de deklaag.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMateriaalDeklaag'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


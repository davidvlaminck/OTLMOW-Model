# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMateriaalAfdichting(KeuzelijstField):
    """De verschillende opties materiaal waaruit de afdichting kan bestaan."""
    naam = 'KlMateriaalAfdichting'
    label = 'materiaal afdichting'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlMateriaalAfdichting'
    definition = 'De verschillende opties materiaal waaruit de afdichting kan bestaan.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMateriaalAfdichting'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMateriaalBevestigingsbeugel(KeuzelijstField):
    """De verschillende opties materiaal waaruit de bevestigingsbeugel kan bestaan."""
    naam = 'KlMateriaalBevestigingsbeugel'
    label = 'materiaal bevestigingsbeugel'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlMateriaalBevestigingsbeugel'
    definition = 'De verschillende opties materiaal waaruit de bevestigingsbeugel kan bestaan.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMateriaalBevestigingsbeugel'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


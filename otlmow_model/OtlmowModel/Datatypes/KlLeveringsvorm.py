# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLeveringsvorm(KeuzelijstField):
    """De configuratie waarin de plank besteld wordt."""
    naam = 'KlLeveringsvorm'
    label = 'Leveringsvorm'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLeveringsvorm'
    definition = 'De configuratie waarin de plank besteld wordt.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLeveringsvorm'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


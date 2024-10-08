# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlKunststoffenDamplankvorm(KeuzelijstField):
    """De vorm van de kunststoffen damplank."""
    naam = 'KlKunststoffenDamplankvorm'
    label = 'Kunststoffen damplankvorm'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlKunststoffenDamplankvorm'
    definition = 'De vorm van de kunststoffen damplank.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlKunststoffenDamplankvorm'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


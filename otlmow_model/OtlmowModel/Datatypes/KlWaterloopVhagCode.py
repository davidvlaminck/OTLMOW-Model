# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWaterloopVhagCode(KeuzelijstField):
    """De VHAG code voor de waterloop."""
    naam = 'KlWaterloopVhagCode'
    label = 'Waterloop vhag code'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWaterloopVhagCode'
    definition = 'De VHAG code voor de waterloop.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWaterloopVhagCode'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


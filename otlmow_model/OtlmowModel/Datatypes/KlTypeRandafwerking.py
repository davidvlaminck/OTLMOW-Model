# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeRandafwerking(KeuzelijstField):
    """De lijst verschillende types randafwerking."""
    naam = 'KlTypeRandafwerking'
    label = 'type randafwerking'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlTypeRandafwerking'
    definition = 'De lijst verschillende types randafwerking.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeRandafwerking'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


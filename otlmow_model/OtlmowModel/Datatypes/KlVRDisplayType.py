# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVRDisplayType(KeuzelijstField):
    """De mogelijke types van display van een verkeersregelaar."""
    naam = 'KlVRDisplayType'
    label = 'Verkeersregelaar display type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVRDisplayType'
    definition = 'De mogelijke types van display van een verkeersregelaar.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVRDisplayType'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


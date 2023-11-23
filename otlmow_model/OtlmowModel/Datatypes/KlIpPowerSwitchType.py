# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlIpPowerSwitchType(KeuzelijstField):
    """Type van de IP powerswitch."""
    naam = 'KlIpPowerSwitchType'
    label = 'IP powerswitch type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlIpPowerSwitchType'
    definition = 'Type van de IP powerswitch.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlIpPowerSwitchType'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


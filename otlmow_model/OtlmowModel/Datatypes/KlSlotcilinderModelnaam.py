# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSlotcilinderModelnaam(KeuzelijstField):
    """Lijst van modelnamen van slotcilinders volgens de fabrikant."""
    naam = 'KlSlotcilinderModelnaam'
    label = 'Modelnamen slotcilinders'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSlotcilinderModelnaam'
    definition = 'Lijst van modelnamen van slotcilinders volgens de fabrikant.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSlotcilinderModelnaam'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


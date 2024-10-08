# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSlotcilinderMerk(KeuzelijstField):
    """Lijst van merknamen van slotcilinders volgens de fabrikant."""
    naam = 'KlSlotcilinderMerk'
    label = 'Merknamen slotcilinders'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSlotcilinderMerk'
    definition = 'Lijst van merknamen van slotcilinders volgens de fabrikant.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSlotcilinderMerk'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


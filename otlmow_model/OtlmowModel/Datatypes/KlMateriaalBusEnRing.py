# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMateriaalBusEnRing(KeuzelijstField):
    """Lijst met de verschileende materialen van een bus of ring."""
    naam = 'KlMateriaalBusEnRing'
    label = 'Materiaal bus en ring'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlMateriaalBusEnRing'
    definition = 'Lijst met de verschileende materialen van een bus of ring.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMateriaalBusEnRing'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


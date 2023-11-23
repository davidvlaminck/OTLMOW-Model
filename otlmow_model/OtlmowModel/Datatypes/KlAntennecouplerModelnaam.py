# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAntennecouplerModelnaam(KeuzelijstField):
    """Lijst van modelnamen van antennecouplers volgens de fabrikant."""
    naam = 'KlAntennecouplerModelnaam'
    label = 'Antennecoupler modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAntennecouplerModelnaam'
    definition = 'Lijst van modelnamen van antennecouplers volgens de fabrikant.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAntennecouplerModelnaam'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


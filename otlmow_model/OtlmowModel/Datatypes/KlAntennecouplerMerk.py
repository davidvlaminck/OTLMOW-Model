# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAntennecouplerMerk(KeuzelijstField):
    """Lijst van merknamen van antennecouplers volgens de fabrikant."""
    naam = 'KlAntennecouplerMerk'
    label = 'Antennecoupler merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAntennecouplerMerk'
    definition = 'Lijst van merknamen van antennecouplers volgens de fabrikant.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAntennecouplerMerk'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


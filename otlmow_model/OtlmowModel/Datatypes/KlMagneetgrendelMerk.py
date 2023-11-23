# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMagneetgrendelMerk(KeuzelijstField):
    """Lijst van merknamen van magneetgrendels volgens de fabrikant."""
    naam = 'KlMagneetgrendelMerk'
    label = 'Merknamen magneetgrendels'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlMagneetgrendelMerk'
    definition = 'Lijst van merknamen van magneetgrendels volgens de fabrikant.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMagneetgrendelMerk'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


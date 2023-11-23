# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlToegangscontroleSleuteltype(KeuzelijstField):
    """Types voor sleutels die toegang geven tot een behuizing."""
    naam = 'KlToegangscontroleSleuteltype'
    label = 'Toegangscontrole sleuteltype'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlToegangscontroleSleuteltype'
    definition = 'Types voor sleutels die toegang geven tot een behuizing.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlToegangscontroleSleuteltype'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


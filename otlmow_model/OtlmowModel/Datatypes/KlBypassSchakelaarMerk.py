# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBypassSchakelaarMerk(KeuzelijstField):
    """Merknamen voor bypass schakelaars volgens de fabrikant."""
    naam = 'KlBypassSchakelaarMerk'
    label = 'Merknamen bypass schakelaar'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBypassSchakelaarMerk'
    definition = 'Merknamen voor bypass schakelaars volgens de fabrikant.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBypassSchakelaarMerk'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


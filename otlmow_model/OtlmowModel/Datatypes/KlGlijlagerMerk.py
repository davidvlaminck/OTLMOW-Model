# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlGlijlagerMerk(KeuzelijstField):
    """Lijst met merknamen van glijlagers volgens de fabrikant."""
    naam = 'KlGlijlagerMerk'
    label = 'Merknamen van glijlagers'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlGlijlagerMerk'
    definition = 'Lijst met merknamen van glijlagers volgens de fabrikant.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlGlijlagerMerk'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


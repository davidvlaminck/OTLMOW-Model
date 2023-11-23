# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVlotterschakelaarMerk(KeuzelijstField):
    """Merknamen van de vlotterschakelaar."""
    naam = 'KlVlotterschakelaarMerk'
    label = 'Vlotterschakelaar merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVlotterschakelaarMerk'
    definition = 'Merknamen van de vlotterschakelaar.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVlotterschakelaarMerk'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


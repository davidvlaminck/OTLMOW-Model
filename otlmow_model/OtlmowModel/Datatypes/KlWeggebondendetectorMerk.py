# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWeggebondendetectorMerk(KeuzelijstField):
    """Keuzelijst met merknamen voor Weggebondendetector."""
    naam = 'KlWeggebondendetectorMerk'
    label = 'Weggebondendetector merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWeggebondendetectorMerk'
    definition = 'Keuzelijst met merknamen voor Weggebondendetector.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWeggebondendetectorMerk'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


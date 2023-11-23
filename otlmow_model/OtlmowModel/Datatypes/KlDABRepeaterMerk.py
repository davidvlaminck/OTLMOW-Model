# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDABRepeaterMerk(KeuzelijstField):
    """Merknaam van de DAB repeater module."""
    naam = 'KlDABRepeaterMerk'
    label = 'DAB repeater merknaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDABRepeaterMerk'
    definition = 'Merknaam van de DAB repeater module.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDABRepeaterMerk'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


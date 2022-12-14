# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLichtsensorMerk(KeuzelijstField):
    """Lichtsensor merken."""
    naam = 'KlLichtsensorMerk'
    label = 'Lichtsensor merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLichtsensorMerk'
    definition = 'Lichtsensor merken.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLichtsensorMerk'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


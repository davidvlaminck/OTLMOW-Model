# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlUltrasoonNiveaumetingMerk(KeuzelijstField):
    """Merknamen van de ultrasoon niveaumeting."""
    naam = 'KlUltrasoonNiveaumetingMerk'
    label = 'Ultrasoon niveaumeting merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlUltrasoonNiveaumetingMerk'
    definition = 'Merknamen van de ultrasoon niveaumeting.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlUltrasoonNiveaumetingMerk'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


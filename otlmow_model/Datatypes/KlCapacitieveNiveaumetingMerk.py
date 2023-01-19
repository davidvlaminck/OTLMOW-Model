# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlCapacitieveNiveaumetingMerk(KeuzelijstField):
    """Merknamen van de capacitieve niveaumeting."""
    naam = 'KlCapacitieveNiveaumetingMerk'
    label = 'Capacitieve niveaumeting merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlCapacitieveNiveaumetingMerk'
    definition = 'Merknamen van de capacitieve niveaumeting.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlCapacitieveNiveaumetingMerk'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


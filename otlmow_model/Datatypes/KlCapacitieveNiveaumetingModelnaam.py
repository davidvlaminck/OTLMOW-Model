# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlCapacitieveNiveaumetingModelnaam(KeuzelijstField):
    """Modelnaam van de capacitieve niveaumeting."""
    naam = 'KlCapacitieveNiveaumetingModelnaam'
    label = 'Capacitieve niveaumeting modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlCapacitieveNiveaumetingModelnaam'
    definition = 'Modelnaam van de capacitieve niveaumeting.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlCapacitieveNiveaumetingModelnaam'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


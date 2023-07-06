# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlRelaisMerk(KeuzelijstField):
    """Lijst met merknamen voor relais volgens de fabrikant."""
    naam = 'KlRelaisMerk'
    label = 'Merken relais'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlRelaisMerk'
    definition = 'Lijst met merknamen voor relais volgens de fabrikant.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlRelaisMerk'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


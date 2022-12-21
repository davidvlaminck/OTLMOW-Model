# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlContactpuntMerk(KeuzelijstField):
    """Lijst van merknamen van contactpunten volgens de fabrikant."""
    naam = 'KlContactpuntMerk'
    label = 'Merknamen contactpunten'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlContactpuntMerk'
    definition = 'Lijst van merknamen van contactpunten volgens de fabrikant.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlContactpuntMerk'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


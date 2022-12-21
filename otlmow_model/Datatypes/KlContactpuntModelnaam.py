# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlContactpuntModelnaam(KeuzelijstField):
    """Lijst van modelnamen van contactpunten volgens de fabrikant."""
    naam = 'KlContactpuntModelnaam'
    label = 'Modelnamen contactpunten'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlContactpuntModelnaam'
    definition = 'Lijst van modelnamen van contactpunten volgens de fabrikant.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlContactpuntModelnaam'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


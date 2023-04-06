# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLumenOutput(KeuzelijstField):
    """Mogelijke waarden uitgedrukt in Lumens."""
    naam = 'KlLumenOutput'
    label = 'Lumen output'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLumenOutput'
    definition = 'Mogelijke waarden uitgedrukt in Lumens.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLumenOutput'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


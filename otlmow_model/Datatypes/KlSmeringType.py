# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSmeringType(KeuzelijstField):
    """Keuzelijst voor de verschillende wijzen van smering van een mechanisch systeem."""
    naam = 'KlSmeringType'
    label = 'Smering type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlSmeringType'
    definition = 'Keuzelijst voor de verschillende wijzen van smering van een mechanisch systeem.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSmeringType'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


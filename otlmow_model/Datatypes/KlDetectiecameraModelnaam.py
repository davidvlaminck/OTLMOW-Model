# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDetectiecameraModelnaam(KeuzelijstField):
    """Keuzelijst met modelnamen voor Detectiecamera."""
    naam = 'KlDetectiecameraModelnaam'
    label = 'Detectiecamera modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDetectiecameraModelnaam'
    definition = 'Keuzelijst met modelnamen voor Detectiecamera.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDetectiecameraModelnaam'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


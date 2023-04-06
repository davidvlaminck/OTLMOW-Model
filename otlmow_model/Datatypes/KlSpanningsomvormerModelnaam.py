# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSpanningsomvormerModelnaam(KeuzelijstField):
    """Lijst van modelnamen van spanningsomvormers volgens de fabrikant."""
    naam = 'KlSpanningsomvormerModelnaam'
    label = 'Modelnamen spanningsomvormers'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSpanningsomvormerModelnaam'
    definition = 'Lijst van modelnamen van spanningsomvormers volgens de fabrikant.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSpanningsomvormerModelnaam'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


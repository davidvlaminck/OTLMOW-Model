# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSpanningsomvormerMerk(KeuzelijstField):
    """Lijst van merknamen van spanningsomvormers volgens de fabrikant."""
    naam = 'KlSpanningsomvormerMerk'
    label = 'Merknamen spanningsomvormers'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSpanningsomvormerMerk'
    definition = 'Lijst van merknamen van spanningsomvormers volgens de fabrikant.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSpanningsomvormerMerk'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlGroutankerInjectie(KeuzelijstField):
    """Manier waarop het groutanker wordt uitgevoerd."""
    naam = 'KlGroutankerInjectie'
    label = 'groutanker injectie'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlGroutankerInjectie'
    definition = 'Manier waarop het groutanker wordt uitgevoerd.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlGroutankerInjectie'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


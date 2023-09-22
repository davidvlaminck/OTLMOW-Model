# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeGrondanker(KeuzelijstField):
    """De mogelijke types grondanker."""
    naam = 'KlTypeGrondanker'
    label = 'Type grondanker'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlTypeGrondanker'
    definition = 'De mogelijke types grondanker.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeGrondanker'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


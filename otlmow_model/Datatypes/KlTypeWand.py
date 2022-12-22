# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeWand(KeuzelijstField):
    """De functie die de wand uitoefent."""
    naam = 'KlTypeWand'
    label = 'Type wand'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlTypeWand'
    definition = 'De functie die de wand uitoefent.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeWand'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


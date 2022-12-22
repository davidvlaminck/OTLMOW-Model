# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeSpankabel(KeuzelijstField):
    """Het type waaruit de spankabel is opgebouwd."""
    naam = 'KlTypeSpankabel'
    label = 'Type spankabel'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTypeSpankabel'
    definition = 'Het type waaruit de spankabel is opgebouwd.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeSpankabel'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


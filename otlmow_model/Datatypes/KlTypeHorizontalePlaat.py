# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeHorizontalePlaat(KeuzelijstField):
    """Het type horizontale plaat."""
    naam = 'KlTypeHorizontalePlaat'
    label = 'Type horizontale plaat'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlTypeHorizontalePlaat'
    definition = 'Het type horizontale plaat.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeHorizontalePlaat'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


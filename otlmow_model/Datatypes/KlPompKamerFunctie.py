# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPompKamerFunctie(KeuzelijstField):
    """De mogelijke functies die een pompkamer kan invullen."""
    naam = 'KlPompKamerFunctie'
    label = 'Kamer functie'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlPompKamerFunctie'
    definition = 'De mogelijke functies die een pompkamer kan invullen.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPompKamerFunctie'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


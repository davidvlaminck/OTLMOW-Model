# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeLandhoofd(KeuzelijstField):
    """Het type landhoofd."""
    naam = 'KlTypeLandhoofd'
    label = 'Type landhoofd'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlTypeLandhoofd'
    definition = 'Het type landhoofd.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeLandhoofd'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


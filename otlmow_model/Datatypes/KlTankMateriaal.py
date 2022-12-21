# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTankMateriaal(KeuzelijstField):
    """Het materiaal waaruit de tank vervaardigd is."""
    naam = 'KlTankMateriaal'
    label = 'Tank materiaal'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTankMateriaal'
    definition = 'Het materiaal waaruit de tank vervaardigd is.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTankMateriaal'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


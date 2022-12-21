# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSiloMateriaal(KeuzelijstField):
    """Het materiaal waaruit de silo vervaardigd is."""
    naam = 'KlSiloMateriaal'
    label = 'Silo materiaal'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSiloMateriaal'
    definition = 'Het materiaal waaruit de silo vervaardigd is.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSiloMateriaal'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAfsluitingMateriaal(KeuzelijstField):
    """Het materiaal waaruit de afsluiting vervaardigd is."""
    naam = 'KlAfsluitingMateriaal'
    label = 'Afsluiting materiaal'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAfsluitingMateriaal'
    definition = 'Het materiaal waaruit de afsluiting vervaardigd is.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAfsluitingMateriaal'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)


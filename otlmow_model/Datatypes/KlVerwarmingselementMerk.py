# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVerwarmingselementMerk(KeuzelijstField):
    """Keuzelijst van merken voor verwarmingselementen."""
    naam = 'KlVerwarmingselementMerk'
    label = 'Verwarmingselement merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVerwarmingselementMerk'
    definition = 'Keuzelijst van merken voor verwarmingselementen.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVerwarmingselementMerk'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

